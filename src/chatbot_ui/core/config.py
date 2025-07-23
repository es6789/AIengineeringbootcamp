from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    GROQ_API_KEY: str
    GOOGLE_API_KEY: str
    OPENAI_API_KEY: str
    QDRANT_URL: str
    QDRANT_COLLECTION_NAME: str
    EMBEDDING_MODEL: str
    EMBEDDING_MODEL_PROVIDER: str
    GENERATION_MODEL: str
    GENERATION_MODEL_PROVIDER: str
    LANGSMITH_TRACING: bool
    LANGSMITH_ENDPOINT: str
    LANGSMITH_API_KEY: str
    LANGSMITH_PROJECT: str
    


config = Config()