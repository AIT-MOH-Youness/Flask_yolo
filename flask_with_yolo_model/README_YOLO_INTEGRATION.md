# 🎯 Guide de Gare - Navigation par Panneaux YOLO

## 📱 Application d'Assistance pour Personnes Malvoyantes

Application Android avec détection intelligente de panneaux utilisant **YOLO + Gemini AI** et instructions vocales en français.

---

## ✨ Fonctionnalités

### 1. ✅ Détection d'Objets (Gemini AI)
- Billetterie, escaliers, ascenseurs, escalators
- Valideurs de billets, bandes de guidage
- Quais, chaises, toilettes
- Instructions vocales contextuelles

### 2. 🚧 Reconnaissance de Signes (Mockée)
- Interface complète
- Prête pour implémentation future

### 3. 🆕 **Navigation par Panneaux YOLO** (Nouveau!)
- ✅ Détection avancée avec **YOLO v8**
- ✅ Analyse contextuelle par **Gemini 2.5 Flash**
- ✅ Instructions vocales automatiques (Text-to-Speech)
- ✅ Position des panneaux (gauche/droite/haut/bas)
- ✅ Serveur Flask dédié
- ✅ Architecture MVI propre

---

## 🏗️ Architecture

### Application Android
```
Clean Architecture + MVI Pattern

📦 app/
├── 📱 presentation/     → UI (Jetpack Compose + MVI)
│   ├── screens/
│   │   ├── home/
│   │   ├── objectdetection/
│   │   ├── signrecognition/
│   │   └── signnavigation/  ← NOUVEAU!
│   ├── navigation/
│   └── util/
│       └── TextToSpeechManager  ← NOUVEAU!
│
├── 💼 domain/          → Business Logic
│   ├── model/
│   ├── repository/
│   └── usecase/
│
└── 🗄️ data/           → Data Sources
    ├── remote/
    │   └── api/
    │       ├── GeminiApiService
    │       └── FlaskYoloApiService  ← NOUVEAU!
    ├── repository/
    └── di/
```

### Serveur Flask
```
flask_server/
├── app.py              → API principale
├── requirements.txt    → Dépendances Python
├── bestLichir (1).pt  → Modèle YOLO (6 MB)
├── install.bat        → Installation auto
└── start_server.bat   → Démarrage auto
```

---

## 🚀 Installation & Démarrage

### 📋 Option 1 : Démarrage Rapide (Recommandé)

Voir **[QUICK_START.md](QUICK_START.md)** - Configuration en 5 minutes

### 📋 Option 2 : Guide Complet

Voir **[pils_mobile/SIGN_NAVIGATION_GUIDE.md](pils_mobile/SIGN_NAVIGATION_GUIDE.md)**

### ⚡ Résumé Ultra-Rapide

```bash
# 1. Serveur Flask
cd flask_server
install.bat              # Installation
# Copier bestLichir (1).pt dans flask_server/
start_server.bat         # Démarrage

# 2. Trouver votre IP
ipconfig  # Ex: 192.168.1.100

# 3. Android
# Modifier pils_mobile/data/src/main/java/com/insa/foodies/data/di/DataModule.kt
# Ligne 26: FLASK_BASE_URL = "http://192.168.1.100:5000/"
# Sync Gradle + Run

# 4. Tester
# Ouvrir app → Navigation par Panneaux → Prendre photo
```

---

## 📦 Technologies Utilisées

### Android
- **Kotlin** - Langage principal
- **Jetpack Compose** - UI moderne
- **MVI Pattern** - Architecture réactive
- **Dagger Hilt** - Injection de dépendances
- **Retrofit** - Client HTTP
- **CameraX** - Gestion caméra
- **Text-to-Speech** - Synthèse vocale
- **Coroutines** - Programmation asynchrone

### Backend
- **Flask** - Framework web Python
- **YOLO v8** (Ultralytics) - Détection d'objets
- **Google Gemini 2.5 Flash** - Analyse contextuelle
- **OpenCV** - Traitement d'images
- **PyTorch** - Framework ML

---

## 🎯 Workflow - Navigation par Panneaux

```
┌─────────────────────┐
│   Utilisateur       │
│   Prend une photo   │
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│   Android App       │
│   Encode image      │
└──────────┬──────────┘
           │ HTTP POST
           │ multipart/form-data
           ↓
┌─────────────────────┐
│   Flask Server      │
│   (192.168.x.x)     │
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│   YOLO Inference    │
│   Détecte panneaux  │
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│   Crop chaque       │
│   panneau détecté   │
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│   Gemini AI         │
│   Analyse crop +    │
│   Instructions      │
└──────────┬──────────┘
           │ JSON Response
           ↓
┌─────────────────────┐
│   Android App       │
│   Affichage +       │
│   Text-to-Speech    │
└─────────────────────┘
```

---

## 📊 Format API

### Request
```http
POST http://192.168.x.x:5000/detect-signs
Content-Type: multipart/form-data

image: [fichier .jpg/.png]
```

### Response
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
      "navigation_text": "Gare SNCF: Tournez à gauche..."
    }
  ],
  "total_detections": 1,
  "processing_time": 2.3
}
```

---

## 🎨 Captures d'Écran (Conceptuelles)

### Écran d'Accueil
- ✅ Identifier les objets
- ✅ Guider par les signes
- 🆕 **Navigation par Panneaux (YOLO)**

### Écran Navigation par Panneaux
1. Boutons Caméra/Galerie
2. Indicateur de progression (YOLO + Gemini)
3. Liste des panneaux détectés :
   - Label + Confiance
   - Position (badges colorés)
   - Instructions de navigation
   - Bouton audio 🔊 par panneau
4. Lecture automatique du premier résultat

---

## 🔧 Configuration

### Variables d'Environnement

#### Android (`DataModule.kt`)
```kotlin
private const val FLASK_BASE_URL = "http://192.168.1.100:5000/"
```

#### Flask (`app.py`)
```python
GEMINI_API_KEY = "AIzaSyCEc9m1T5VMKHzwQxjbdmUiIdJDqT6ALsg"
YOLO_MODEL_PATH = "bestLichir (1).pt"
```

---

## 🧪 Tests

### Test Serveur Flask
```bash
cd flask_server
python test_api.py
```

### Test Android
```bash
cd pils_mobile
./gradlew test
./gradlew connectedAndroidTest
```

### Test Manuel
1. Lancer serveur Flask
2. Ouvrir app Android
3. Navigation par Panneaux → Galerie
4. Sélectionner image de test
5. Vérifier détection + audio

---

## 📝 Fichiers de Documentation

- **[QUICK_START.md](QUICK_START.md)** - Démarrage en 5 minutes
- **[pils_mobile/SIGN_NAVIGATION_GUIDE.md](pils_mobile/SIGN_NAVIGATION_GUIDE.md)** - Guide complet
- **[pils_mobile/ARCHITECTURE_MVI_GUIDE.md](pils_mobile/ARCHITECTURE_MVI_GUIDE.md)** - Architecture MVI
- **[pils_mobile/DEVELOPER_GUIDE.md](pils_mobile/DEVELOPER_GUIDE.md)** - Guide développeur
- **[flask_server/README.md](flask_server/README.md)** - Documentation serveur

---

## 🐛 Dépannage

### Erreur de connexion
1. Vérifier serveur Flask lancé
2. Même WiFi PC/téléphone
3. IP correcte dans `DataModule.kt`
4. Pare-feu autorise port 5000

### YOLO model not found
```cmd
copy "bestLichir (1).pt" flask_server\
```

### Gradle sync failed
```bash
cd pils_mobile
./gradlew clean build
```

---

## 👥 Équipe

Projet développé pour l'assistance aux personnes malvoyantes dans les gares.

---

## 📄 Licence

Ce projet est développé dans un cadre éducatif.

---

## 🎉 Nouveautés v2.0

✅ **Navigation par Panneaux YOLO**
- Détection YOLO v8 avec modèle personnalisé
- Analyse contextuelle Gemini 2.5 Flash
- Text-to-Speech automatique en français
- Serveur Flask dédié (6 MB modèle)
- Architecture MVI complète
- Position spatiale des panneaux
- Interface utilisateur moderne

---

## 📞 Support

Pour toute question :
1. Consulter [QUICK_START.md](QUICK_START.md)
2. Consulter [SIGN_NAVIGATION_GUIDE.md](pils_mobile/SIGN_NAVIGATION_GUIDE.md)
3. Vérifier les logs Flask et Android Logcat

---

**🚀 Prêt à naviguer intelligemment !**
