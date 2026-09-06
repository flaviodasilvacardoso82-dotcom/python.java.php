#!/bin/bash
# Script para criar ambiente virtual e instalar dependências em macOS/Linux

echo "============================================"
echo "Criando Ambiente Virtual..."
echo "============================================"
python3 -m venv venv

echo ""
echo "============================================"
echo "Ativando Ambiente Virtual..."
echo "============================================"
source venv/bin/activate

echo ""
echo "============================================"
echo "Instalando Dependências..."
echo "============================================"
pip install -r requirements.txt

echo ""
echo "============================================"
echo "✓ Pronto! Seu ambiente está configurado!"
echo "============================================"
echo ""
echo "Para ativar o ambiente virtual depois, use:"
echo "  source venv/bin/activate"
echo ""
echo "Para rodar o servidor Flask, use:"
echo "  python app.py"
echo ""
