# Multi-App AI Suite

A Streamlit-based multi-application platform with a FastAPI backend for AI-powered tools. Users can switch between apps in the sidebar:<br>

**Text Summarizer –** Upload a document (PDF, TXT, DOCX) and get a concise 3-sentence summary using Google Gemini API.<br>

**Expense Tracker –** Track your personal expenses (food, rent, travel, etc.) and get weekly/monthly summaries.<br>

**AI Q&A Bot –** Ask questions and get answers powered by Gemini AI.<br>

## Features

Multi-app interface with Streamlit sidebar.<br>

Backend using FastAPI for file processing and API calls.<br>

Gemini AI integration for text summarization and Q&A.<br>

Supports .pdf, .txt, .docx file uploads.<br>

Responsive UI with loading indicators for API calls.<br>

## Installation

Clone the repository<br>

*git clone https://github.com/Niki-098/Multi_App<br>
cd Multi_App*


## Create virtual environment

*python -m venv multi_venv
multi_venv\Scripts\activate  # Windows<br>
 source multi_venv/bin/activate   macOS/Linux*


## Install dependencies

*pip install -r requirements.txt*<br>


Add your Gemini API key in .env file:

*GEMINI_API_KEY=your_api_key_here*

## Usage
1️. Start Backend<br>
cd backend<br>
uvicorn main:app --reload --port 8000<br><br>

2️. Start Frontend
cd frontend<br>
streamlit run app.py<br><br>


Open your browser → choose an app from the sidebar → start using it.

## Dependencies

Python 3.10+<br>
FastAPI<br>
Streamlit<br>
google-generativeai (Gemini API)<br>
PyPDF2<br>
python-docx<br>
python-dotenv<br>



## Notes
Ensure the backend is running before using the frontend.<br>
CORS is enabled in FastAPI for seamless communication.<br>
Summarizer strictly limits output to 3–4 sentences.<br>
Gemini API requires a valid API key configured in .env.
