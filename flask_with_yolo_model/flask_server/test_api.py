"""
Script de test pour l'API Flask YOLO + Gemini
"""

import requests
import sys
from pathlib import Path

# Configuration
BASE_URL = "http://127.0.0.1:8080"  # Changez selon votre IP

def test_health():
    """Test de santé du serveur"""
    print("🔍 Test 1: Health Check")
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        if response.status_code == 200:
            print("✅ Serveur accessible")
            print(f"   Réponse: {response.json()}")
            return True
        else:
            print(f"❌ Erreur: Status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Impossible de se connecter au serveur: {e}")
        print("\n💡 Assurez-vous que:")
        print("   1. Le serveur Flask est lancé (python app.py)")
        print("   2. Vous êtes sur le même WiFi")
        print("   3. L'URL est correcte dans le script")
        return False

def test_detect_signs(image_path):
    """Test de détection de panneaux"""
    print("\n🔍 Test 2: Détection de Panneaux")
    
    if not Path(image_path).exists():
        print(f"❌ Image introuvable: {image_path}")
        return False
    
    try:
        with open(image_path, 'rb') as img_file:
            files = {'image': img_file}
            print("📤 Envoi de l'image...")
            response = requests.post(
                f"{BASE_URL}/detect-signs",
                files=files,
                timeout=60  # 60 secondes pour le traitement
            )
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Détection réussie")
            print(f"   Panneaux détectés: {data.get('total_detections', 0)}")
            print(f"   Temps de traitement: {data.get('processing_time', 0)}s")
            
            for i, detection in enumerate(data.get('detections', []), 1):
                print(f"\n   📍 Panneau {i}:")
                print(f"      Label: {detection['label']}")
                print(f"      Confiance: {detection['confidence']:.2%}")
                print(f"      Position: {detection['position']}")
                print(f"      Navigation: {detection['navigation_text']}")
            
            return True
        else:
            print(f"❌ Erreur: Status {response.status_code}")
            print(f"   Réponse: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Erreur lors de la requête: {e}")
        return False

def main():
    print("="*60)
    print("🧪 Test du Serveur Flask YOLO + Gemini")
    print("="*60)
    
    # Test 1: Health check
    if not test_health():
        print("\n❌ Le serveur n'est pas accessible. Arrêt des tests.")
        sys.exit(1)
    
    # Test 2: Détection (optionnel - nécessite une image)
    print("\n" + "="*60)
    image_path = input("📸 Entrez le chemin d'une image de panneau (ou appuyez sur Entrée pour passer): ").strip()
    
    if image_path:
        test_detect_signs(image_path)
    else:
        print("⏭️  Test de détection ignoré")
    
    print("\n" + "="*60)
    print("✅ Tests terminés!")
    print("="*60)

if __name__ == "__main__":
    main()
