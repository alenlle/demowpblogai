import requests
from config.settings import GROQ_API_KEY

API_URL = "https://api.groq.com/openai/v1/chat/completions"

def ask_groq(prompt):
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not set. Check your environment variables.")

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",  # FIX: updated model name
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(API_URL, json=payload, headers=headers, timeout=60)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
