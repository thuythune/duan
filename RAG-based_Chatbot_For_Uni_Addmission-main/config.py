import os
from dotenv import load_dotenv
load_dotenv("key.env")
# --- Document and Paths ---
DOC_PATH = "./input3.pdf"
PERSIST_DIRECTORY = "./chroma_db_beta_rag" # Directory to store the Chroma vector database
# --- Model Names ---
MODEL_NAME = "google/gemma-4-26b-a4b-it:free" # Model gánh Text generation trên đường truyền OpenRouter
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
EMBEDDING_MODEL = "bge-m3" # Vẫn giữ nguyên bge-m3 chạy bằng Ollama dưới máy

# --- Vector Store ---
VECTOR_STORE_NAME = "beta-rag"

# --- History Store ---
HISTORY_PERSIST_DIRECTORY = "./chroma_db_history"
HISTORY_COLLECTION_NAME = "chat-history"

# --- Text Splitting ---
CHUNK_SIZE = 1500
CHUNK_OVERLAP = 300

# --- Logging ---
LOG_LEVEL = "INFO"
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(module)s - %(message)s'