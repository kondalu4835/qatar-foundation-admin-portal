#!/bin/bash

# Qatar Foundation Admin Portal - Startup Script (macOS/Linux)
# This script starts both the backend Flask server and frontend HTTP server

echo ""
echo "============================================"
echo "Qatar Foundation Admin Portal"
echo "============================================"
echo ""

# Check if running from correct directory
if [ ! -d "backend" ]; then
    echo "Error: backend directory not found!"
    echo "Please run this script from the project root directory."
    exit 1
fi

if [ ! -d "frontend" ]; then
    echo "Error: frontend directory not found!"
    echo "Please run this script from the project root directory."
    exit 1
fi

# Create virtual environment and install dependencies if needed
if [ ! -d "backend/.venv" ]; then
    echo "Creating Python virtual environment..."
    cd backend
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -q -r requirements.txt
    cd ..
fi

# Start backend in background
echo "Starting Backend Server (Flask on port 5000)..."
cd backend
source .venv/bin/activate
python app.py &
BACKEND_PID=$!
cd ..

# Wait for backend to start
sleep 3

# Start frontend in background
echo "Starting Frontend Server (HTTP on port 8000)..."
cd frontend
python3 -m http.server 8000 &
FRONTEND_PID=$!
cd ..

# Wait for frontend to start
sleep 2

echo ""
echo "============================================"
echo "Servers Started Successfully!"
echo "============================================"
echo ""
echo "Backend:  http://127.0.0.1:5000"
echo "Frontend: http://localhost:8000"
echo ""
echo "Opening browser..."
sleep 2

# Open browser (macOS)
if [[ "$OSTYPE" == "darwin"* ]]; then
    open http://localhost:8000/login.html
# Open browser (Linux)
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open http://localhost:8000/login.html || echo "Please open http://localhost:8000/login.html in your browser"
fi

echo ""
echo "The application should open in your default browser."
echo "If not, navigate to: http://localhost:8000/login.html"
echo ""
echo "Press Ctrl+C to stop the servers"
echo ""

# Wait for user interrupt
wait
