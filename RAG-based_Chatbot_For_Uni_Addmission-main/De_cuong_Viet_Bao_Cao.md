# Kịch Bản Viết Báo Cáo Đồ Án Tốt Nghiệp: RAG Chatbot Tuyển Sinh

Dựa vào cấu trúc 4 chương mà bạn vừa gửi, mình đã ánh xạ trực tiếp nó vào "linh hồn" của bộ code mà chúng ta đang có. Bạn hãy dùng bộ khung dàn ý siêu chi tiết này để bắt đầu gõ văn bản cho Quyển Báo Cáo trên file Word của bạn nhé!

---

## Chương 1: Khảo sát thực tế và phân tích nghiệp vụ

**1.1. Khảo sát thực tế:**
*   **Bối cảnh:** Hằng năm, số lượng thí sinh có nhu cầu tra cứu thông tin tại trường Đại học là rất lớn. Các câu hỏi thường xoay quanh chỉ tiêu, điểm chuẩn, lệ phí, tổ hợp môn...
*   **Điểm nghẽn hiện tại:** Dữ liệu nằm rải rác hoặc ẩn sâu trong cuốn "Sổ tay quy chế tuyển sinh" dài hàng trăm trang PDF. Sinh viên tự tìm thì nản, mà gọi tổng đài viên thì quá tải.
*   **Hướng giải quyết:** Cần một nhân viên "ảo" túc trực 24/7, có trí nhớ siêu việt, đã đọc thuộc lòng cuốn PDF đó để giải đáp ngay lập tức cho sinh viên.

**1.2. Phân tích nghiệp vụ (Quy trình hệ thống):**
*   **Nghiệp vụ Xử lý Hồ Sơ (Offline):** Nhà trường ban hành file quy chế dạng PDF (chính là file `input3.pdf` trong project). Hệ thống thay vì đọc cả cuốn, sẽ băm nhỏ nó ra thành từng đoạn vài trăm chữ để dễ tìm kiếm.
*   **Nghiệp vụ Phục vụ (Online):** Sinh viên đặt câu hỏi (VD: Mã ngành trí tuệ nhân tạo là gì?). Hệ thống mang câu hỏi đó đi lục lọi trong các đoạn văn bản đã băm nhỏ xem đoạn nào nói về "trí tuệ nhân tạo". Sau đó rút đoạn văn đó ra, đưa cho AI đọc và bắt AI tóm tắt thành tiếng Việt đưa lại cho sinh viên.

---

## Chương 2: Giới thiệu công nghệ

Phần này bạn chỉ cần copy khái niệm lý thuyết từ Google, NHƯNG nhớ ghép thêm đoạn "Ứng dụng trong đồ án" để thầy cô thấy bạn thật sự nắm rõ vấn đề:

*   **LLM (Mô hình ngôn ngữ lớn):** Giới thiệu LLM là gì. **Ứng dụng:** Đồ án sử dụng `Qwen2.5:3b` vì nó tối ưu cho Tiếng Việt và nhẹ, chạy được cục bộ (nội bộ ảo hóa trên máy trường) qua Ollama giúp tránh làm rò rỉ dữ liệu quy chế ra bên ngoài như khi dùng ChatGPT.
*   **RAG (Retrieval-Augmented Generation):** Giải thích nó là sự kết hợp giữa "Tìm kiếm văn bản" và "Tạo sinh câu chữ". **Ứng dụng:** Giúp chatbot không bị ảo giác (hallucination) và không bịa ra thông tin mã ngành sai.
*   **Python:** Ngôn ngữ dùng để làm AI. Các thư viện dùng là `langchain` (để ráp nối các khối AI) và `ChromaDB` (để lưu trữ dữ liệu Vector).
*   **FastAPI:** Nền tảng Server cực nhẹ của Python. **Ứng dụng:** Tạo hệ thống Backend đa luồng, chuyên quản lý các endpoint (cụ thể là `POST /chat`).
*   **Next.js:** Framework mạnh nhất của React. **Ứng dụng:** Dựng giao diện hộp thoại mượt mà, đẳng cấp, giao tiếp với FastAPI.

---

## Chương 3: Thiết kế và Xây dựng hệ thống

Chương này là quan trọng nhất, nơi bạn sẽ khoe toàn bộ đống code mà chúng ta vừa làm:

**3.1. Thiết kế Hệ thống Client-Server:**
*   **Tách biệt vi mô:** Thay vì code một cục rườm rà, bạn đã thiết kế chia tách Mặt tiền (Frontend: Next.js) nằm ở cổng 3000, và Não bộ (Backend: FastAPI) nằm ở cổng 8000. Điều này chứng minh đồ án hoàn toàn có thể đem đi triển khai thực tế cấp trường.

**3.2. Sơ đồ khối hoạt động (Você có thể vẽ bằng Draw.io):**
*   Bạn có thể minh họa chu trình này theo thứ tự file code: 
     - **Bước 1 (Tiền xử lý):** `data_handler.py` cắt nhỏ PDF thành các đoạn văn.
     - **Bước 2 (Lưu trữ):** `vector_db_manager.py` dùng model `BGE-M3` biến các đoạn văn thành Vector và cất vào ổ cứng ChromaDB.
     - **Bước 3 (Người dùng tương tác):** Next.js (`page.js`) bắt text của người dùng gửi cho FastAPI (`backend_api.py`).
     - **Bước 4 (Sinh lởi):** `llm_services.py` kích hoạt quy trình RAG, lọc và ép buộc AI trả lời Tiếng Việt rành mạch.

**3.3. Thiết kế Prompt (Bí kíp tinh chỉnh AI):**
*   Trích xuất đoạn system prompt ra để phân tích: "Bạn là trợ lý AI hữu ích... CỦA BẠN PHẢI HOÀN TOÀN BẰNG TIẾNG VIỆT... KHÔNG giải thích dài dòng". Giải thích rằng nhờ lệnh thép này, AI không bị nói tiếng Anh hay nhảm nhí.

---

## Chương 4: Thực nghiệm và Đánh giá

**4.1. Môi trường Thực nghiệm:**
*   Phần cứng: Laptop cá nhân.
*   Framework: Đã chạy thành công 2 dịch vụ cùng lúc bằng file `run_all.bat`.

**4.2. Các Kịch Bản Test (Test cases):**
*   Bạn hãy chụp lại một số ảnh màn hình và đưa vào báo cáo:
    1.  *Test hỏi thông tin chính xác:* Hỏi "Mã ngành cntt", chụp ảnh AI bám sát dữ liệu trả về đúng.
    2.  *Test hỏi ngoài lề:* Bạn hãy thử hỏi AI một thông tin KHÔNG có trong PDF (VD: Em muốn học nấu ăn). Xem AI có thật thà bảo "Em không tìm thấy thông tin trong tài liệu" không. Nếu có, đây là TRƯỜNG HỢP KIỂM CHỨNG TỐT NHẤT chứng minh RAG hoạt động.

**4.3. Đánh giá ưu điểm/nhược điểm:**
*   **Ưu điểm:** Tốc độ phản hồi tốt (nhờ chuyển sang LLM gọn nhẹ), trả lời chính xác, độ bảo mật cao vì mọi thứ nằm ở localhost. Giao diện mượt mà của Next.js (chống chớp giật so với Streamlit cũ).
*   **Nhược điểm (Hướng phát triển):** Nếu PDF là ảnh scan sẽ khó đọc (cần tích hợp OCR trong tương lai mở rộng),...
