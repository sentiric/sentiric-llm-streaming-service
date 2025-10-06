# sentiric-llm-streaming-service/app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Sentiric LLM Streaming Service"
    API_V1_STR: str = "/api/v1"
    
    ENV: str = "production"
    LOG_LEVEL: str = "INFO"
    SERVICE_VERSION: str = "0.1.0"
    
    # Hangi harici/uzman motorun streaming API'sine proxy yapacağı.
    # Örn: Gemini API veya yerel Ollama/Llama.cpp'nin streaming arayüzü.
    STREAMING_TARGET_URL: str
    
    # Akış hızını kontrol eden parametreler
    STREAMING_CHUNK_SIZE: int = 1024 

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding='utf-8',
        extra='ignore'
    )

settings = Settings()