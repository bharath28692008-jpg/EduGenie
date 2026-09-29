import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def summarize_text(text: str, style: str = "concise"):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Summarize this in {style} style: {text}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"