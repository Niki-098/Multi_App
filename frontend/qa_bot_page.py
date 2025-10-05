import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def qa_bot_app():
    st.title("🤖 AI Q&A Bot")
    st.write("Ask any question and get an AI-generated answer.")

    question = st.text_area("Your Question:", placeholder="Type your question here...")

    if st.button("Get Answer"):
        if not question.strip():
            st.warning("Please enter a question.")
            return

        with st.spinner("Thinking..."):
            model = genai.GenerativeModel("gemini-2.5-flash")
            response = model.generate_content(question)
            st.subheader("Answer:")
            st.write(response.text)
