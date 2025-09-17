

````markdown
# CRUD Usuários — FastAPI + Frontend

Este projeto é um exemplo simples de **CRUD (Create, Read, Update, Delete)** de usuários, feito com:
- **Backend**: FastAPI (API REST)
- **Frontend**: HTML + JS (requisições via `fetch`)

---

## 🚀 Como rodar a API

### 1. Instalar dependências
No terminal:
```bash
pip install fastapi uvicorn
````

### 2. Subir o servidor

Na pasta do projeto, execute:

```bash
uvicorn main:app --reload --port 3344
```

A API ficará disponível em:

```
http://127.0.0.1:3344
```

---

## 🖥️ Como usar o Frontend

1. Abra o arquivo `index.html` no navegador.
2. No campo **Base URL da API**, deixe:

   ```
   http://127.0.0.1:3344
   ```
3. Agora é só testar:

   * **GET /users** → listar todos os usuários
   * **GET /users/{id}** → buscar por ID
   * **POST /users** → criar usuário
   * **PUT /users/{id}** → atualizar usuário
   * **DELETE /users/{id}** → remover usuário

---

## 📂 Estrutura do projeto

```
.
├── main.py       # Código da API FastAPI
├── index.html    # Frontend simples para interagir com a API
└── README.md     # Instruções do projeto
```

---

## 🛠️ Git — Passo a Passo

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/req_test.git
cd req_test
```

### 2. Salvar alterações

```bash
git add .
git commit -m "feat: adiciona API FastAPI e frontend CRUD"
```

### 3. Enviar alterações para o GitHub

> ⚠️ Se o repositório remoto já tiver commits que você não tem, use `pull --rebase`.

```bash
git pull origin main --rebase
git push origin main
```

### 4. Caso queira sobrescrever o remoto (cuidado!)

```bash
git push origin main --force
```

---

## 📌 Endpoints da API

* `GET    /users` → lista todos
* `GET    /users/{id}` → retorna 1 usuário
* `POST   /users` → cria novo usuário (`{ "id": 1, "name": "Ana" }`)
* `PUT    /users/{id}` → atualiza usuário (`{ "id": 1, "name": "João" }`)
* `DELETE /users/{id}` → remove usuário


