# Jogo da Velha - Site com Flask

Projeto web do seu jogo da velha em Python!

## 📁 Estrutura do Projeto

```
meu_site_velha/
├── app.py                 # Aplicação Flask principal
├── requirements.txt       # Dependências do projeto
├── .gitignore            # Arquivos a ignorar no Git
├── venv/                 # Ambiente virtual (será criado)
└── templates/
    └── index.html        # Página principal com o jogo
```

## 🚀 Como Rodar

### 1. Criar o Ambiente Virtual

```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```

### 2. Ativar o Ambiente Virtual

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

Quando ativo, o terminal mostrará `(venv)` na frente.

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar a Aplicação

```bash
python app.py
```

Pronto! Abra seu navegador e vá para:
```
http://localhost:5000
```

## 🎮 Como Jogar

- Clique nas casas para jogar
- X joga primeiro
- Ganha quem fizer 3 em linha (horizontal, vertical ou diagonal)
- Clique em "Reiniciar Jogo" para começar nova partida

## 📝 Notas

- O Flask roda em modo `debug=True`, então qualquer mudança em `app.py` reinicia automaticamente
- Para parar o servidor, pressione `Ctrl+C` no terminal
- Para desativar o ambiente virtual, digite `deactivate`

Bom jogo! 🎉
