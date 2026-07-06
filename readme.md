# FastAPI MongoDB CRUD API

A simple REST API built with **FastAPI** and **MongoDB** using the asynchronous **PyMongo** driver. This project demonstrates basic CRUD (Create, Read, Update, Delete) operations.

## Features

- Create a user
- Retrieve all users
- Retrieve a user by ID
- Update a user
- Delete a user
- Asynchronous MongoDB operations
- Interactive API documentation with Swagger UI

## Tech Stack

- Python 3
- FastAPI
- PyMongo
- MongoDB
- Pydantic
- Uvicorn

## Project Structure

```text
app/
├── database.py
├── main.py
└── schemas.py

.env
requirements.txt
README.md
```

## Installation


### 2. Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the API

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- **API:** http://127.0.0.1:8000
- **Swagger UI:** http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
| :----: | :------: | ----------- |
| POST | `/users` | Create a new user |
| GET | `/users` | Retrieve all users |
| GET | `/users/{id}` | Retrieve a user by ID |
| PUT | `/users/{id}` | Update a user |
| DELETE | `/users/{id}` | Delete a user |
