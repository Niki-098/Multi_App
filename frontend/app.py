import streamlit as st
from summarizer_page import summarizer_app
from expense_tracker_page import expense_tracker_app
from qa_bot_page import qa_bot_app

st.set_page_config(page_title="Multi-App AI", page_icon="", layout="wide")

st.sidebar.title("AI Multi-App")
app_choice = st.sidebar.radio(
    "Choose an App:",
    ["📝 Text Summarizer", "💰 Expense Tracker", "💬 AI Q&A Bot"]
)

if app_choice == "📝 Text Summarizer":
    summarizer_app()
elif app_choice == "💰 Expense Tracker":
    expense_tracker_app()
elif app_choice == "💬 AI Q&A Bot":
    qa_bot_app()
