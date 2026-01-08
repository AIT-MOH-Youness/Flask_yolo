# ⚡ DÉMARRAGE EXPRESS - 3 ÉTAPES

## 🎯 Configuration en 8 Minutes

### 1️⃣ SERVEUR (3 minutes)

```cmd
# Copier le modèle
copy "bestLichir (1).pt" flask_server\

# Aller dans le dossier
cd flask_server

# Double-clic sur ces fichiers (dans l'ordre)
install.bat      ← Attendez "Installation terminée"
start_server.bat ← Laissez la fenêtre ouverte
```

**✅ Prêt quand vous voyez** :
```
🎯 YOLO Model: Loaded
* Running on http://0.0.0.0:5000
```

---

### 2️⃣ IP + ANDROID (3 minutes)

```powershell
# Trouver votre IP
ipconfig
# Notez : 192.168.X.X
```

**Ouvrir** : `pils_mobile\data\src\main\java\com\insa\foodies\data\di\DataModule.kt`

**Ligne 26** - Remplacer par votre IP :
```kotlin
private const val FLASK_BASE_URL = "http://192.168.X.X:5000/"
```

**Sauvegarder** : `Ctrl + S`

---

### 3️⃣ BUILD & TEST (2 minutes)

**Android Studio** :
- Clic 🐘 (Sync)
- Clic ▶️ (Run)

**Dans l'app** :
- "Navigation par Panneaux"
- Prendre/Choisir photo
- ✅ Résultats + Audio 🔊

---

## 🆘 Problème ?

### Serveur pas accessible
```powershell
# Vérifier
curl http://192.168.X.X:5000/health

# Si erreur : vérifier IP et serveur lancé
```

### YOLO not found
```cmd
# Le fichier doit être ici
dir flask_server\bestLichir*.pt
```

---

## 📚 Documentation Complète

- **👉 [INDEX.md](INDEX.md)** ← Tous les guides
- **🚀 [IMPLEMENTATION_COMPLETE.md](IMPLEMENTATION_COMPLETE.md)** ← Résumé complet
- **🖼️ [VISUAL_GUIDE.md](VISUAL_GUIDE.md)** ← Avec images

---

**⏱️ Total : 8 minutes | Status : ✅ Prêt à l'emploi**
