# Nova AI

A simple, fast AI chat agent built with Python, Streamlit, and the Groq API. Originally built to understand the fundamentals of AI agents and large language models outside of my usual Android development stack.

**Live App:** [https://nova-ai-0.streamlit.app/](https://nova-ai-0.streamlit.app/)

## Screenshots
*(Add your screenshots here by replacing the placeholders)*
![Nova AI Chat Interface](screenshot1.png)

## Tech Stack
*   **Frontend:** Streamlit
*   **Backend:** Python
*   **LLM API:** Groq (Llama 3.3 70B)
*   **Memory:** Custom agent architecture to retain conversation history

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Vikash-Singh-Bhadoriya/Nova-AI.git
   cd Nova-AI
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your Groq API key:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```