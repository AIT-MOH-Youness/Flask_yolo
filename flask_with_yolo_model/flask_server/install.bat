@echo off
echo ========================================
echo  Installation Flask Server
echo ========================================
echo.

REM Créer l'environnement virtuel
echo [1/4] Creation de l'environnement virtuel...
python -m venv venv
if errorlevel 1 (
    echo Erreur: Python n'est pas installe ou introuvable
    pause
    exit /b 1
)

REM Activer l'environnement virtuel
echo [2/4] Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

REM Installer les dépendances
echo [3/4] Installation des dependances...
pip install -r requirements.txt
if errorlevel 1 (
    echo Erreur lors de l'installation des dependances
    pause
    exit /b 1
)

REM Vérifier le modèle YOLO
echo [4/4] Verification du modele YOLO...
if exist "bestLichir (1).pt" (
    echo Modele YOLO trouve!
) else (
    echo.
    echo ATTENTION: Le modele YOLO n'est pas trouve!
    echo Copiez le fichier "bestLichir (1).pt" dans ce dossier
    echo.
)

echo.
echo ========================================
echo  Installation terminee!
echo ========================================
echo.
echo Pour lancer le serveur:
echo   1. Activez l'environnement: venv\Scripts\activate
echo   2. Lancez le serveur: python app.py
echo.
pause
