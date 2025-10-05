from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import docx

load_dotenv()  

app = FastAPI()

#Allow CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@app.get("/")
def root():
    return {"message": "Backend is running successfully!"}

@app.post("/summarize/")
async def summarize_file(file: UploadFile):
    text = ""
    if file.filename.endswith(".pdf"):
        pdf = PdfReader(file.file)
        for page in pdf.pages:
            text += page.extract_text() or ""
    elif file.filename.endswith(".txt"):
        text = (await file.read()).decode("utf-8")
    elif file.filename.endswith(".docx"):
        doc = docx.Document(file.file)
        text = "\n".join([p.text for p in doc.paragraphs])
    else:
        return {"error": "Unsupported file format."}

    if not text.strip():
        return {"error": "No text found in the file."}

    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = (
        "You are a precise summarization assistant. "
        "Your task is to summarize the given text in **exactly 3 sentences**. "
        "Never exceed 3 sentences unless absolutely necessary — 4 at maximum. "
        "Each sentence must be concise, information-dense, and avoid repetition. "
        "Do not include any introductory or concluding phrases like 'In summary' or 'The text discusses'. "
        "Output only the summary sentences, nothing else.\n\n"
        f"Text:\n{text}"
    )

    response = model.generate_content(prompt)
    summary = response.text.strip()
    return {"summary": summary}
