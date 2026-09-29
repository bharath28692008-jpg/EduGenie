import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_quiz(topic: str, num_questions: int = 5):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Generate {num_questions} MCQs on '{topic}' with 4 options and correct answer with explanation. Format as JSON."
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"