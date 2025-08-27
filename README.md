Multi-Container App (Flask + PostgreSQL)

This project is a beginner-friendly DevOps application that demonstrates how to containerize and orchestrate a simple Python web service with a PostgreSQL database using Docker Compose.

It also includes CI/CD with GitHub Actions to validate Docker builds automatically.

🚀 Project Overview

Backend: A Python Flask API with two endpoints:

/health → reports service status

/db → connects to PostgreSQL and verifies database access

Database: PostgreSQL with persistent storage

Orchestration: Docker Compose manages multi-container networking

CI/CD: GitHub Actions workflow builds and tests the project automatically on each push

🗂 Repository Structure
multi-container-app/
├─ Backend/             # Flask backend service
│  ├─ app.py
│  ├─ requirements.txt
│  └─ Dockerfile
├─ docker-compose.yml   # Service orchestration (Flask + Postgres)
├─ .gitignore           # Ignore unnecessary files
└─ README.md            # Project documentation

⚙️ Prerequisites

Before running locally, install:

Docker Desktop

Git

(Optional) GitHub Desktop
 for repo management

▶️ How to Run Locally

Clone the repo:

git clone https://github.com/<your-username>/multi-container-app.git
cd multi-container-app


Start the containers:

docker compose up --build


Access the app:

Backend health: http://localhost:5000/health

{"status": "healthy"}


Database test: http://localhost:5000/db

Stop everything:

docker compose down -v

🧪 CI/CD Pipeline

This repo uses GitHub Actions for CI/CD:

On each push, the workflow builds the Docker images and runs Compose

Ensures Dockerfiles and service orchestration remain valid

Workflow file is stored in:

.github/workflows/ci.yml

🎯 Learning Goals

This project is designed to build core DevOps skills:

Dockerfile authoring

Multi-container orchestration with Docker Compose

Container networking and environment variables

Database initialization in containers

GitHub Actions for CI/CD pipelines

Repository structuring & documentation best practices

📝 Next Steps

Add migrations with Flask-Migrate to manage DB schema

Add a frontend (React/Next.js) for a full-stack example

Deploy to a cloud provider (Azure, AWS, or GCP)

📚 References

Flask Documentation

PostgreSQL Documentation

Docker Compose Docs

GitHub Actions Docs
