import streamlit as st
import os
from groq import Groq

# Use Streamlit secrets if available, else use local env variable
api_key = st.secrets["GROQ_API_KEY"] if "GROQ_API_KEY" in st.secrets else os.getenv("GROQ_API_KEY")

# Initialize the Groq client
client = Groq(api_key=api_key)

st.title("Nova AI (Agent)")

user_input = st.chat_input("Ask something")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    # Use Groq to generate a response
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": user_input}],
        model="llama-3.3-70b-versatile",
    )

    response_text = chat_completion.choices[0].message.content

    with st.chat_message("assistant"):
        st.write(response_text)