from src.groq_client import ask_llm

def generate_questions(resume, jd):
    """
    Generates interview questions based on resume + job description
    """

    prompt = f"""
Generate interview questions based on:

Resume:
{resume}

Job Description:
{jd}

Returns:
- 5 HR questions
- 5 Technical questions
- 3 Project-based questions
"""
    
    return ask_llm(prompt)