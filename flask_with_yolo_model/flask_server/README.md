# 🚀 Flask YOLO + Gemini Server

Serveur Flask pour la détection de panneaux avec YOLO et guidage par Gemini AI.

## 📦 Installation

### 1. Créer un environnement virtuel

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Placer le modèle YOLO

Copiez le fichier `bestLichir (1).pt` dans le dossier `flask_server/`

```
flask_server/
├── app.py
├── bestLichir (1).pt  ← Placez le modèle ici
├── requirements.txt
└── README.md
```

## 🎯 Lancer le serveur

```bash
python app.py
```

Le serveur démarre sur : `http://0.0.0.0:8080`

## 🌐 Trouver votre adresse IP locale

### Windows (PowerShell)
```powershell
ipconfig
# Cherchez "IPv4 Address" sous votre adaptateur réseau
# Ex: 192.168.1.100
```

### Linux/Mac
```bash
ifconfig | grep "inet "
# ou
ip addr show
```

## 📡 API Endpoints

### 1. Test de santé
```http
GET http://192.168.x.x:8080/health
```

**Réponse :**
```json
{
  "status": "healthy",
  "models": {
    "yolo": "loaded",
    "gemini": "configured"
  }
}
```

### 2. Détection de panneaux
```http
POST http://192.168.x.x:8080/detect-signs
Content-Type: multipart/form-data

body: image=[fichier image]
```

**Réponse :**
```json
{
  "success": true,
  "detections": [
    {
      "id": 0,
      "label": "panneau_direction",
      "confidence": 0.95,
      "bbox": [120, 50, 300, 200],
      "position": {
        "horizontal": "LEFT",
        "vertical": "EYE_LEVEL"
      },
      "navigation_text": "Gare SNCF: Tournez à gauche, Métro: Continuez tout droit"
    }
  ],
  "total_detections": 1,
  "processing_time": 2.3
}
```

## 🔧 Configuration Android

Dans votre app Android, mettez à jour l'URL :

```kotlin
// Remplacez x.x par votre IP locale (ex: 192.168.1.100)
private const val BASE_URL = "http://192.168.1.100:8080/"
```

## 🧪 Test avec cURL

```bash
curl -X POST -F "image=@test_image.jpg" http://192.168.1.100:8080/detect-signs
```

## 🐳 Exécution avec Docker

Assurez-vous que le fichier du modèle YOLO `bestLichir (1).pt` se trouve dans le dossier `flask_server/` avant de construire l'image.

Depuis la racine du projet `flask_with_yolo_model/` :

```powershell
docker build -t flask-yolo-gemini .

docker run --rm -p 8080:8080 `
  -e GEMINI_API_KEY="VOTRE_CLE_GEMINI" `
  -e YOLO_MODEL_PATH="bestLichir (1).pt" `
  flask-yolo-gemini
```

Le serveur sera accessible sur : `http://localhost:8080`

## 📝 Notes

- Le serveur doit être sur le **même réseau WiFi** que votre téléphone Android
- Vérifiez que votre **pare-feu** autorise le port 5000
- Le modèle YOLO doit être dans le même dossier que `app.py`
- La clé API Gemini est déjà configurée dans le code

## 🐛 Dépannage

### Le serveur ne démarre pas
- Vérifiez que Python 3.8+ est installé
- Vérifiez que toutes les dépendances sont installées

### L'app Android ne se connecte pas
- Vérifiez votre adresse IP avec `ipconfig` (Windows) ou `ifconfig` (Linux/Mac)
- Vérifiez que téléphone et PC sont sur le même WiFi
- Essayez de désactiver temporairement le pare-feu

### YOLO model not found
- Assurez-vous que `bestLichir (1).pt` est dans le dossier `flask_server/`
- Vérifiez le nom du fichier (espaces, parenthèses)
