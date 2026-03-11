import streamlit as st
import os
from google import genai

# API key from Streamlit secrets
client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

st.title("Nova AI")

user_input = st.chat_input("Ask something")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=user_input
    )

    with st.chat_message("assistant"):
        st.write(response.text)