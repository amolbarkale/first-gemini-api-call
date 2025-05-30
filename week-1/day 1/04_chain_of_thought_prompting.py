import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Chain-of-thought with higher temperature and more tokens
model = genai.GenerativeModel("gemini-2.0-flash-001")

response = model.generate_content(
    "If a train travels 60 km in 1.5 hours, what is its average speed? Explain the steps.",
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 200
    }
)

print(response.text)
