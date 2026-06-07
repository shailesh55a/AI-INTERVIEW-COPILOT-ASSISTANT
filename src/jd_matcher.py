from src.groq_client import ask_llm

def match_resume_jd(resume, jd):
    """
    Compares resume with job description using LLM reasoning
    """

    prompt = f"""
Compares Resume vs Job Description.

Resume:
{resume}

job Description:
{jd}

Return:
1. Match Score (0-100)
2. Matching Skills
3. Missing Skills
4. Important Suggestions
"""
    
    return ask_llm(prompt)