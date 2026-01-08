# 🤝 Contribuer au Projet Guide de Gare

Merci de votre intérêt pour contribuer ! Ce projet aide les personnes malvoyantes à naviguer dans les gares.

---

## 📋 Comment Contribuer

### 1. 🐛 Signaler un Bug

Créer une **Issue** sur GitHub avec :
- **Titre clair** : "Bug: [Description courte]"
- **Description** :
  - Système : Android 12, Python 3.9, etc.
  - Étapes pour reproduire
  - Comportement attendu vs réel
  - Captures d'écran / logs

**Template** :
```markdown
### Environnement
- OS : Windows 11
- Python : 3.9
- Android : API 33

### Étapes
1. Lancer Flask
2. Taper photo
3. Erreur : Connection Refused

### Logs
[Coller logs Flask + Android Logcat]
```

---

### 2. 💡 Proposer une Amélioration

Créer une **Issue** avec :
- **Titre** : "Feature: [Description]"
- **Motivation** : Pourquoi cette feature ?
- **Proposition** : Comment l'implémenter ?

**Exemple** :
```markdown
### Feature Proposée
Support hors ligne avec TFLite

### Motivation
Utilisation sans WiFi dans gares

### Implémentation
- Convertir YOLO .pt → .tflite
- Intégrer TensorFlow Lite Android
- Cache Gemini responses
```

---

### 3. 🔧 Soumettre un Pull Request

#### A. Fork & Clone

```bash
# 1. Forker le dépôt sur GitHub (bouton "Fork")

# 2. Cloner votre fork
git clone https://github.com/VOTRE-USERNAME/guide-de-gare-yolo.git
cd guide-de-gare-yolo

# 3. Ajouter remote upstream
git remote add upstream https://github.com/AUTEUR-ORIGINAL/guide-de-gare-yolo.git
```

#### B. Créer une Branche

```bash
# Toujours partir de main à jour
git checkout main
git pull upstream main

# Créer branche descriptive
git checkout -b feature/support-offline-mode
# ou
git checkout -b fix/tts-crash-android-12
```

#### C. Développer

**Respecter l'architecture** :
```
pils_mobile/
  domain/      # Business Logic (pas de dépendances Android/Framework)
  data/        # Repositories, API, DTOs
  presentation/ # UI, ViewModels, MVI
```

**Conventions de code** :
- Kotlin : [Kotlin Coding Conventions](https://kotlinlang.org/docs/coding-conventions.html)
- Python : [PEP 8](https://pep8.org/)

**Tests** :
```bash
# Android
cd pils_mobile
./gradlew test

# Flask
cd flask_server
pytest test_api.py
```

#### D. Commit

```bash
# Commits atomiques et clairs
git add domain/src/main/java/com/insa/foodies/domain/model/OfflineCache.kt
git commit -m "feat(domain): Add offline cache model"

git add presentation/src/main/java/com/insa/foodies/presentation/screens/SignNavigationScreen.kt
git commit -m "fix(ui): Fix TTS crash on Android 12"
```

**Conventions Commits** :
- `feat(scope): Description` - Nouvelle feature
- `fix(scope): Description` - Bug fix
- `refactor(scope): Description` - Refactoring
- `docs: Description` - Documentation
- `test(scope): Description` - Tests

**Scopes** : `domain`, `data`, `presentation`, `flask`, `docs`

#### E. Push & Pull Request

```bash
# Push vers votre fork
git push origin feature/support-offline-mode

# 1. Aller sur GitHub → votre fork
# 2. Bouton "Compare & pull request"
# 3. Remplir template PR :
```

**Template Pull Request** :
```markdown
### Description
Implémente support hors ligne avec TFLite

### Type de Changement
- [x] Feature
- [ ] Bug Fix
- [ ] Refactoring
- [ ] Documentation

### Checklist
- [x] Tests passent (`./gradlew test`)
- [x] Documentation mise à jour
- [x] Code respecte conventions
- [x] Pas de conflits avec main

### Captures d'écran
[Si UI/UX changes]

### Tests Effectués
- [x] Android API 33 (Pixel 5)
- [x] Android API 26 (émulateur)
- [x] Mode hors ligne
```

---

## 🎯 Priorités Actuelles

### High Priority
- [ ] Support TFLite (mode hors ligne)
- [ ] Tests unitaires domain/data layers
- [ ] Historique détections avec Room DB
- [ ] Support multilingue (EN, AR, ES)

### Medium Priority
- [ ] Amélioration UI/UX (Material 3)
- [ ] Mode sombre
- [ ] Statistiques utilisateur
- [ ] Export résultats (PDF/CSV)

### Low Priority
- [ ] Widget Android
- [ ] Wear OS support
- [ ] CI/CD GitHub Actions

**Voir** : [Issues GitHub](https://github.com/AUTEUR-ORIGINAL/guide-de-gare-yolo/issues)

---

## 🏗️ Architecture

### Clean Architecture

```
domain/       # Business Logic (entities, use cases, repositories interfaces)
  ├── model/  # Entities
  ├── repository/  # Interfaces
  └── usecase/     # Business Logic

data/         # Implementation
  ├── remote/      # API Services, DTOs
  ├── local/       # Room DB (futur)
  ├── mapper/      # DTO ↔ Domain
  └── repository/  # Implementation

presentation/ # UI
  ├── screens/     # Composables
  ├── viewmodel/   # MVI ViewModels
  └── navigation/  # Nav Graph
```

### MVI Pattern

```kotlin
Contract.kt
  ├── State      # UI State immutable
  ├── Event      # User actions
  └── Effect     # One-time events (navigation, toasts)

ViewModel.kt
  ├── _state: MutableState<State>
  ├── onEvent(Event)
  └── setEffect(Effect)

Screen.kt (Composable)
  ├── LaunchedEffect { collectEffect() }
  ├── when (state) { ... }
  └── viewModel.onEvent(Event.OnClick)
```

---

## 📚 Resources

### Documentation
- [Kotlin Docs](https://kotlinlang.org/docs/)
- [Jetpack Compose](https://developer.android.com/jetpack/compose)
- [Flask Docs](https://flask.palletsprojects.com/)
- [Ultralytics YOLO](https://docs.ultralytics.com/)

### Guides Projet
- [ARCHITECTURE_MVI_GUIDE.md](pils_mobile/ARCHITECTURE_MVI_GUIDE.md)
- [SIGN_NAVIGATION_GUIDE.md](pils_mobile/SIGN_NAVIGATION_GUIDE.md)
- [README_YOLO_INTEGRATION.md](README_YOLO_INTEGRATION.md)

---

## 🧪 Tests

### Android (Kotlin)

```kotlin
// domain/src/test/java/com/insa/foodies/domain/usecase/NavigateWithSignsUseCaseTest.kt
@Test
fun `GIVEN image with signs WHEN invoke THEN returns success`() = runTest {
    // Arrange
    val mockRepo = mockk<SignNavigationRepository>()
    coEvery { mockRepo.detectSignsAndNavigate(any()) } returns Result.success(mockResult)
    val useCase = NavigateWithSignsUseCase(mockRepo)
    
    // Act
    val result = useCase(ImageSource.Gallery(mockUri))
    
    // Assert
    assertTrue(result.isSuccess)
}
```

### Flask (Python)

```python
# flask_server/test_api.py
def test_detect_signs_with_image():
    with open('test_image.jpg', 'rb') as f:
        response = client.post('/detect-signs', 
            data={'image': (f, 'test.jpg')},
            content_type='multipart/form-data'
        )
    assert response.status_code == 200
    assert response.json['success'] == True
```

---

## 🔒 Sécurité

### NE JAMAIS committer :
- ❌ Clés API (`GEMINI_API_KEY`)
- ❌ Modèles YOLO (`*.pt`, `*.onnx`)
- ❌ `local.properties` Android
- ❌ Dossiers `venv/`, `build/`, `__pycache__/`

**Vérifier avant commit** :
```bash
git status
# ✅ Aucun fichier sensible dans "Changes to be committed"
```

---

## 💬 Communication

### Channels
- **Issues GitHub** : Bugs, features, questions
- **Pull Requests** : Code reviews, discussions
- **Discussions GitHub** : Questions générales

### Délais de Réponse
- Issues : ~48h
- Pull Requests : ~72h (review)
- Questions : ~24h

---

## 🎓 Premier Contribution ?

Bienvenue ! Suivez ce workflow :

1. ⭐ **Star** le projet (encouragement !)
2. 🍴 **Fork** le dépôt
3. 📚 Lire [VISUAL_GUIDE.md](VISUAL_GUIDE.md) + [ARCHITECTURE_MVI_GUIDE.md](pils_mobile/ARCHITECTURE_MVI_GUIDE.md)
4. 🔍 Chercher issue avec label `good first issue`
5. 💬 Commenter l'issue : "Je travaille dessus"
6. 🔧 Développer sur branche dédiée
7. ✅ Tests + Documentation
8. 🚀 Pull Request avec description claire

**Issues recommandées pour débuter** :
- Documentation improvements
- UI/UX enhancements
- Tests unitaires
- Traductions

---

## 🏆 Code of Conduct

### Nos Valeurs
- ❤️ Respect et bienveillance
- 🤝 Collaboration constructive
- 📚 Partage de connaissances
- 🌍 Accessibilité pour tous

### Comportements Attendus
- ✅ Feedback constructif et respectueux
- ✅ Considération pour perspectives diverses
- ✅ Focus sur l'impact utilisateur (personnes malvoyantes)
- ✅ Patience avec contributeurs débutants

### Comportements Inacceptables
- ❌ Langage offensant ou discriminatoire
- ❌ Harcèlement
- ❌ Spam ou trolling
- ❌ Publication informations privées

**Signalement** : [email@example.com] (modérateurs répondent en 24h)

---

## 📜 Licence

En contribuant, vous acceptez que votre code soit sous la même licence que le projet.

---

## ✅ Checklist Avant Pull Request

- [ ] Code respecte conventions Kotlin/Python
- [ ] Tests ajoutés/modifiés passent (`./gradlew test`, `pytest`)
- [ ] Documentation mise à jour (README, guides)
- [ ] Pas de fichiers sensibles (clés API, modèles)
- [ ] Commits clairs et atomiques (`feat:`, `fix:`)
- [ ] Pull Request description complète
- [ ] Branche à jour avec `upstream/main`
- [ ] Pas de conflits

---

## 🙏 Merci !

Chaque contribution, petite ou grande, rend ce projet plus accessible aux personnes malvoyantes. Merci de votre aide ! 🎉

---

<div align="center">

**Questions ?** Ouvrez une [Issue GitHub](https://github.com/AUTEUR-ORIGINAL/guide-de-gare-yolo/issues) !

_Guide mis à jour le 07 Janvier 2026_

</div>
