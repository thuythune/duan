"use client";

import { useState, useRef, useEffect } from "react";
import Link from "next/link";

export default function Chatbot() {
  const [messages, setMessages] = useState([
    { role: "ai", content: "Xin chào! Mình là trợ lý AI tuyển sinh của Đại học CNTT & TT (ICTU). Mình có thể giúp gì cho bạn hôm nay?" }
  ]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [history, setHistory] = useState([
    { id: 1, title: 'Hỏi về điểm chuẩn CNTT' },
    { id: 2, title: 'Học phí Kỹ thuật phần mềm' },
  ]);
  
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = async () => {
    if (!input.trim()) return;
    
    const userMessage = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsLoading(true);

    try {
      const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage.content }),
      });

      if (!response.ok) {
        throw new Error("Lỗi kết nối tới máy chủ AI");
      }

      const data = await response.json();
      setMessages((prev) => [...prev, { role: "ai", content: data.answer }]);
    } catch (error) {
      setMessages((prev) => [...prev, { role: "ai", content: "Xin lỗi, máy chủ AI hiện đang quá tải hoặc gặp sự cố. Bạn vui lòng thử lại sau nhé." }]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="app-container">
      {/* Sidebar */}
      <aside className="sidebar">
        <div className="sidebar-header">
          <Link href="/" className="back-link">← Trang chủ</Link>
          <h2>Lịch sử chat</h2>
        </div>
        <button className="new-chat-btn" onClick={() => setMessages([{ role: "ai", content: "Xin chào! Mình là trợ lý AI tuyển sinh của Đại học CNTT & TT (ICTU). Mình có thể giúp gì cho bạn hôm nay?" }])}> + Đoạn chat mới</button>
        <ul className="history-list">
          {history.map(item => (
            <li key={item.id} className="history-item">
              <span className="icon">💬</span> {item.title}
            </li>
          ))}
        </ul>
      </aside>

      {/* Main Chat Area */}
      <main className="chat-main">
        <header className="chat-header">
          <div className="header-title">
             <div className="status-dot"></div>
             ICTU AI Admission Assistant
          </div>
        </header>

        <div className="messages-container">
          {messages.map((msg, index) => (
            <div key={index} className={`message-wrapper ${msg.role}`}>
              <div className="avatar">{msg.role === 'ai' ? '🤖' : '👩‍🎓'}</div>
              <div className={`message-bubble ${msg.role}`}>
                {msg.content}
              </div>
            </div>
          ))}
          
          {isLoading && (
            <div className="message-wrapper ai">
              <div className="avatar">🤖</div>
              <div className="message-bubble loading">
                <span className="dot"></span>
                <span className="dot"></span>
                <span className="dot"></span>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <div className="input-container">
          <div className="input-box">
            <input 
              type="text" 
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyPress}
              placeholder="Nhập câu hỏi của bạn về tuyển sinh (VD: Điểm chuẩn IT)..."
              disabled={isLoading}
            />
            <button className="send-btn" onClick={handleSend} disabled={isLoading || !input.trim()}>
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
            </button>
          </div>
          <div className="footer-text">
            ICTU AI có thể mắc lỗi. Vui lòng kiểm tra lại thông tin quan trọng.
          </div>
        </div>
      </main>
    </div>
  );
}
