# 🎮 Game Tracker

A full-stack web application designed to help users organize their video game collections, track their gaming progress, and manage their backlog.

Built with **FastAPI, PostgreSQL, SQLModel, and Vue.js**.

> 🚧 **Project Status:** In Development

## 📑 Table of Contents

1. [About the Project](#-about-the-project)
2. [Tech Stack](#-tech-stack)
3. [Planned Features](#-planned-features)
4. [Project Structure](#-project-structure)
5. [Getting Started](#-getting-started)
6. [Database Setup](#-database-setup)
7. [Environment Variables](#-environment-variables)
8. [Running the Backend](#-running-the-backend)
9. [GitHub Actions](#-github-actions)
10. [API Endpoints](#-api-endpoints)
11. [Future Improvements](#-future-improvements)

---

## 📖 About the Project

Game Backlog Tracker is a personal project created to strengthen my full-stack development skills.

The application is designed to help users keep track of games they own, are currently playing, or have completed.

This project focuses on improving my understanding of:

- RESTful API development
- CRUD operations
- Relational databases
- PostgreSQL and SQLModel
- Data validation using Pydantic
- Automated testing
- Continuous integration with GitHub Actions
- Frontend and backend integration

The initial version focuses on core functionality without user authentication.

---

## 🛠️ Tech Stack

### Backend

- 🐍 Python
- ⚡ FastAPI
- 🗄️ PostgreSQL
- 🔗 SQLModel
- ✅ Pydantic
- 🧪 pytest
- 🧹 Ruff

### Frontend (Planned)

- 💚 Vue.js
- ⚡ Vite
- 🎨 CSS

### Development Tools

- 💻 Visual Studio Code
- 🐙 Git & GitHub
- 🔄 GitHub Actions
- 📦 pip

---

## ✨ Planned Features

- 🎮 Add games to a personal backlog
- 📋 View saved games
- ✏️ Edit game information
- 🗑️ Delete games
- 🎯 Track game completion status
- ⭐ Rate completed games
- 📝 Add personal notes
- 🕹️ Record gaming platforms
- 🏷️ Organize games by genre
- 📅 Track release and completion dates

---

## 📁 Project Structure

The project is organized into separate backend and frontend directories.

Example structure:

```text
Game-Tracker-NoAuth/
│
├── .github/
│   └── workflows/
│       └── backend-ci.yml
│
├── backend/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── tests/
│   ├── database.py
│   ├── main.py
│   └── .env
│
├── frontend/                # Planned frontend
│
├── .gitignore
├── requirements.txt
└── README.md
```

*The structure may change as development continues.*

---

## 🚀 Getting Started

### Prerequisites

Before running this project, make sure you have:

- Python 3.12
- PostgreSQL
- Git
- pip

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Game-Tracker-NoAuth.git
```

Navigate into the project:

```bash
cd Game-Tracker-NoAuth
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

Navigate into the backend directory:

```bash
cd backend
```

Create the virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

From the `backend` directory:

```bash
python -m pip install -r ../requirements.txt
```

This installs the Python dependencies required for the backend.

---

## 🗄️ Database Setup

This project uses PostgreSQL for data storage and SQLModel for database operations.

### 1. Create the database

Ensure your PostgreSQL server is running.

From your terminal:

```bash
createdb game_tracker
```

Alternatively, inside PostgreSQL:

```sql
CREATE DATABASE game_tracker;
```

Only one method is required.

### 2. Verify the database

Connect to PostgreSQL:

```bash
psql -d game_tracker
```

List existing tables:

```sql
\dt
```

If no tables exist yet, they will be created after the SQLModel table models are defined and the application's table-creation function runs.

---

## 🔐 Environment Variables

Create a `.env` file inside the `backend` directory.

Add the following:

```env
DATABASE_URL=postgresql+psycopg://YOUR_USERNAME@localhost:5432/game_tracker
```

Replace `YOUR_USERNAME` with your PostgreSQL username.

If your PostgreSQL server requires password authentication, include the appropriate credentials.

### Security

The `.env` file is excluded from version control using `.gitignore`.

Sensitive information such as database passwords and API keys should never be committed to GitHub.

---

## ▶️ Running the Backend

Navigate into the backend directory and activate your virtual environment.

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

**http://127.0.0.1:8000**

### 📚 API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc

These interfaces can be used to test API endpoints.

---

## 🔄 GitHub Actions

This project uses GitHub Actions for continuous integration (CI).

The backend workflow is configured to run when changes are pushed to GitHub.

### CI Workflow

| Step | Description |
|---|---|
| 📥 Checkout | Retrieves repository code |
| 🐍 Python Setup | Configures Python 3.12 |
| 📦 Dependencies | Installs required packages |
| 🧹 Ruff | Checks Python code quality |
| 🧪 pytest | Runs automated tests |

### Purpose

Continuous integration helps:

- Identify coding errors early
- Maintain consistent code quality
- Catch bugs through automated tests
- Verify changes before further development

The workflow will become more useful as automated backend tests are implemented.

---

## 🌐 API Endpoints

The following REST API endpoints are planned for managing games.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/games` | Retrieve all games |
| `GET` | `/games/{id}` | Retrieve a specific game |
| `POST` | `/games` | Create a new game |
| `PATCH` | `/games/{id}` | Update an existing game |
| `DELETE` | `/games/{id}` | Delete a game |
 `DELETE` | `/games` | Delete all games |

Additional endpoints may be introduced during development.

---

## 🔮 Future Improvements

Potential future enhancements include:

- 🔐 User authentication
- 🔍 Search and filtering
- 📊 Gaming statistics
- 🎮 Third-party video game API integration
- 📱 Responsive frontend design
- 🧪 Additional automated tests
- 🗄️ Database migrations using Alembic
- ☁️ Production deployment

These features are outside the initial project scope and may be implemented in future versions.

---

## 🎯 Project Goals

The primary goal of this project is to strengthen my backend development skills through practical application.

Areas of focus include:

1. Building RESTful APIs with FastAPI.
2. Implementing CRUD functionality.
3. Designing relational database models.
4. Connecting PostgreSQL using SQLModel.
5. Writing and maintaining automated tests.
6. Using GitHub Actions for continuous integration.
7. Building a maintainable full-stack application.

---

## 👩🏽‍💻 Development Status

🚧 This project is currently under active development.

Core backend functionality is being implemented before expanding into frontend integration and additional features.
