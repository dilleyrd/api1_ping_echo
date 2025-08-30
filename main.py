#
# # A simple FastAPI application with ping and echo endpoints.
#

from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI instance
app = FastAPI(title="API-1 Ping and Echo")

# Define request and response models
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
