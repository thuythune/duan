# ICTU AI Admission Assistant

Đây là dự án Chatbot Tư vấn Tuyển sinh ứng dụng RAG (Retrieval-Augmented Generation) dành cho **Trường Đại học Công nghệ Thông tin và Truyền thông (ICTU)**.
Hệ thống sử dụng tài liệu PDF nội bộ (Đề án tuyển sinh) để giải đáp các câu hỏi một cách chính xác nhất mà không gặp phải tình trạng bịa đặt thông tin (hallucination).

## Kiến trúc Hệ thống
- **Backend:** FastAPI (Python), LangChain
- **Vector Database:** ChromaDB
- **LLM Engine:** Ollama local model (`gemma2:2b`)
- **Embedding Model:** `bge-m3`
- **Frontend:** Next.js (React) giao diện hiện đại

## Cài đặt nhanh

### Yêu cầu
- Python 3.10+
- Node.js & npm (để chạy giao diện web)
- [Ollama](https://ollama.com) (tải và cài đặt để chạy local AI)

### Các bước cài đặt
1. Cài đặt các thư viện Python:
   ```bash
   pip install -r requirements.txt
   ```
2. Cài đặt các thư viện Node.js cho Frontend:
   ```bash
   cd frontend
   npm install
   cd ..
   ```
3. Khởi động các Model (Đảm bảo ứng dụng Ollama đang chạy):
   ```bash
   ollama pull gemma2:2b
   ollama pull bge-m3
   ```
4. Đặt tài liệu PDF tuyển sinh của trường vào folder gốc và đổi tên thành `input3.pdf` (nếu cần thay đổi tên, xem trong `config.py`)

5. Chạy toàn bộ hệ thống bằng 1 lệnh duy nhất:
   ```bash
   python app.py
   ```
   Lệnh này sẽ khởi động AI Backend trên cổng 8000 và Frontend trên cổng 3000, sau đó tự động mở trình duyệt.