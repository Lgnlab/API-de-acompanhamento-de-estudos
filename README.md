## 📋 API de acompanhamento de estudos

## 🚀 Funcionalidades

- cadastrar usuário;
- fazer login;
- cadastrar matérias;
- listar matérias;
- cadastrar uma sessão de estudo;
- listar sessões de estudo;
- marcar uma sessão como concluída;
- mostrar o total de horas estudadas por matéria.


## 🛠️ Tecnologias utilizadas

- Python 3
- FasAPI
- SQLite3
- SQLAlchemy
- Pydantic
- JWT (JSON Web Token)
- Passlib  
- python-jose
- python-dotenv
- Uvicorn
- Pytest
- Git e GitHub

## ⚙️ Como instalar dependências

1. Ative o ambiente virtual
-Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

-Se estiver no Prompt de Comando (CMD):

.venv\Scripts\activate.bat

-Você deverá ver algo como:

(.venv) PS C:\Users\Lucas\study-control-api>
2. Instale as dependências

pip install fastapi uvicorn sqlalchemy pydantic python-jose[cryptography] passlib[bcrypt] python-dotenv


## ⚙️ Como executar a aplicação

uvicorn app.main:app --reload


## 🎯 Objetivo do projeto

API de acompanhamento de estudos é uma API REST desenvolvida para auxiliar no gerenciamento dos estudos de um usuário.

O objetivo é permitir o cadastro de matérias, o registro de sessões de estudo e o acompanhamento da evolução por meio de funcionalidades como autenticação de usuários, organização das disciplinas e controle das sessões realizadas.

Além de resolver um problema prático, este projeto tem como foco o aprendizado e a aplicação de boas práticas no desenvolvimento de APIs utilizando Python e FastAPI.

## 👨‍💻 Autor

Lucas Gabriel Nascimento