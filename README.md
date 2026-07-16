## 📋 API de acompanhamento de estudos

## 🚀 Funcionalidades

Usuários:

- Cadastro de usuário
- Login com JWT

Matérias:

- Cadastro de matérias
- Listagem das matérias do usuário autenticado

Sessões de estudo:

- Cadastro de sessões
- Listagem das sessões
- Conclusão de uma sessão

Relatórios:

- Total de horas estudadas por matéria


## 🛠️ Tecnologias utilizadas

- Python 3
- FasAPI
- SQLite3
- SQLAlchemy
- Pydantic
- JWT (JSON Web Token)
- Passlib  
- Bcrypt
- python-jose
- python-dotenv
- Uvicorn


## ⚙️ Como instalar dependências

Clone o repositório:

```bash
git clone https://github.com/Lgnlab/API-de-acompanhamento-de-estudos
```

Entre na pasta:

```bash
cd API-controle-de-estudo
```

Crie o ambiente virtual:

### Windows

```bash
python -m venv .venv
```

Ative:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

-Configuração do .env

Crie um arquivo chamado:

```text
.env
```

Com o seguinte conteúdo:

```env
DATABASE_URL=sqlite:///database.db

SECRET_KEY=sua_chave_secreta

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30


## ⚙️ Como executar a aplicação

uvicorn app.main:app --reload
A API ficará disponível em:
http://127.0.0.1:8000


## 🎯 Objetivo do projeto

API de acompanhamento de estudos é uma API REST desenvolvida para auxiliar no gerenciamento dos estudos de um usuário.

O objetivo é permitir o cadastro de matérias, o registro de sessões de estudo e o acompanhamento da evolução por meio de funcionalidades como autenticação de usuários, organização das disciplinas e controle das sessões realizadas.

Além de resolver um problema prático, este projeto tem como foco o aprendizado e a aplicação de boas práticas no desenvolvimento de APIs utilizando Python e FastAPI.

## Aprendizados

Durante este projeto foram praticados:

- Desenvolvimento de APIs REST
- FastAPI
- SQLAlchemy ORM
- Relacionamentos entre tabelas
- Autenticação JWT
- Hash de senhas
- Proteção de rotas
- CRUD
- Agregações SQL (`SUM` e `GROUP BY`)
- Organização em camadas


## 👨‍💻 Autor

Lucas Gabriel Nascimento