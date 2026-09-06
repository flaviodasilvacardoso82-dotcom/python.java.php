@echo off
REM Script para criar ambiente virtual e instalar dependências no Windows

echo ============================================
echo Criando Ambiente Virtual...
echo ============================================
python -m venv venv

echo.
echo ============================================
echo Ativando Ambiente Virtual...
echo ============================================
call venv\Scripts\activate.bat

echo.
echo ============================================
echo Instalando Dependências...
echo ============================================
pip install -r requirements.txt

echo.
echo ============================================
echo ✓ Pronto! Seu ambiente está configurado!
echo ============================================
echo.
echo Para ativar o ambiente virtual depois, use:
echo   venv\Scripts\activate.bat
echo.
echo Para rodar o servidor Flask, use:
echo   python app.py
echo.
pause
