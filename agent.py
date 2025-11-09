# agent.py
"""
Google AI Agent Example
This agent uses the Google Generative AI SDK (Gemini) to analyze or chat with input text.
"""

import google.generativeai as genai

# Configure API key (get one from Google AI Studio)
genai.configure(api_key="YOUR_API_KEY_HERE")

def run_agent(prompt: str):
    """
    The AI agent takes a user prompt and returns a model-generated response.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("🤖 Google AI Agent ready!")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Goodbye!")
            break
        reply = run_agent(user_input)
        print(f"Agent: {reply}")
