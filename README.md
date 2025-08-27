# Multi-Container App with GitHub Actions CI/CD 🚀

This project showcases a multi-container web application using **Flask**, **PostgreSQL**, and **Redis**, orchestrated with **Docker Compose**. The entire CI/CD pipeline is automated using a **GitHub-only workflow**, demonstrating a modern, cloud-native DevOps approach without needing a local machine.

## Features ✨

  * **Three-tier architecture**: A **Python Flask** backend, a **PostgreSQL** database, and a **Redis** cache.
  * **Containerization**: Each service runs in its own Docker container, ensuring isolation and portability.
  * **Docker Compose**: A single `docker-compose.yml` file defines and manages the entire application stack.
  * **GitHub Actions**: A CI pipeline automatically builds and tests the application on every push and pull request to the `main` branch.

## Getting Started 💻

This project is designed to be built and run on GitHub. You don't need to clone the repository to your local machine to see it in action. The **GitHub Actions workflow** handles everything automatically.

### Project Structure

```
multi-container-app/
├─ backend/
│  ├─ app.py
│  ├─ requirements.txt
│  └─ Dockerfile
├─ db/
│  └─ init.sql
├─ .github/
│  └─ workflows/
│     └─ ci.yml
├─ docker-compose.yml
├─ .gitignore
└─ README.md
```

### Services

  * **`backend`**: A Flask application that connects to both PostgreSQL and Redis. It includes endpoints to check the database for seeded messages and to track hits using the Redis cache.
  * **`db`**: A PostgreSQL database instance that is seeded with initial data from `db/init.sql`.
  * **`redis`**: A Redis cache instance used for a simple hit counter.

## GitHub Actions CI/CD Pipeline 🚦

The `.github/workflows/ci.yml` file defines the CI/CD pipeline, which automatically runs whenever code is pushed to or a pull request is made against the `main` branch.

**The pipeline performs the following steps:**

1.  **Checkout repo**: Checks out the repository code.
2.  **Set up Docker Buildx**: Configures a Docker build environment.
3.  **Build containers**: Builds the `backend` container and pulls the `postgres` and `redis` images.
4.  **Run containers**: Starts all three containers in the background.
5.  **Wait for services**: Pauses briefly to ensure all services are up and running.
6.  **Test Flask health endpoint**: Uses `curl` to verify that the Flask backend is healthy and responding. This serves as a basic integration test.

You can monitor the workflow runs by navigating to the **Actions** tab in the repository.

## Technologies Used 🛠️

  * **Python 3.10**: The language for the backend application.
  * **Flask**: A lightweight Python web framework.
  * **psycopg2-binary**: Python adapter for PostgreSQL.
  * **redis-py**: Python client for Redis.
  * **Docker**: Containerization platform.
  * **Docker Compose**: Tool for defining and running multi-container Docker applications.
  * **GitHub Actions**: CI/CD platform.
