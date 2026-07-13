# Intern Backend

## Setup

Create a virtual environment:

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
venv\Scripts\activate
```

Install dependencies:

```powershell
python -m pip install fastapi uvicorn
```

## Run Server

```powershell
python -m uvicorn app.server:app --reload
```

## Health Check

Open:

```text
http://127.0.0.1:8000/api/health
```