from huggingface_hub import InferenceClient

from app.core.config import settings


client = InferenceClient(
    api_key=settings.HF_TOKEN,
)