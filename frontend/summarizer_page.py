import streamlit as st
import requests
import io

BACKEND_URL = "http://127.0.0.1:8000/summarize/"

def summarizer_app():
    st.title("📝 Text Summarizer")
    st.write("Upload a document (PDF, TXT, or DOCX) and get a 3-sentence summary powered by Gemini AI.")

    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "txt", "docx"])

    if uploaded_file is not None:
        st.info(f"**File uploaded:** {uploaded_file.name}")
        if st.button("Summarize"):
            try:
                with st.spinner("Summarizing your document... Please wait"):
                    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                    response = requests.post(BACKEND_URL, files=files)

                    if response.status_code == 200:
                        data = response.json()
                        if "summary" in data:
                            st.success("Summary generated successfully!")
                            st.subheader("📄 Summary:")
                            st.write(data["summary"])
                        else:
                            st.error(data.get("error", "Something went wrong."))
                    else:
                        st.error("Failed to connect to the backend.")
            except Exception as e:
                st.error(f"⚠️ Error: {e}")
