#
# # A simple FastAPI application with ping and echo endpoints.
#

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi import HTTPException
from fastapi import Path

# Create FastAPI instance
app = FastAPI(title="API-1 Ping and Echo")

# Define request model
class EchoIn(BaseModel):
    message: str

# Define response model
class EchoOut(BaseModel):
    message: str

# Define ping endpoint
@app.get("/ping")
def ping():
    return {"status": "ok"}

# Define echo endpoint
@app.post("/echo", response_model=EchoOut)
def echo(body: EchoIn):
    return {"message": body.message}


# Query-string version: /echo-query?message=Hello
@app.get("/echo-query", response_model=EchoOut)
def echo_query(message: Optional[str] = None):
    if not message:
        # A clear, friendly error for beginners:
        raise HTTPException(
            status_code=400,
            detail="Please add ?message=Hello to the URL (for example: /echo-query?message=Hello)"
        )
    return {"message": message}

# Path version: /echo-path/Hello
@app.get("/echo-path/{message}", response_model=EchoOut)
def echo_path(message: str):
    msg = message.strip()
    if not msg:
        raise HTTPException(status_code=400, detail="Message cannot be empty.")
    return {"message": msg}

# Math endpoint: /math/square/5
@app.get("/math/square/{n}")
def square(n: int = Path(ge=0, le=1000, description="A whole number from 0 to 1000")):
    return {"n": n, "square": n * n}

