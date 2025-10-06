# sentiric-llm-streaming-service/app/main.py
from fastapi import FastAPI, status
from fastapi.responses import StreamingResponse
from contextlib import asynccontextmanager
from app.core.logging import setup_logging
from app.core.config import settings
import structlog
import asyncio
import json

logger = structlog.get_logger(__name__)

async def mock_streaming_generator(prompt: str):
    """Placeholder: Gerçek zamanlı LLM akışını simüle eder."""
    words = [f"Simulated", "response", "for", prompt.split()[0], "is", "streaming", "now."]
    for word in words:
        # LLM token'ını JSON formatında Event Source formatına benzer şekilde göndeririz
        chunk = {"generated_text": word + " "}
        yield json.dumps(chunk) + "\n"
        await asyncio.sleep(0.1) # 100ms gecikme ile token gönderimi
    
    # Son paket (opsiyonel)
    yield json.dumps({"generated_text": "", "is_final": True}) + "\n"


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    logger.info("LLM Streaming Service başlatılıyor", version=settings.SERVICE_VERSION, env=settings.ENV)
    
    # TODO: Harici LLM API istemcileri (Eğer burası direkt harici API'ye bağlanıyorsa)
    
    yield
    
    logger.info("LLM Streaming Service kapatılıyor")

app = FastAPI(
    title="Sentiric LLM Streaming Service",
    description="Akış Bazlı LLM Çıktısı",
    version=settings.SERVICE_VERSION,
    lifespan=lifespan
)

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "ok", "service": "llm-streaming"}

# Streaming endpoint'i: LLM Gateway bu endpoint'i çağıracaktır.
# Content-Type: application/x-ndjson (newline-delimited JSON) veya text/event-stream
@app.post(settings.API_V1_STR + "/generate_stream")
async def generate_stream(prompt: str):
    logger.info("Streaming isteği alındı", prompt=prompt)
    
    # Gerçek akışı StreamingResponse ile döndür
    return StreamingResponse(
        mock_streaming_generator(prompt), 
        media_type="application/jsonl" # Newline Delimited JSON
    )