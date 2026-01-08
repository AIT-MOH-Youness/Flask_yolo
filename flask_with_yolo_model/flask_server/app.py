"""
Flask Server for YOLO Sign Detection + Gemini Navigation
Processes images with YOLO model and provides navigation guidance via Gemini AI
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image
import google.generativeai as genai
import io
import base64
from typing import List, Dict, Tuple
import time
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for Android client

# Configuration
# Prefer environment variables in container; fall back to existing default for local dev
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyAFI6e8LMl2e3XOJe4VcJmn8W84ZHCk9U4")
YOLO_MODEL_PATH = os.getenv("YOLO_MODEL_PATH", "bestLichir (1).pt")

# Initialize models
print("🔄 Loading YOLO model...")
yolo_model = YOLO(YOLO_MODEL_PATH)
print("✅ YOLO model loaded successfully!")

print("🔄 Configuring Gemini AI...")
genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel('gemini-flash-latest')
print("✅ Gemini AI configured successfully!")


def determine_position(center_x: float, center_y: float, img_width: int, img_height: int) -> Dict[str, str]:
    """Determine object position in image (horizontal and vertical)"""
    
    # Horizontal position
    if center_x < img_width * 0.33:
        h_position = "LEFT"
    elif center_x > img_width * 0.67:
        h_position = "RIGHT"
    else:
        h_position = "CENTER"
    
    # Vertical position
    if center_y < img_height * 0.33:
        v_position = "ABOVE"
    elif center_y > img_height * 0.67:
        v_position = "BELOW"
    else:
        v_position = "EYE_LEVEL"
    
    return {
        "horizontal": h_position,
        "vertical": v_position
    }


def get_navigation_from_gemini(cropped_image: Image.Image) -> str:
    """Get navigation instructions from Gemini for a cropped sign image"""
    
    prompt = """Lis ce panneau et dis-moi EXACTEMENT quelles destinations il indique et quelle direction prendre pour chacune.

Formate ta réponse comme ceci:
- [Destination 1]: [direction - gauche/droite/tout droit]
- [Destination 2]: [direction - gauche/droite/tout droit]

Exemples:
"Gare: À gauche, Aéroport: À droite, Continuez tout droit pour trouver le Métro"
ou
"Limite de vitesse: 50 km/h"
ou
"Arrêt obligatoire"

Sois extrêmement concis. Indique uniquement ce qui est écrit sur le panneau et la direction à prendre. Maximum 30 mots. Réponds TOUJOURS en français."""
    
    try:
        response = gemini_model.generate_content([prompt, cropped_image])
        return response.text.strip()
    except Exception as e:
        print(f"❌ Gemini API error: {e}")
        return f"Impossible de lire le panneau: {str(e)}"


def process_detection(img: np.ndarray, box, idx: int, img_width: int, img_height: int) -> Dict:
    """Process a single YOLO detection"""
    
    # Extract bounding box data
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    conf = float(box.conf[0])
    cls = int(box.cls[0])
    label = yolo_model.names[cls]
    
    # Calculate center position
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    
    # Determine position
    position = determine_position(center_x, center_y, img_width, img_height)
    
    # Crop the detected object
    cropped = img[y1:y2, x1:x2]
    
    if cropped.size == 0:
        return None
    
    # Convert to PIL Image for Gemini
    cropped_rgb = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(cropped_rgb)
    
    # Get navigation instructions from Gemini
    print(f"🔄 Getting navigation for detection {idx + 1}...")
    navigation_text = get_navigation_from_gemini(pil_image)
    
    return {
        "id": idx,
        "label": label,
        "confidence": round(conf, 3),
        "bbox": [x1, y1, x2, y2],
        "position": position,
        "navigation_text": navigation_text
    }


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "models": {
            "yolo": "loaded",
            "gemini": "configured"
        }
    }), 200


@app.route('/detect-signs', methods=['POST'])
def detect_signs():
    """
    Main endpoint: Detect signs with YOLO and get navigation instructions from Gemini
    
    Expected: multipart/form-data with 'image' field
    Returns: JSON with detections and navigation instructions
    """
    
    start_time = time.time()
    
    # Validate request
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    file = request.files['image']
    
    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400
    
    try:
        # Read image
        image_bytes = file.read()
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            return jsonify({"error": "Invalid image format"}), 400
        
        img_height, img_width = img.shape[:2]
        print(f"📷 Processing image: {img_width}x{img_height}")
        
        # Run YOLO detection
        print("🔄 Running YOLO detection...")
        results = yolo_model(img)
        
        num_detections = len(results[0].boxes)
        print(f"✅ Found {num_detections} objects")
        
        if num_detections == 0:
            return jsonify({
                "detections": [],
                "message": "No signs detected in the image",
                "processing_time": round(time.time() - start_time, 2)
            }), 200
        
        # Process each detection
        detections = []
        for idx, box in enumerate(results[0].boxes):
            detection = process_detection(img, box, idx, img_width, img_height)
            if detection:
                detections.append(detection)
                print(f"✅ Detection {idx + 1}: {detection['label']} - {detection['position']['horizontal']}")
        
        processing_time = round(time.time() - start_time, 2)
        
        return jsonify({
            "success": True,
            "detections": detections,
            "total_detections": len(detections),
            "processing_time": processing_time
        }), 200
        
    except Exception as e:
        print(f"❌ Error processing image: {e}")
        return jsonify({
            "error": f"Processing failed: {str(e)}"
        }), 500


@app.route('/test', methods=['GET'])
def test():
    """Test endpoint"""
    return jsonify({
        "message": "Flask YOLO + Gemini Server is running!",
        "endpoints": {
            "health": "/health",
            "detect": "/detect-signs (POST with image)"
        }
    }), 200


if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 Flask Server Starting...")
    print("🎯 YOLO Model: Loaded")
    print("🤖 Gemini AI: Configured")
    print("="*50 + "\n")
    
    # Run server on all interfaces, port 8080 (common port, less likely blocked)
    app.run(host='0.0.0.0', port=8080, debug=True)
