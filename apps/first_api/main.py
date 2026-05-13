import asyncio
import logging

from fastapi import FastAPI
from pydantic import BaseModel

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat(request: ChatRequest):
    logger.info(f"Received message: {request.message}")

    await asyncio.sleep(3)

    logger.info("Generated response successfully")

    return {
        "reply": f"LLM response to: {request.message}",
    }