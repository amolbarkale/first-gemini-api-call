import os
from dotenv import load_dotenv
import google.generativeai as genai

def main():
    # Load API key from .env file
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in .env")
        return

    # Configure Gemini API
    genai.configure(api_key=api_key)

    # Initialize Gemini model
    model = genai.GenerativeModel("gemini-2.0-flash-001")

    # Set system prompt (fixed)
    system_prompt = "You are a helpful assistant who answers questions clearly and politely."

    # Get user prompt from input
    user_input = input("Enter your question: ")

    # Combine system + user prompt
    full_prompt = f"{system_prompt}\nUser: {user_input}"

    # Generate response with token tracking
    response = model.generate_content(full_prompt)

    # Output response and token usage
    print("\nAssistant:", response.text)
    print("\n[Token Usage Not Available in Gemini API Yet]")

if __name__ == "__main__":
    main()
