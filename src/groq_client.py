import os
from groq import Groq
from dotenv import load_dotenv

# Load api key from .env file
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm(prompt: str):
    """
    Sends prompt to Groq LLM (Llama 3.3) and returns response text
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", # powerful general-purpose model
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7 # controls randomness of output
    )

    # Extract model response text
    return response.choices[0].message.content