"use client";

import { useState, useRef, useEffect } from "react";

export default function Chatbot() {
  const [messages, setMessages] = useState([
    { role: "ai", content: "Xin chào! Mình là trợ lý AI tuyển sinh của Đại học CNTT & TT. Mình có thể giúp gì cho bạn hôm nay?" }
  ]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  // Cuộn xuống dòng cuối khi có tin nhắn mới
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
    <div className="chat-wrapper">
      <div className="chat-header">
        <h1>ICTU AI Admission Assistant</h1>
      </div>
      
      <div className="messages-container">
        {messages.map((msg, index) => (
          <div key={index} className={`message-bubble ${msg.role === "user" ? "message-user" : "message-ai"}`}>
            {msg.content}
          </div>
        ))}
        {isLoading && (
          <div className="message-bubble message-ai">
            <div className="loading-dots">
              <div className="dot"></div>
              <div className="dot"></div>
              <div className="dot"></div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="input-area">
        <input 
          type="text" 
          className="chat-input"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyPress}
          placeholder="Nhập câu hỏi của bạn về tuyển sinh..."
          disabled={isLoading}
        />
        <button 
          className="send-button"
          onClick={handleSend}
          disabled={isLoading || !input.trim()}
        >
          Gửi
        </button>
      </div>
    </div>
  );
}
