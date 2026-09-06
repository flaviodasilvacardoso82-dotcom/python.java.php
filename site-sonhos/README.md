# Fragmentos de Sonhos

Site interativo feito com Flask e Vue 3.

## 1. Abrir a pasta no terminal

No PowerShell, a partir da pasta do projeto:

```powershell
cd ".\site-sonhos"
```

## 2. Criar o ambiente virtual

O ambiente virtual deixa as dependências deste site separadas dos outros projetos Python:

```powershell
py -3 -m venv .venv
```

Se o comando `py` não existir, use o caminho do Python instalado:

```powershell
& "C:\Users\tarug\AppData\Local\Python\pythoncore-3.14-64\python.exe" -m venv .venv
```

## 3. Ativar o ambiente virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação, execute uma vez:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Depois, ative novamente. O terminal deverá mostrar `(.venv)` no início da linha.

## 4. Instalar as dependências

```powershell
python -m pip install -r requirements.txt
```

## 5. Iniciar o site

```powershell
python app.py
```

Abra no navegador: <http://127.0.0.1:5000>

Para parar o servidor, pressione `Ctrl+C` no terminal.

## Estrutura

```text
site-sonhos/
├── app.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

## Sobre o Google e a publicação

`127.0.0.1:5000` funciona somente no seu computador. Ele serve para testar o site localmente, mas não deixa o site público nem faz com que ele apareça no Google.

Para publicar, é necessário colocar o projeto em um serviço de hospedagem que execute Python/Flask, como Render, PythonAnywhere ou Railway. Depois de obter uma URL pública, o Google pode encontrar o site com o tempo. Para acelerar a indexação, normalmente também se cadastra a URL no Google Search Console.

Nunca coloque senhas ou chaves secretas no código ou no repositório público.
