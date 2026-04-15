import logging

from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


from config import MODEL_NAME, EMBEDDING_MODEL


def get_llm():
    """Initializes and returns the ChatOllama LLM instance."""
    logging.info(f"Initializing LLM: {MODEL_NAME}")
    return ChatOllama(model=MODEL_NAME)


def get_embedding_model():
    """Initializes and returns the OllamaEmbeddings instance."""
    logging.info(f"Initializing Embedding Model: {EMBEDDING_MODEL}")
    return OllamaEmbeddings(model=EMBEDDING_MODEL)


def get_retriever(_vector_db, _llm):  
    """
    Creates a standard retriever.
    _vector_db: The cached vector database instance.
    _llm: The cached LLM instance (kept for signature compatibility).
    """
    if _vector_db is None or _llm is None:
        logging.error("Vector DB or LLM is None, cannot create retriever.")
        return None

    logging.info("Creating Standard Retriever.")
    # Sử dụng retriever mặc định để tốc độ nhanh gọn nhất
    retriever = _vector_db.as_retriever(search_kwargs={"k": 4})
    return retriever


def get_history_retriever(_history_db):
    """
    Creates a retriever for Q&A history.
    """
    if _history_db is None:
        logging.warning("History DB is None, cannot create history retriever.")
        return None
    logging.info("Creating History Retriever.")
    return _history_db.as_retriever(search_kwargs={"k": 2})


def get_rag_chain(_retriever, _history_retriever, _llm):
    """
    Creates the RAG chain.
    _retriever: The cached document retriever instance.
    _history_retriever: The cached history retriever instance.
    _llm: The cached LLM instance.
    """
    if _retriever is None or _llm is None:
        logging.error("Retriever or LLM is None, cannot create RAG chain.")
        return None

    logging.info("Creating RAG chain.")
    template = """Bạn là một trợ lý AI hữu ích. Hãy trả lời câu hỏi DỰA TRÊN bối cảnh được cung cấp dưới đây. 
Nếu bối cảnh không có thông tin, hãy trả lời rằng bạn không tìm thấy thông tin trong tài liệu. 
LƯU Ý QUAN TRỌNG: 
1. Câu trả lời CỦA BẠN PHẢI HOÀN TOÀN BẰNG TIẾNG VIỆT.
2. Hãy trả lời thật NGẮN GỌN, đi thẳng vào trọng tâm câu hỏi. KHÔNG giải thích dài dòng hoặc đưa thêm thông tin thừa không được hỏi.

Bối cảnh từ tài liệu tuyển sinh:
{context}

Lịch sử trò chuyện liên quan (nếu có):
{history}

Câu hỏi: {question}
Câu trả lời (bằng Tiếng Việt):
"""
    prompt = ChatPromptTemplate.from_template(template)
    
    def get_history(query):
        if _history_retriever:
            docs = _history_retriever.invoke(query)
            return "\n\n".join([doc.page_content for doc in docs])
        return "Không có."

    chain = (
            {
                "context": _retriever, 
                "history": get_history,
                "question": RunnablePassthrough()
            }
            | prompt
            | _llm
            | StrOutputParser()
    )
    return chain