import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load local environment if available (.env file)
load_dotenv()

# Try to get API key from Streamlit secrets first (Cloud), fallback to os.getenv (Local)
try:
    api_key = st.secrets["GROQ_API_KEY"]
except (FileNotFoundError, KeyError):
    api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("API Key not found. Please set GROQ_API_KEY in Streamlit secrets or .env file.")
    st.stop()

# Initialize Groq client
client = Groq(api_key=api_key)

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
    st.markdown("Model: Llama 3.3 70B (via Groq)")

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
        # Use Groq to generate the response
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are NovaAI, a helpful personal AI agent."
                },
                # Pass the conversation history
                *[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
            ],
            model="llama-3.3-70b-versatile",
        )
        
        answer = chat_completion.choices[0].message.content

    # AI message
    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
