import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Few-shot with stop sequence
model = genai.GenerativeModel("gemini-2.0-flash-001")
prompt = """Translate to Spanish:
Dog -> Perro
Cat -> Gato
Bird ->"""

response = model.generate_content(
    prompt,
    generation_config={
        "stop_sequences": ["\n"],
        "temperature": 0.3
    }
)

print(response.text)
