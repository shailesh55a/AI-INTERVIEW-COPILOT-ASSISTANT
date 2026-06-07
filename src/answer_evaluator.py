from src.groq_client import ask_llm

def evaluate_answer(question, answer):
    """
    Evaluates candidate answer like an interviewer
    """

    prompt = f"""
You are an expert interviewer.

Question: {question}

candidate Answer: {answer}

Evaluate on:
1. Technical Accuracy (0-10)
2. Communication (0-10)
3. Confidence (0-10)
4. Relevance (0-10)

Return:
- Total Score out of 40
- Detailed Feedback
"""
    
    return ask_llm(prompt)