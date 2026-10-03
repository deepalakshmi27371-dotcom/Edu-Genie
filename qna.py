from ai_client import generate_text


def answer_question(question: str, level: str = "beginner") -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Student level: {level}

Answer the following question clearly and accurately:

Question:
{question}

Instructions:
- Use simple English.
- Explain step by step when useful.
- Keep the answer suitable for a student.
- Give a small example when helpful.
"""

    return generate_text(prompt)