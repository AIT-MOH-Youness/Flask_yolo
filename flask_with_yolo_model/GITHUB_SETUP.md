# 🌐 Publication GitHub - Guide Complet

> Comment publier votre projet "Guide de Gare" sur GitHub

---

## 📋 Table des Matières

- [Prérequis](#prérequis)
- [Préparation](#préparation)
- [Création Dépôt GitHub](#création-dépôt-github)
- [Publication](#publication)
- [Configuration](#configuration)
- [Checklist Sécurité](#checklist-sécurité)

---

## ✅ Prérequis

- Compte GitHub : https://github.com/join
- Git installé : https://git-scm.com/download/win
- PowerShell ou Git Bash

**Vérifier Git installé** :
```powershell
git --version
```

---

## 🎯 Préparation

### 1. Déplacer le Modèle YOLO

Le modèle `bestLichir (1).pt` (6 MB) **ne doit PAS** être sur GitHub (fichier trop volumineux).

```powershell
# Créer dossier local pour sauvegarder le modèle
mkdir C:\ModelesYOLO
move "bestLichir (1).pt" C:\ModelesYOLO\
move "bestLichir (1).onnx" C:\ModelesYOLO\
```

✅ Le `.gitignore` est configuré pour exclure les fichiers `*.pt` et `*.onnx`.

---

### 2. Vérifier les Clés API

**IMPORTANT** : Ne jamais publier votre clé API Gemini !

#### Option A : Utiliser Variable d'Environnement (Recommandé)

**Modifier `flask_server/app.py`** ligne 16 :
```python
# AVANT (dangereux)
gemini_api_key = "AIzaSyCEc9m1T5VMKHzwQxjbdmUiIdJDqT6ALsg"

# APRÈS (sécurisé)
import os
gemini_api_key = os.getenv("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
```

Puis créer fichier `.env` (ignoré par Git) :
```bash
echo GEMINI_API_KEY=AIzaSyCEc9m1T5VMKHzwQxjbdmUiIdJDqT6ALsg > flask_server/.env
```

Ajouter dans `.gitignore` :
```
flask_server/.env
```

#### Option B : Supprimer la Clé (Simplest)

**Modifier `flask_server/app.py`** ligne 16 :
```python
gemini_api_key = "VOTRE_CLE_API_GEMINI"
```

Les utilisateurs devront la remplacer.

---

## 🚀 Création Dépôt GitHub

### Via GitHub Website (Plus Simple)

1. **Aller sur** : https://github.com/new
2. **Remplir** :
   - Repository name : `guide-de-gare-yolo`
   - Description : `Application Android d'assistance pour personnes malvoyantes avec détection YOLO`
   - Visibility : **Public** ou Private
   - ✅ **NE PAS** cocher "Add a README" (on a déjà le nôtre)
3. **Cliquer** : "Create repository"

---

## 📤 Publication

### 1. Initialiser Git Local

```powershell
cd C:\Users\DELL\Desktop\PILS-07-01-2026

# Initialiser repo
git init

# Ajouter tous les fichiers (sauf exclusions .gitignore)
git add .

# Vérifier ce qui sera publié
git status
```

Vous devriez voir :
```
✅ CHANGELOG.md
✅ INDEX.md
✅ README.md
✅ START_HERE.md
✅ VISUAL_GUIDE.md
✅ flask_server/ (sans venv/ ni __pycache__)
✅ pils_mobile/ (sans build/ ni .gradle/)
❌ bestLichir (1).pt (exclu par .gitignore)
```

### 2. Premier Commit

```powershell
# Configurer identité Git (si première fois)
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"

# Créer commit
git commit -m "🎉 Version 2.0 - YOLO Integration Complete"
```

### 3. Lier avec GitHub

**Remplacer `VOTRE-USERNAME`** par votre nom d'utilisateur GitHub :

```powershell
git remote add origin https://github.com/VOTRE-USERNAME/guide-de-gare-yolo.git
```

### 4. Pousser vers GitHub

```powershell
# Renommer branche en "main" (standard GitHub)
git branch -M main

# Pousser vers GitHub
git push -u origin main
```

**Entrer** :
- Username GitHub
- Personal Access Token (voir section suivante)

---

## 🔑 Personal Access Token

GitHub n'accepte plus les mots de passe. Vous devez créer un **Personal Access Token**.

### Création Token

1. **Aller sur** : https://github.com/settings/tokens
2. **Cliquer** : "Generate new token" → "Generate new token (classic)"
3. **Configurer** :
   - Note : `PILS Upload`
   - Expiration : `90 days`
   - Scopes : ✅ `repo` (cocher toutes les sous-cases)
4. **Cliquer** : "Generate token"
5. **COPIER** le token (vous ne le reverrez plus !)

Exemple : `ghp_16C7e42F292c6912E7710c838347Ae178B4a`

### Utilisation

Lors du `git push`, entrer :
- **Username** : votre nom d'utilisateur GitHub
- **Password** : COLLER le token (pas votre mot de passe)

---

## 📝 Configuration README GitHub

GitHub affichera automatiquement le [README.md](README.md) à la racine.

### Badges Dynamiques

Notre README inclut déjà :
```markdown
[![Status](https://img.shields.io/badge/status-production_ready-green)]()
[![Version](https://img.shields.io/badge/version-2.0-blue)]()
```

Personnalisables sur : https://shields.io/

---

## 🔒 Checklist Sécurité

Avant publication, vérifier :

- [ ] ✅ Modèle YOLO `bestLichir (1).pt` déplacé (pas sur GitHub)
- [ ] ✅ Clé API Gemini protégée (variable d'environnement ou placeholder)
- [ ] ✅ `.gitignore` vérifié (pas de `venv/`, `__pycache__/`, `build/`)
- [ ] ✅ `local.properties` Android exclu (contient paths locaux)
- [ ] ✅ Aucun mot de passe dans le code
- [ ] ✅ README documenté et clair

---

## 🌐 Après Publication

### URL de Votre Projet

```
https://github.com/VOTRE-USERNAME/guide-de-gare-yolo
```

### Partager

- Direct link : URL ci-dessus
- Clone command : 
  ```bash
  git clone https://github.com/VOTRE-USERNAME/guide-de-gare-yolo.git
  ```

### Mettre à Jour

```powershell
# Après modifications locales
git add .
git commit -m "Description des changements"
git push
```

---

## 📦 Instructions Post-Clone (Pour Utilisateurs)

Ajouter dans README.md section "Installation" :

```markdown
## Installation Depuis GitHub

### 1. Cloner le Projet
git clone https://github.com/VOTRE-USERNAME/guide-de-gare-yolo.git
cd guide-de-gare-yolo

### 2. Télécharger le Modèle YOLO
Le modèle `bestLichir (1).pt` n'est pas inclus (trop volumineux).
- Télécharger depuis : [LIEN GOOGLE DRIVE / DROPBOX]
- Copier dans : `flask_server/bestLichir (1).pt`

### 3. Configurer Clé API Gemini
Créer `flask_server/.env`:
GEMINI_API_KEY=votre_clé_api_ici

### 4. Lancer
cd flask_server
install.bat
start_server.bat
```

---

## 📊 Statistiques GitHub

Après publication, GitHub affichera automatiquement :
- 📊 Nombre de lignes de code
- 📈 Langages utilisés (Kotlin, Python, Java)
- 🌟 Stars / Forks
- 📅 Dernière mise à jour

---

## 🎯 Optimisations GitHub

### README Attractif

Notre [README.md](README.md) inclut :
- ✅ Badges de statut
- ✅ Emojis visuels
- ✅ Quick links
- ✅ Architecture diagram (ASCII)
- ✅ Installation rapide

### Topics GitHub

Ajouter topics (tags) sur GitHub :
```
android, kotlin, yolo, gemini-ai, flask, 
computer-vision, accessibility, text-to-speech, 
mvi-architecture, jetpack-compose
```

**Comment ajouter** :
1. Aller sur votre dépôt GitHub
2. Section "About" (en haut à droite) → ⚙️
3. Ajouter topics
4. Save

### GitHub Pages (Optionnel)

Publier documentation en site web :
1. Settings → Pages
2. Source : `main` branch, `/docs` folder
3. Save

URL : `https://VOTRE-USERNAME.github.io/guide-de-gare-yolo/`

---

## 🐛 Problèmes Courants

### Erreur : "Permission denied"

```powershell
# Vérifier remote
git remote -v

# Si mauvaise URL, remplacer
git remote remove origin
git remote add origin https://github.com/VOTRE-USERNAME/guide-de-gare-yolo.git
```

### Erreur : "Large files"

GitHub limite : 100 MB / fichier, 1 GB / dépôt.

**Solution** : Modèle YOLO (6 MB) doit être exclu. Vérifier `.gitignore` :
```
*.pt
*.onnx
```

### Erreur : "Authentication failed"

Utiliser **Personal Access Token**, pas le mot de passe GitHub.

---

## 📚 Ressources

- **Git Documentation** : https://git-scm.com/doc
- **GitHub Guides** : https://guides.github.com/
- **Shields.io (Badges)** : https://shields.io/
- **Markdown Guide** : https://www.markdownguide.org/

---

## ✅ Checklist Finale

Avant de cliquer "Publish" :

- [ ] Git installé (`git --version`)
- [ ] Compte GitHub créé
- [ ] Modèle YOLO sauvegardé localement (pas sur GitHub)
- [ ] Clé API Gemini protégée
- [ ] `.gitignore` vérifié
- [ ] `git add .` exécuté
- [ ] `git commit -m "..."` créé
- [ ] Remote GitHub configuré
- [ ] Personal Access Token généré
- [ ] README attractif vérifié
- [ ] Prêt à `git push` 🚀

---

<div align="center">

**🌐 Prêt pour GitHub !**

_Une fois publié, votre projet sera visible par le monde entier_  
_Documentation complète • Architecture claire • Code propre_

</div>
