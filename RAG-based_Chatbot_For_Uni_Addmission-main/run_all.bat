@echo off
echo Starting FastAPI Backend Services...
start cmd /k "%~dp0.venv\Scripts\python.exe -m uvicorn backend_api:app --reload --port 8000"

echo Starting Next.js Frontend Framework...
start cmd /k "cd /d %~dp0frontend && npm run dev"

echo All services are starting up!
echo The web app will be available at: http://localhost:3000
timeout 3 > NUL
start http://localhost:3000
exit
