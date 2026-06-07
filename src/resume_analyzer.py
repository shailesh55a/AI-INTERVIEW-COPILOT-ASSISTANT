from src.groq_client import ask_llm

def analyze_resume(text):
    """
    Uses LLM to analyze resume structure and content
    """

    prompt = f"""
You are an expert recruiter.

Analyze the following resume:

{text}

Return structured output:
1. Key Skills
2. Projects
3. Strengths
4. Weaknesses
5. Suitable job Roles
"""
    
    return ask_llm(prompt)