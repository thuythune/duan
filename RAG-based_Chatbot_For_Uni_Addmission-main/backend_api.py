import os
import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import config
import data_handler
import vector_db_manager
import llm_services
from utils import setup_logging

# Khởi tạo log
setup_logging()

# Khởi tạo FastAPI
app = FastAPI(title="E-JUST Admisson RAG API")

# Cấu hình CORS để Next.js (chạy port 3000) có thể giao tiếp
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Trong production nên để cụ thể http://localhost:3000
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models định nghĩa dữ liệu API
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    answer: str

# Biến lưu trữ Pipeline
RAG_CHAIN = None
HISTORY_DB = None

@app.on_event("startup")
async def startup_event():
    """Khởi động và tải AI, Vector DB vào RAM sẵn sàng chiến đấu."""
    global RAG_CHAIN, HISTORY_DB
    logging.info("Starting up API Server and initializing RAG Pipeline...")
    
    DOC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input3.pdf')
    
    # 1. Tải Embedding Model
    embedding_model = llm_services.get_embedding_model()
    if not embedding_model:
        logging.error("Failed to load Embedding Model.")
        return

    # 2. Kiểm tra/Tạo Vector DB
    db = vector_db_manager.load_or_create_vector_db()
    if not db:
        logging.critical("Failed to load or create Vector DB.")
        return

    HISTORY_DB = vector_db_manager.load_or_create_history_db()

    # 3. Khởi tạo LLM và Retriever
    llm = llm_services.get_llm()
    if not llm:
        logging.error("Failed to load LLM Model.")
        return

    retriever = llm_services.get_retriever(db, llm)
    history_retriever = llm_services.get_history_retriever(HISTORY_DB)
    
    # 4. Gắn kết thành RAG Chain
    RAG_CHAIN = llm_services.get_rag_chain(retriever, history_retriever, llm)
    logging.info("RAG Pipeline initialization complete! Server is Ready.")


@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    """Nhận câu hỏi từ Frontend và nhả câu trả lời."""
    if RAG_CHAIN is None:
        raise HTTPException(status_code=500, detail="RAG Pipeline is not initialized.")
    
    try:
        logging.info(f"Received query: {req.message}")
        answer = RAG_CHAIN.invoke(req.message)
        
        # Lưu câu hỏi và câu trả lời vào history DB
        if HISTORY_DB is not None:
            vector_db_manager.save_to_history(HISTORY_DB, req.message, answer)
            
        return ChatResponse(answer=answer)
    except Exception as e:
        logging.error(f"Error during RAG invocation: {e}")
        raise HTTPException(status_code=500, detail=str(e))
