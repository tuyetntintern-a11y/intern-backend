# Intern Backend

Backend project using FastAPI.

## Setup

### 1. Create virtual environment

```powershell
python -m venv venv
```

### 2. Activate virtual environment

Windows PowerShell:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install fastapi uvicorn
```

## Run Server

Run the following command from the project root directory:

```powershell
python -m uvicorn app.server:app --reload
```

Server will start:

```
http://127.0.0.1:8000
```

## API

### Health Check

Endpoint:

```
GET /api/health
```

URL:

```
http://127.0.0.1:8000/api/health
```

Response example:

```json
{
  "status": "ok"
}
```