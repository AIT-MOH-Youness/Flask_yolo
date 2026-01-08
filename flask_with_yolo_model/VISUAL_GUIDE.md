# 🎯 Configuration Rapide en Images

## 🖥️ Partie 1 : Serveur Flask

### Étape 1 : Copier le Modèle YOLO
```
📁 Source
C:\Users\DELL\Desktop\PILS-07-01-2026\bestLichir (1).pt

📁 Destination  
C:\Users\DELL\Desktop\PILS-07-01-2026\flask_server\bestLichir (1).pt
```

### Étape 2 : Installer et Lancer

**Double-cliquer sur** :
```
📄 flask_server\install.bat
```
Attendez "Installation terminée!"

**Puis double-cliquer sur** :
```
📄 flask_server\start_server.bat
```

**✅ Serveur prêt quand vous voyez** :
```
========================================
🚀 Flask Server Starting...
🎯 YOLO Model: Loaded
🤖 Gemini AI: Configured
========================================

* Running on http://0.0.0.0:5000
```

**⚠️ NE PAS FERMER CETTE FENÊTRE !**

---

## 🌐 Partie 2 : Trouver votre IP

### Ouvrir PowerShell

**Windows** : Touche Windows + X → "Windows PowerShell"

### Taper la commande
```powershell
ipconfig
```

### Chercher "IPv4 Address"
```
Carte réseau sans fil Wi-Fi:
   ...
   Adresse IPv4. . . . . . . . . . . . : 192.168.1.100
                                         ^^^^^^^^^^^^^^
                                      NOTEZ CETTE ADRESSE !
```

---

## 📱 Partie 3 : Configuration Android

### Étape 1 : Ouvrir le Fichier

**Chemin** :
```
pils_mobile\data\src\main\java\com\insa\foodies\data\di\DataModule.kt
```

### Étape 2 : Modifier la Ligne 26

**AVANT** :
```kotlin
private const val FLASK_BASE_URL = "http://192.168.1.100:5000/"
```

**APRÈS** (avec VOTRE IP) :
```kotlin
private const val FLASK_BASE_URL = "http://192.168.1.XXX:5000/"
                                           ^^^^^^^^^^^^^^
                                        Remplacez par votre IP
```

**Exemple** : Si votre IP est `192.168.43.217`
```kotlin
private const val FLASK_BASE_URL = "http://192.168.43.217:5000/"
```

### Étape 3 : Sauvegarder
**Ctrl + S**

---

## 🔧 Partie 4 : Build Android

### Dans Android Studio

1. **Sync Gradle**
```
Cliquer sur l'icône 🐘 (Sync Project with Gradle Files)
OU
Menu : File → Sync Project with Gradle Files
```
Attendez "Gradle sync finished"

2. **Build**
```
Menu : Build → Make Project
OU
Ctrl + F9
```
Attendez "Build successful"

3. **Run**
```
Cliquer sur ▶️ (Run 'app')
OU
Shift + F10
```

---

## 📱 Partie 5 : Test dans l'App

### Écran d'Accueil

Vous verrez 3 cartes :
1. ✅ Identifier les objets
2. ✅ Guider par les signes
3. 🆕 **Navigation par Panneaux (YOLO)** ← CLIQUER ICI !

### Écran Navigation

**Étape 1** : Cliquer "Choisir depuis la galerie"

**Étape 2** : Sélectionner une photo de panneau

**Étape 3** : Attendre l'analyse
```
⏳ Analyse en cours...
   Détection YOLO + Analyse Gemini
```

**Étape 4** : Résultats !
```
✅ 2 panneau(x) détecté(s)
   Temps de traitement: 3.5s

   📍 Panneau 1:
      Label: panneau_direction
      Confiance: 95%
      [À gauche] [Niveau yeux]
      
      🧭 Navigation:
      Gare SNCF: Tournez à gauche
      Métro: Continuez tout droit
      
      [🔊] ← Cliquer pour écouter
```

**Étape 5** : Audio automatique !
Le premier panneau est lu automatiquement 🔊

---

## ✅ Checklist Visuelle

### Avant de Tester

```
☐ Serveur Flask lancé (fenêtre console ouverte)
☐ Message "YOLO Model: Loaded" visible
☐ IP trouvée avec ipconfig
☐ IP modifiée dans DataModule.kt (ligne 26)
☐ Fichier sauvegardé (Ctrl+S)
☐ Gradle synchronisé (🐘)
☐ Build réussi (✅)
☐ PC et téléphone sur le MÊME WiFi
```

### Test Rapide

```
☐ App installée sur téléphone
☐ Écran "Navigation par Panneaux" ouvert
☐ Photo de panneau sélectionnée
☐ Message "Analyse en cours..." affiché
☐ Résultats affichés
☐ Audio entendu 🔊
```

---

## 🐛 Problèmes Courants - Solutions Visuelles

### ❌ "Connection refused"

**Vérifier** :
1. Fenêtre serveur Flask ouverte ?
   ```
   ✅ OUI → Passer au point 2
   ❌ NON → Lancer start_server.bat
   ```

2. IP correcte dans DataModule.kt ?
   ```
   Ouvrir le fichier
   Ligne 26 : http://192.168.X.X:5000/
              Correspond à votre ipconfig ?
   ```

3. Même WiFi ?
   ```
   PC : Paramètres → Réseau → WiFi
   📱 : Paramètres → WiFi
   Même nom de réseau ?
   ```

---

### ❌ "YOLO Model not found"

**Solution Visuelle** :
```
1. Ouvrir Explorateur Windows
2. Aller à : C:\Users\DELL\Desktop\PILS-07-01-2026\
3. Voir : bestLichir (1).pt (6 MB) ✅
4. Copier ce fichier
5. Aller à : flask_server\
6. Coller ici
7. Vérifier présence : flask_server\bestLichir (1).pt ✅
8. Relancer start_server.bat
```

---

### ❌ "Gradle sync failed"

**Solution** :
```
1. Android Studio
2. Menu : Build → Clean Project
3. Attendre fin
4. Menu : Build → Rebuild Project
5. Attendre fin
6. Cliquer 🐘 (Sync)
```

---

## 📸 Conseils pour Prendre des Photos

### ✅ Bonnes Photos
```
✓ Panneau visible et net
✓ Bon éclairage
✓ Distance : 1-3 mètres
✓ Panneau occupant 20-50% de l'image
✓ Pas de flou
```

### ❌ À Éviter
```
✗ Trop loin (panneau minuscule)
✗ Trop proche (panneau coupé)
✗ Sombre
✗ Flou
✗ Contre-jour
```

---

## 🎯 Ordre d'Exécution - Mémo Visuel

```
┌─────────────────────────────────────┐
│  1️⃣  COPIER MODÈLE YOLO             │
│     bestLichir (1).pt → flask_server│
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  2️⃣  INSTALLER FLASK                │
│     Double-clic: install.bat        │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  3️⃣  LANCER SERVEUR                 │
│     Double-clic: start_server.bat   │
│     NE PAS FERMER LA FENÊTRE !     │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  4️⃣  TROUVER IP                     │
│     PowerShell: ipconfig            │
│     Noter: 192.168.X.X             │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  5️⃣  MODIFIER ANDROID               │
│     DataModule.kt ligne 26          │
│     FLASK_BASE_URL = "http://IP:5000/"│
│     Ctrl+S pour sauvegarder        │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  6️⃣  SYNC GRADLE                    │
│     Clic 🐘 dans Android Studio     │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  7️⃣  RUN APP                        │
│     Clic ▶️  dans Android Studio    │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  8️⃣  TESTER                         │
│     Navigation par Panneaux → Photo │
│     Attendre résultats + Audio 🔊  │
└─────────────────────────────────────┘
```

---

## 🎉 Vous Avez Réussi Quand...

```
✅ Console Flask affiche :
   "🎯 YOLO Model: Loaded"
   "🤖 Gemini AI: Configured"
   "* Running on http://0.0.0.0:5000"

✅ Android Studio affiche :
   "Gradle sync finished"
   "Build successful"

✅ App Android affiche :
   "X panneau(x) détecté(s)"
   Cartes avec informations
   
✅ Audio fonctionne :
   🔊 Voix française lit les instructions
```

---

**🎊 Félicitations ! Votre système YOLO est opérationnel !**

Pour toute question, consultez :
- [QUICK_START.md](QUICK_START.md) - Guide rapide
- [CHANGELOG.md](CHANGELOG.md) - Liste complète des changements
- [README_YOLO_INTEGRATION.md](README_YOLO_INTEGRATION.md) - Vue d'ensemble
