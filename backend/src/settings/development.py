import os

from dotenv import load_dotenv
from src.summarization.engines import LangChain, LiteLLMFlow

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

CORS_CONFIG = {
    "allow_origins": ["*"],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}

# Configurações OpenAI
OPEN_AI_TOKEN = os.getenv("OPEN_AI_TOKEN")

# Configurações TensorFlow
TENSORFLOW_MODEL_NAME = os.getenv("TENSORFLOW_MODEL_NAME")

# Configurações LiteLLM
LITELLM_API_URL = os.getenv("LITELLM_API_URL")
LITELLM_API_KEY = os.getenv("LITELLM_API_KEY")
LITELLM_MODEL = os.getenv("LITELLM_MODEL")

# Carga automática da engine a ser usada pelo service
LLM_ENGINES = {
    "LiteLLMFlow": LiteLLMFlow(
        url_api=LITELLM_API_URL,
        api_key=LITELLM_API_KEY,
        model=LITELLM_MODEL
    ),
    "LangChain": LangChain(api_key=OPEN_AI_TOKEN),
    # "Tensorflow": TensorFlow(model_name=TENSORFLOW_MODEL_NAME),
}
