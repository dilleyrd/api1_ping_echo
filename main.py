#
# # A simple FastAPI application with ping and echo endpoints.
#

# Import necessary libraries

from fastapi import FastAPI                 # FastAPI framework, for building APIs, handling requests, and routing
from pydantic import BaseModel              # Pydantic, for data validation and settings management using Python type annotations   
from typing import Optional                 # Optional type hinting, for parameters that can be None
from fastapi import HTTPException, Query    # HTTPException for error handling, Query for query parameter validation
from fastapi import Path                    # Path for path parameter validation, used in the math endpoint

# Create FastAPI instance
app = FastAPI(title="API-1 Ping and Echo")

# EchoIn and EchoOut are Pydantic models that define the shape of your JSON

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
# accepts a JSON body that must match EchoIn
# returns a JSON body that matches EchoOut
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

# Greet endpoint: /greet?name=YourName
@app.get("/greet")
def greet(name: str | None = Query(default=None, description="Your first name")):
    if not name:
        raise HTTPException(
            status_code=400,
            detail="Please add ?name=YourName to the URL (for example: /greet?name=Sam)"
        )
    return {"greeting": f"Hello, {name}!"}