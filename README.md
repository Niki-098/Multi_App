# Multi-App AI Suite

A Streamlit-based multi-application platform with a FastAPI backend for AI-powered tools. Users can switch between apps in the sidebar:

Text Summarizer – Upload a document (PDF, TXT, DOCX) and get a concise 3-sentence summary using Google Gemini API.

Expense Tracker – Track your personal expenses (food, rent, travel, etc.) and get weekly/monthly summaries.

AI Q&A Bot – Ask questions and get answers powered by Gemini AI.

Features

Multi-app interface with Streamlit sidebar.

Backend using FastAPI for file processing and API calls.

Gemini AI integration for text summarization and Q&A.

Supports .pdf, .txt, .docx file uploads.

Responsive UI with loading indicators for API calls.

Installation

Clone the repository

git clone https://github.com/YourUsername/Multi_App.git
cd Multi_App


Create virtual environment

python -m venv multi_venv
multi_venv\Scripts\activate  # Windows
# source multi_venv/bin/activate  # macOS/Linux


Install dependencies

pip install -r requirements.txt


Add your Gemini API key in .env file:

GEMINI_API_KEY=your_api_key_here

Usage
1️⃣ Start Backend
cd backend
uvicorn main:app --reload --port 8000

2️⃣ Start Frontend
cd frontend
streamlit run app.py


Open your browser → choose an app from the sidebar → start using it.

Dependencies

Python 3.10+

FastAPI

Streamlit

google-generativeai (Gemini API)

PyPDF2

python-docx

python-dotenv

requests

Notes

Ensure the backend is running before using the frontend.

CORS is enabled in FastAPI for seamless communication.

Summarizer strictly limits output to 3–4 sentences.

Gemini API requires a valid API key configured in .env.
