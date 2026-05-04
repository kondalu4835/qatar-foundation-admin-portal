@echo off
REM Qatar Foundation Admin Portal - Startup Script
REM This script starts both the backend Flask server and frontend HTTP server

echo.
echo ============================================
echo Qatar Foundation Admin Portal
echo ============================================
echo.

REM Check if running from correct directory
if not exist "backend" (
    echo Error: backend directory not found!
    echo Please run this script from the project root directory.
    pause
    exit /b 1
)

if not exist "frontend" (
    echo Error: frontend directory not found!
    echo Please run this script from the project root directory.
    pause
    exit /b 1
)

REM Start backend in new window
echo Starting Backend Server (Flask on port 5000)...
start "Qatar Foundation - Backend" cmd /k cd backend ^& python -m venv .venv 2>nul ^& .venv\Scripts\activate ^& pip install -q -r requirements.txt 2>nul ^& python app.py

REM Wait for backend to start
timeout /t 3 /nobreak

REM Start frontend in new window
echo Starting Frontend Server (HTTP on port 8000)...
start "Qatar Foundation - Frontend" cmd /k cd frontend ^& python -m http.server 8000

REM Wait for frontend to start
timeout /t 2 /nobreak

echo.
echo ============================================
echo Servers Started Successfully!
echo ============================================
echo.
echo Backend:  http://127.0.0.1:5000
echo Frontend: http://localhost:8000
echo.
echo Opening browser...
timeout /t 2 /nobreak

REM Open browser
start http://localhost:8000/login.html

echo.
echo The application should open in your default browser.
echo If not, navigate to: http://localhost:8000/login.html
echo.
pause
