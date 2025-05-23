import os
from dotenv import load_dotenv

def cargar_api_key():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("❌ No se encontró la OPENAI_API_KEY en el archivo .env")
    return api_key
