# Alternative Assets Python Backend

This is a FastAPI-based backend service for managing alternative assets data. The service provides several API endpoints to retrieve information about investors, assets by investors, and investor commitments.

# Getting Started

## Prerequisites

- Python 3.12 or higher
- Poetry for dependency management 
- Docker (optional, for containerised deployment)

## Clone the repository

```bash
git clone https://github.com/mbarclay/alternative-assets-fullstack
cd alternative-assets-fullstack/alternative-assets-backend
```

## Install dependencies using Poetry:

```bash
poetry install
```

## Run the application:
You can start the application using Uvicorn directly:

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

The service will be available at http://localhost:8000

### Docker

Alternatively, you can build and run using Docker:

```bash
docker build -t alternative-assets-backend .
docker run -d -p 8000:8000 alternative-assets-backend
```

Configuration files such as config.py and settings.toml are copied into the Docker container during the build process.

## API Endpoints

- GET /: Returns a welcome message. 
- GET /investors: Retrieves a list of all investors. 
- GET /assets-summary/{investor_code}: Retrieves a summary of assets by a specific investor. 
- GET /investor/{investor_code}/commitments/asset-class/{asset_class_code}: Retrieves investor commitments for a specific asset class.

## Formating and Linting

The project has been configured with [Ruff](https://docs.astral.sh/ruff/)

### To sort imports and format the project:

```bash
ruff check --select I --fix
ruff format ./
```

### To lint the project:

```bash
ruff check ./
```