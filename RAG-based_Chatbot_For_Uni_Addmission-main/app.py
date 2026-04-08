import subprocess
import os
import sys
import time
import webbrowser

def main():
    print("="*50)
    print("🚀 KHỞI ĐỘNG HỆ THỐNG RAG CHATBOT 🚀")
    print("="*50)
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 1. Khởi động AI Backend (FastAPI)
    print("\n[1/2] Đang khởi động AI Trí tuệ nhân tạo (Backend)...")
    backend_cmd = [sys.executable, "-m", "uvicorn", "backend_api:app", "--reload", "--port", "8000"]
    backend_process = subprocess.Popen(backend_cmd, cwd=base_dir)
    
    # 2. Khởi động Web Giao diện (Next.js)
    print("[2/2] Đang khởi động Giao diện Web (Frontend)...")
    frontend_dir = os.path.join(base_dir, "frontend")
    npm_cmd = "npm.cmd" if os.name == 'nt' else "npm"
    frontend_process = subprocess.Popen([npm_cmd, "run", "dev"], cwd=frontend_dir)
    
    print("\n✅ Hệ thống đã sẵn sàng!")
    print("👉 Hãy mở trình duyệt truy cập: http://localhost:3000")
    
    # Tự động mở trình duyệt sau 3 giây
    time.sleep(3)
    webbrowser.open("http://localhost:3000")
    
    try:
        # Giữ cho script sống để 2 process chạy lót nền
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nĐang tắt hệ thống...")
        backend_process.terminate()
        frontend_process.terminate()
        print("Đã tắt.")

if __name__ == "__main__":
    main()