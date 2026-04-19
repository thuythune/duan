# --- Document and Paths ---
DOC_PATH = "./input3.pdf"
PERSIST_DIRECTORY = "./chroma_db_beta_rag" # Directory to store the Chroma vector database

# --- Model Names ---
MODEL_NAME = "nvidia/nemotron-3-super-120b-a12b:free" # Model gánh Text generation trên đường truyền OpenRouter
OPENROUTER_API_KEY = "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" # BẮT BUỘC ĐIỀN API KEY TẠI ĐÂY
EMBEDDING_MODEL = "bge-m3" # Vẫn giữ nguyên bge-m3 chạy bằng Ollama dưới máy em

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