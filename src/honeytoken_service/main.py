from fastapi import FastAPI, Request
from pydantic import BaseModel
from .generator import generate_api_key, fake_user, fake_db_row
from .alert import send_alert
import os

app = FastAPI(title="Honeytoken-as-a-Service")

ALERT_WEBHOOK = os.environ.get("ALERT_WEBHOOK")

class GenerateRequest(BaseModel):
    type: str = "api_key"
    ttl_seconds: int = 0


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/generate")
async def generate(req: GenerateRequest):
    if req.type == "api_key":
        token = generate_api_key()
        payload = {"type": "api_key", "token": token}
    elif req.type == "user":
        payload = {"type": "user", **fake_user()}
    elif req.type == "db_row":
        payload = {"type": "db_row", **fake_db_row()}
    else:
        payload = {"type": "unknown"}

    return payload


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    # In production: enrich, store, and notify
    if ALERT_WEBHOOK:
        send_alert(ALERT_WEBHOOK, data)
    return {"received": True}
