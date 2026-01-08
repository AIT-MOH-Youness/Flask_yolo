@echo off
echo ========================================
echo  Demarrage du Serveur Flask
echo ========================================
echo.

REM Vérifier si l'environnement virtuel existe
if not exist "venv\" (
    echo Erreur: L'environnement virtuel n'existe pas
    echo Executez d'abord: install.bat
    pause
    exit /b 1
)

REM Vérifier le modèle YOLO
if not exist "bestLichir (1).pt" (
    echo.
    echo ERREUR: Le modele YOLO n'est pas trouve!
    echo Copiez "bestLichir (1).pt" dans ce dossier
    echo.
    pause
    exit /b 1
)

REM Activer l'environnement et lancer le serveur
call venv\Scripts\activate.bat

echo.
echo Lancement du serveur Flask...
echo Appuyez sur Ctrl+C pour arreter le serveur
echo.

python app.py

pause
