import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_learning_recommendations(topic: str, level: str = "beginner"):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Create a structured learning roadmap for '{topic}' from beginner to advanced. Include timelines and resources for level {level}."
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"