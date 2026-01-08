# 🚀 Démarrage Rapide - Navigation par Panneaux YOLO

## ⚡ Configuration en 5 Minutes

### 📋 Prérequis
- ✅ Python 3.8+ installé
- ✅ Android Studio installé
- ✅ PC et téléphone sur le même WiFi

---

## 🎯 Étape 1 : Serveur Flask (5 min)

### Option A : Automatique (Windows)

```cmd
# 1. Ouvrir PowerShell dans flask_server
cd C:\Users\DELL\Desktop\PILS-07-01-2026\flask_server

# 2. Double-cliquer sur: install.bat
# Cela va créer l'environnement virtuel et installer les dépendances

# 3. Copier le modèle YOLO
copy "C:\Users\DELL\Desktop\PILS-07-01-2026\bestLichir (1).pt" .

# 4. Double-cliquer sur: start_server.bat
# Le serveur démarre automatiquement!
```

### Option B : Manuel

```bash
cd flask_server
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

**✅ Serveur prêt quand vous voyez** :
```
🚀 Flask Server Starting...
🎯 YOLO Model: Loaded
🤖 Gemini AI: Configured
* Running on http://0.0.0.0:5000
```

---

## 🌐 Étape 2 : Trouver votre IP (30 sec)

```powershell
ipconfig
```

Cherchez **"IPv4 Address"** (exemple: `192.168.1.100`)

---

## 📱 Étape 3 : Configuration Android (2 min)

### 3.1 Modifier l'URL

**Fichier** : `pils_mobile/data/src/main/java/com/insa/foodies/data/di/DataModule.kt`

**Ligne 26** :
```kotlin
private const val FLASK_BASE_URL = "http://192.168.1.100:5000/"
//                                         ^^^^^^^^^^^^^^
//                                    Remplacez par VOTRE IP
```

### 3.2 Build & Run

1. Ouvrir Android Studio
2. **Sync Gradle** (🐘)
3. **Run** (▶️)

---

## 🧪 Étape 4 : Test (1 min)

### Test Rapide du Serveur

```powershell
# Dans un nouveau PowerShell
cd flask_server
python test_api.py
```

Ou via curl :
```powershell
curl http://192.168.1.100:5000/health
```

### Test dans l'App

1. Ouvrir l'app sur votre téléphone
2. Cliquer **"Navigation par Panneaux (YOLO)"**
3. Prendre photo d'un panneau
4. 🎉 Résultats + Audio automatique!

---

## ✅ Checklist Complète

### Serveur Flask
- [ ] Python installé
- [ ] `install.bat` exécuté
- [ ] Modèle `bestLichir (1).pt` copié dans `flask_server/`
- [ ] Serveur lancé avec `start_server.bat`
- [ ] Message "YOLO Model: Loaded" visible

### Android
- [ ] IP correcte dans `DataModule.kt` (ligne 26)
- [ ] Gradle synchronisé
- [ ] App compilée sans erreur
- [ ] Téléphone sur le même WiFi que le PC

### Test
- [ ] `/health` retourne `{"status": "healthy"}`
- [ ] App se connecte au serveur
- [ ] Photo prise et analysée
- [ ] Résultats affichés
- [ ] Audio fonctionne

---

## 🐛 Problèmes Courants

### "Connection refused" dans l'app

**Solutions** :
1. Vérifier que le serveur Flask est lancé
2. Vérifier l'IP dans `DataModule.kt`
3. PC et téléphone sur le même WiFi
4. Désactiver pare-feu temporairement :
```powershell
netsh advfirewall set allprofiles state off
```

### "YOLO Model not found"

**Solution** :
```cmd
copy "C:\Users\DELL\Desktop\PILS-07-01-2026\bestLichir (1).pt" flask_server\
```

### Serveur très lent

**Normal** : Première requête prend 5-10s (chargement modèles)  
Les suivantes : 2-5s

---

## 📊 Résumé du Workflow

```
📱 App Android
    ↓
    📸 Prend photo
    ↓
    🌐 HTTP POST → Flask Server (192.168.x.x:5000)
    ↓
    🎯 YOLO détecte panneaux
    ↓
    ✂️  Crop chaque panneau
    ↓
    🤖 Gemini analyse chaque crop
    ↓
    📝 Instructions de navigation
    ↓
    ⬆️  Retour JSON à l'app
    ↓
    📱 Affichage + 🔊 Text-to-Speech
```

---

## 🎉 Prêt à Tester !

1. ✅ Double-cliquez sur `start_server.bat`
2. ✅ Mettez votre IP dans `DataModule.kt`
3. ✅ Lancez l'app Android
4. ✅ Prenez une photo de panneau
5. ✅ Écoutez les instructions vocales !

**Temps total : ~8 minutes** ⚡

---

## 📞 Support

Si problème, vérifiez dans l'ordre :
1. Serveur Flask lancé ? → Regardez la console
2. IP correcte ? → `ipconfig` + vérifier `DataModule.kt`
3. Même WiFi ? → Paramètres réseau
4. Pare-feu ? → Désactivez temporairement
5. Modèle YOLO ? → `dir flask_server\bestLichir*`
