# FastAPI Starter — Ping and Echo

## Quickstart
1. Create and activate a virtual environment.
2. `pip install -r requirements.txt`
3. `uvicorn main:app --reload`
4. Visit `http://localhost:8000/ping`. Use a REST client to POST to `/echo`.

## Endpoints
- `GET /ping` -> `{"status":"ok"}`
- `POST /echo` with JSON `{ "message": "hello" }` -> echoes back the message
