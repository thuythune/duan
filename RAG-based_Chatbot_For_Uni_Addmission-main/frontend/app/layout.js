import './globals.css';

export const metadata = {
  title: 'ICTU AI Admission Assistant',
  description: 'Trợ lý ảo Tư vấn Tuyển sinh Đại học CNTT & TT (ICTU) ứng dụng AI/RAG',
  icons: {
    icon: '/favicon.ico',
  },
};

export default function RootLayout({ children }) {
  return (
    <html lang="vi">
      <body>
        {children}
      </body>
    </html>
  );
}
