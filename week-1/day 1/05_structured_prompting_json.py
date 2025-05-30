import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Structured output with penalties to control repetition
model = genai.GenerativeModel("gemini-2.0-flash-001")

response = model.generate_content(
    "List 3 frontend frameworks in JSON format with their creators.",
    generation_config={
        "frequency_penalty": 1.0,
        "presence_penalty": 0.6,
        "temperature": 0.5,
        "max_output_tokens": 150
    }
)

print(response.text)
