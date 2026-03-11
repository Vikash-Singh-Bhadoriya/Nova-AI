from dotenv import load_dotenv
import os
from google import genai

# load api key
load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

print("Gemini Agent Ready (type exit to quit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=user_input
    )
    print("Agent:", response.text)  