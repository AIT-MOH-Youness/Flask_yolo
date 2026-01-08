# 🌳 Arborescence Complète du Projet

> Structure détaillée de tous les fichiers créés/modifiés

---

## 📦 Vue d'Ensemble

```
PILS-07-01-2026/
│
├── 📄 Documentation Principale (12 fichiers)
├── 🐍 Flask Server (7 fichiers)
├── 📱 Android App (25 fichiers créés/modifiés)
└── ⚙️ Configuration (2 fichiers)

Total : 46 fichiers
```

---

## 📚 Documentation à la Racine

```
PILS-07-01-2026/
│
├── 📘 README.md                         ⭐ README principal GitHub
├── 📘 INDEX.md                          📚 Index navigation docs
├── 📘 START_HERE.md                     🚀 Démarrage ultra-rapide (8 min)
├── 📘 VISUAL_GUIDE.md                   🖼️ Guide visuel complet
├── 📘 QUICK_START.md                    ⚡ Installation 5 minutes
├── 📘 IMPLEMENTATION_COMPLETE.md        ✅ Résumé implémentation
├── 📘 CHANGELOG.md                      📋 Liste modifications
├── 📘 README_YOLO_INTEGRATION.md        🎯 Vue d'ensemble YOLO
├── 📘 GITHUB_SETUP.md                   🌐 Publication GitHub
├── 📘 CONTRIBUTING.md                   🤝 Guide contribution
├── 📘 PROJECT_STATUS.md                 📊 État du projet
│
├── 📄 LICENSE                           ⚖️ MIT License
├── 📄 .gitignore                        🚫 Exclusions Git
│
├── 🔬 notebooka3961d96ba (1).ipynb     📓 Notebook Jupyter (référence)
├── 🤖 bestLichir (1).pt                🎯 Modèle YOLO (6 MB)
└── 🤖 bestLichir (1).onnx              🎯 Modèle ONNX (référence)
```

### Description Fichiers Documentation

| Fichier | Description | Durée Lecture |
|---------|-------------|---------------|
| **README.md** | README principal pour GitHub avec badges | 5 min |
| **INDEX.md** | Navigation complète de toute la documentation | 3 min |
| **START_HERE.md** | Guide ultra-rapide en 3 étapes | 8 min |
| **VISUAL_GUIDE.md** | Guide visuel étape par étape avec captures | 15 min |
| **QUICK_START.md** | Installation rapide en ligne de commande | 10 min |
| **IMPLEMENTATION_COMPLETE.md** | Résumé de l'implémentation complète | 10 min |
| **CHANGELOG.md** | Liste détaillée de tous les changements | 5 min |
| **README_YOLO_INTEGRATION.md** | Vue d'ensemble architecture YOLO | 12 min |
| **GITHUB_SETUP.md** | Guide publication sur GitHub | 15 min |
| **CONTRIBUTING.md** | Guide pour contributeurs | 10 min |
| **PROJECT_STATUS.md** | État complet du projet | 8 min |

---

## 🐍 Flask Server

```
flask_server/
│
├── 🐍 app.py                            ⭐ API Flask principale
│   ├── POST /detect-signs               📸 Endpoint détection
│   ├── GET /health                      💚 Health check
│   └── GET /test                        🧪 Test endpoint
│
├── 📋 requirements.txt                  📦 Dépendances Python
│   ├── flask==3.0.0
│   ├── flask-cors==4.0.0
│   ├── ultralytics==8.1.0               🤖 YOLO v8
│   ├── opencv-python==4.8.1.78
│   ├── pillow==10.1.0
│   ├── google-generativeai==0.3.2       🤖 Gemini API
│   ├── numpy==1.24.3
│   ├── torch==2.1.1
│   └── torchvision==0.16.1
│
├── 📄 install.bat                       🔧 Installation automatique
│   ├── Crée venv Python
│   ├── Installe requirements.txt
│   └── Vérifie modèle YOLO
│
├── 📄 start_server.bat                  🚀 Lancement serveur
│   ├── Active venv
│   ├── Vérifie modèle + API key
│   └── Lance Flask port 5000
│
├── 🧪 test_api.py                       ✅ Tests API
│   ├── test_health_check()
│   └── test_detect_signs()
│
├── 📘 README.md                         📚 Documentation serveur
│   ├── Installation Python
│   ├── Configuration modèle
│   ├── Endpoints API
│   └── Tests cURL
│
├── 📄 .gitignore                        🚫 Exclusions
│   ├── venv/
│   ├── __pycache__/
│   └── *.pyc
│
└── 🤖 bestLichir (1).pt                🎯 Modèle YOLO (à copier)
    (6 MB - non sur GitHub)
```

### API Flask

```http
POST /detect-signs
Content-Type: multipart/form-data

Parameters:
  - image: File (jpg/png)

Response:
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
      "navigation_text": "Gare SNCF: Tournez à gauche"
    }
  ],
  "total_detections": 1,
  "processing_time": 2.3,
  "message": "Detection completed successfully"
}
```

---

## 📱 Android App

### Structure Générale

```
pils_mobile/
│
├── 📱 app/                              📦 Module principal
│   ├── build.gradle.kts
│   ├── proguard-rules.pro
│   └── src/
│       ├── main/
│       │   ├── AndroidManifest.xml
│       │   ├── java/com/insa/foodies/
│       │   │   └── FoodiesApplication.kt
│       │   └── res/                     🎨 Resources
│       ├── test/                        🧪 Tests unitaires
│       └── androidTest/                 📱 Tests instrumentés
│
├── 🧠 domain/                           💼 Business Logic
├── 💾 data/                             🗄️ Data Layer
├── 🎨 presentation/                     📱 UI Layer
│
├── 🔧 gradle/
│   ├── libs.versions.toml               📋 Versions centralisées
│   └── wrapper/
│
├── 📄 build.gradle.kts                  🔨 Build racine
├── 📄 settings.gradle.kts               ⚙️ Settings
├── 📄 gradle.properties                 🔧 Properties
├── 📄 local.properties                  🔒 Paths locaux
│
└── 📚 Documentation
    ├── ARCHITECTURE_MVI_GUIDE.md        🏗️ Guide MVI
    ├── DEVELOPER_GUIDE.md               👨‍💻 Guide développeur
    ├── PROJECT_SUMMARY.md               📊 Résumé projet
    └── ...
```

---

### 🧠 Domain Layer (5 fichiers créés)

```
domain/src/main/java/com/insa/foodies/domain/
│
├── 📦 model/
│   ├── SignPosition.kt                  📍 Position panneaux
│   │   ├── enum HorizontalPosition
│   │   │   ├── LEFT
│   │   │   ├── CENTER
│   │   │   └── RIGHT
│   │   └── enum VerticalPosition
│   │       ├── ABOVE
│   │       ├── EYE_LEVEL
│   │       └── BELOW
│   │
│   ├── DetectedSign.kt                  🪧 Panneau détecté
│   │   ├── data class DetectedSign
│   │   │   ├── id: Int
│   │   │   ├── label: String
│   │   │   ├── confidence: Float
│   │   │   ├── boundingBox: BoundingBox
│   │   │   ├── position: SignPosition
│   │   │   └── navigationText: String
│   │   └── data class BoundingBox
│   │       ├── x1: Int
│   │       ├── y1: Int
│   │       ├── x2: Int
│   │       └── y2: Int
│   │
│   └── SignNavigationResult.kt          ✅ Résultat complet
│       ├── signs: List<DetectedSign>
│       ├── totalDetections: Int
│       ├── processingTime: Double
│       └── message: String?
│
├── 📦 repository/
│   └── SignNavigationRepository.kt      🔌 Interface repository
│       └── suspend fun detectSignsAndNavigate()
│
└── 📦 usecase/
    └── NavigateWithSignsUseCase.kt     🎯 Use case
        └── operator fun invoke()
```

**Principe** : Aucune dépendance Android/Framework dans Domain

---

### 💾 Data Layer (4 créés + 1 modifié)

```
data/src/main/java/com/insa/foodies/data/
│
├── 📦 remote/
│   ├── api/
│   │   └── FlaskYoloApiService.kt       🌐 API Retrofit
│   │       └── @POST("detect-signs")
│   │           suspend fun detectSigns()
│   │
│   └── dto/
│       └── SignDetectionResponseDto.kt   📋 DTOs
│           ├── data class SignDetectionResponseDto
│           ├── data class DetectedSignDto
│           └── data class PositionDto
│
├── 📦 mapper/
│   └── FlaskYoloMapper.kt               🔄 Mapper DTO→Domain
│       └── fun toDomain(): SignNavigationResult
│
├── 📦 repository/
│   └── SignNavigationRepositoryImpl.kt   ✅ Implementation
│       ├── @Inject constructor
│       └── override suspend fun detectSignsAndNavigate()
│
└── 📦 di/
    └── DataModule.kt                    💉 Dependency Injection
        ├── FLASK_BASE_URL               🌐 "http://192.168.1.100:5000/"
        ├── @Provides provideFlaskRetrofit()
        ├── @Provides provideFlaskYoloApi()
        └── @Binds bindSignNavigationRepo()
```

**Ligne importante** : `DataModule.kt` ligne 26
```kotlin
private const val FLASK_BASE_URL = "http://192.168.1.100:5000/"
```
👉 Remplacer `192.168.1.100` par votre IP locale

---

### 🎨 Presentation Layer (4 créés + 3 modifiés)

```
presentation/src/main/java/com/insa/foodies/presentation/
│
├── 📦 screens/
│   ├── signnavigation/
│   │   ├── SignNavigationContract.kt    📋 MVI Contract
│   │   │   ├── data class State
│   │   │   │   ├── isLoading: Boolean
│   │   │   │   ├── detectedSigns: List
│   │   │   │   ├── error: String?
│   │   │   │   ├── processingTime: Double?
│   │   │   │   └── currentSpeakingIndex: Int?
│   │   │   ├── sealed interface Event
│   │   │   │   ├── OnCameraClick
│   │   │   │   ├── OnGalleryClick
│   │   │   │   ├── OnImageCaptured
│   │   │   │   ├── OnImageSelected
│   │   │   │   ├── OnSpeakSign
│   │   │   │   ├── OnStopSpeaking
│   │   │   │   └── OnClearResults
│   │   │   └── sealed interface Effect
│   │   │       ├── NavigateToCamera
│   │   │       ├── NavigateToGallery
│   │   │       ├── ShowError
│   │   │       └── ShowSuccess
│   │   │
│   │   ├── SignNavigationViewModel.kt   🧠 ViewModel
│   │   │   ├── @HiltViewModel
│   │   │   ├── @Inject constructor
│   │   │   ├── fun onEvent(Event)
│   │   │   ├── private suspend fun detectSigns()
│   │   │   ├── private fun speakSign()
│   │   │   └── private fun getPositionText()
│   │   │
│   │   ├── SignNavigationScreen.kt      📱 Composable UI
│   │   │   ├── @Composable SignNavigationScreen()
│   │   │   ├── @Composable CameraGalleryButtons()
│   │   │   ├── @Composable LoadingIndicator()
│   │   │   ├── @Composable ErrorMessage()
│   │   │   ├── @Composable DetectedSignsList()
│   │   │   └── @Composable SignCard()
│   │   │
│   │   └── SIGN_NAVIGATION_GUIDE.md     📘 Guide détaillé
│   │
│   └── home/
│       └── HomeScreen.kt                🏠 [MODIFIÉ]
│           └── + FeatureCard("Navigation par Panneaux")
│
├── 📦 navigation/
│   ├── Screen.kt                        🧭 [MODIFIÉ]
│   │   └── + object SignNavigation : Screen("sign_navigation")
│   │
│   └── NavGraph.kt                      🗺️ [MODIFIÉ]
│       └── + composable(Screen.SignNavigation.route) { ... }
│
└── 📦 util/
    └── TextToSpeechManager.kt           🔊 TTS Service
        ├── @Singleton
        ├── @Inject constructor
        ├── fun speak(text: String)
        ├── fun stop()
        ├── fun isSpeaking(): Boolean
        └── fun shutdown()
```

---

## 📊 Récapitulatif par Type

### Fichiers Créés (32)

#### Documentation (11)
- README.md (principal)
- INDEX.md
- START_HERE.md
- VISUAL_GUIDE.md
- QUICK_START.md
- IMPLEMENTATION_COMPLETE.md
- CHANGELOG.md
- README_YOLO_INTEGRATION.md
- GITHUB_SETUP.md
- CONTRIBUTING.md
- PROJECT_STATUS.md

#### Flask Backend (7)
- app.py
- requirements.txt
- install.bat
- start_server.bat
- test_api.py
- README.md
- .gitignore

#### Android Domain (5)
- SignPosition.kt
- DetectedSign.kt
- SignNavigationResult.kt
- SignNavigationRepository.kt
- NavigateWithSignsUseCase.kt

#### Android Data (4)
- FlaskYoloApiService.kt
- SignDetectionResponseDto.kt
- FlaskYoloMapper.kt
- SignNavigationRepositoryImpl.kt

#### Android Presentation (4)
- SignNavigationContract.kt
- SignNavigationViewModel.kt
- SignNavigationScreen.kt
- TextToSpeechManager.kt

#### Configuration (2)
- LICENSE
- .gitignore (racine)

---

### Fichiers Modifiés (4)

#### Android (4)
1. **data/di/DataModule.kt** (ligne 26)
   - Ajout : Flask Retrofit configuration
   - Ajout : FLASK_BASE_URL constant
   
2. **presentation/navigation/Screen.kt**
   - Ajout : SignNavigation route object
   
3. **presentation/navigation/NavGraph.kt**
   - Ajout : SignNavigation composable
   - Ajout : onNavigateToSignNavigation parameter
   
4. **presentation/screens/home/HomeScreen.kt**
   - Ajout : FeatureCard "Navigation par Panneaux (YOLO)"
   - Ajout : onNavigateToSignNavigation callback

---

## 🎯 Fichiers Importants à Connaître

### Pour Démarrer (3 fichiers)
1. **START_HERE.md** - Guide ultra-rapide
2. **flask_server/install.bat** - Installation serveur
3. **data/di/DataModule.kt** (ligne 26) - Configuration IP

### Pour Développer (5 fichiers)
1. **flask_server/app.py** - API Flask
2. **domain/usecase/NavigateWithSignsUseCase.kt** - Business logic
3. **presentation/screens/signnavigation/SignNavigationViewModel.kt** - ViewModel
4. **presentation/screens/signnavigation/SignNavigationScreen.kt** - UI
5. **data/repository/SignNavigationRepositoryImpl.kt** - Repository

### Pour Publier GitHub (4 fichiers)
1. **GITHUB_SETUP.md** - Guide publication
2. **.gitignore** - Exclusions
3. **LICENSE** - Licence MIT
4. **CONTRIBUTING.md** - Guide contribution

---

## 🔍 Comment Trouver un Fichier ?

### Par Fonctionnalité

**YOLO Detection** :
- Backend : `flask_server/app.py` (lignes 50-150)
- Android : `domain/usecase/NavigateWithSignsUseCase.kt`

**Gemini Integration** :
- Backend : `flask_server/app.py` (lignes 150-200)
- Config : `flask_server/app.py` (ligne 16)

**Text-to-Speech** :
- Service : `presentation/util/TextToSpeechManager.kt`
- Usage : `presentation/screens/signnavigation/SignNavigationViewModel.kt`

**Navigation** :
- Routes : `presentation/navigation/Screen.kt`
- NavGraph : `presentation/navigation/NavGraph.kt`

**UI Screen** :
- Composable : `presentation/screens/signnavigation/SignNavigationScreen.kt`
- Contract : `presentation/screens/signnavigation/SignNavigationContract.kt`

### Par Technologie

**Flask/Python** :
```
flask_server/
  ├── app.py
  ├── requirements.txt
  └── test_api.py
```

**Retrofit/API** :
```
data/
  ├── remote/api/FlaskYoloApiService.kt
  └── remote/dto/SignDetectionResponseDto.kt
```

**Jetpack Compose** :
```
presentation/screens/signnavigation/
  └── SignNavigationScreen.kt
```

**Dependency Injection** :
```
data/di/DataModule.kt
```

---

## 📱 Points d'Entrée

### Pour Utilisateur
1. Ouvrir app Android
2. Home Screen → Tap "Navigation par Panneaux (YOLO)"
3. SignNavigationScreen s'affiche

### Pour Développeur Android
1. Entry point : `HomeScreen.kt` (ligne ~80)
2. Navigation : `NavGraph.kt` (ligne ~60)
3. Screen : `SignNavigationScreen.kt`
4. ViewModel : `SignNavigationViewModel.kt`

### Pour Développeur Backend
1. Entry point : `flask_server/app.py`
2. Route principale : `/detect-signs` (ligne 50)
3. YOLO : Fonction `detect_signs()` (ligne 80)
4. Gemini : Fonction `get_navigation_from_gemini()` (ligne 150)

---

## ✅ Checklist Utilisation

### Avant Premier Lancement
- [ ] Copier `bestLichir (1).pt` → `flask_server/`
- [ ] Run `flask_server/install.bat`
- [ ] Trouver IP locale (`ipconfig`)
- [ ] Modifier `data/di/DataModule.kt` ligne 26
- [ ] Run `flask_server/start_server.bat`
- [ ] Android Studio : Sync Gradle
- [ ] Android Studio : Build & Run

### Fichiers à Modifier
1. **data/di/DataModule.kt** (ligne 26) : Votre IP
2. **flask_server/app.py** (ligne 16) : Clé API Gemini (optionnel)

### Fichiers à Copier
1. **bestLichir (1).pt** : Racine → `flask_server/`

---

<div align="center">

**🌳 Arborescence Complète Disponible**

_46 fichiers • 32 créés • 4 modifiés_  
_Documentation exhaustive • Code production-ready_

**👉 [START_HERE.md](START_HERE.md) pour commencer !**

</div>

---

_Document généré le 07 Janvier 2026_
