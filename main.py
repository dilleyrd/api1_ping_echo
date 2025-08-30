from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API-1 Ping and Echo")

class EchoIn(BaseModel):
    message: str

class EchoOut(BaseModel):
    message: str

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.post("/echo", response_model=EchoOut)
def echo(body: EchoIn):
    return {"message": body.message}
