import os
from groq import Groq
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm(prompt: str):
    """
    Sends a prompt to the Groq API and returns the generated response.
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
