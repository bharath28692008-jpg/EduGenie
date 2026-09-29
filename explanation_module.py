import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def explain_topic(topic: str, level: str = "beginner"):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        if level == "beginner":
            prompt = f"Explain '{topic}' in simple terms with everyday analogies for a beginner student."
        elif level == "intermediate":
            prompt = f"Explain '{topic}' in detail with real-world use cases for an intermediate learner."
        else:
            prompt = f"Give an advanced, technical deep-dive explanation of '{topic}' including architecture and math if applicable."

        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)} - Check your GOOGLE_API_KEY in .env"