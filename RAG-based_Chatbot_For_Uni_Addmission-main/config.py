# --- Document and Paths ---
DOC_PATH = "./input3.pdf"
PERSIST_DIRECTORY = "./chroma_db_beta_rag" # Directory to store the Chroma vector database

# --- Model Names ---
MODEL_NAME = "gemma2:2b"
EMBEDDING_MODEL = "bge-m3"

# --- Vector Store ---
VECTOR_STORE_NAME = "beta-rag"

# --- History Store ---
HISTORY_PERSIST_DIRECTORY = "./chroma_db_history"
HISTORY_COLLECTION_NAME = "chat-history"

# --- Text Splitting ---
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

# --- Logging ---
LOG_LEVEL = "INFO"
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(module)s - %(message)s'