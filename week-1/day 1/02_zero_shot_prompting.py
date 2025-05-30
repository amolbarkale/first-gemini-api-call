import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Zero-shot with temperature and max_tokens
model = genai.GenerativeModel("gemini-2.0-flash-001")
response = model.generate_content(
    "What are the benefits of drinking water?",
    generation_config={
        "temperature": 0.2,
        "max_output_tokens": 100
    }
)

print(response.text)
