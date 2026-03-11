import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load local environment if available (.env file)
load_dotenv()
# Try to get API key from Streamlit secrets first (Cloud), fallback to os.getenv (Local)
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except (FileNotFoundError, KeyError):
    api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API Key not found. Please set GOOGLE_API_KEY in Streamlit secrets or .env file.")
    st.stop()
client = genai.Client(api_key=api_key)

# Page settings
st.set_page_config(
    page_title="NovaAI",
    page_icon="🤖",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("🤖 NovaAI")
    st.markdown("Your Personal AI Agent")

    if st.button("Clear Chat"):
        st.session_state.messages = []

    st.markdown("---")
    st.markdown("Model: Gemini 2.5 Flash")

# Title
st.title("🤖 NovaAI Chat")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask anything..."):

    # user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # loading spinner
    with st.spinner("NovaAI is thinking..."):
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        answer = response.text
        

    # AI message
    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})