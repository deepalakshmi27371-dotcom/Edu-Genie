from ai_client import generate_text


def explain_topic(topic: str, level: str = "beginner") -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Student level: {level}

Explain the following topic clearly:

Topic:
{topic}

Instructions:
- Start from the basics.
- Use simple English.
- Explain step by step.
- Give a simple real-world example.
- Use short sections or bullet points.
- Make the explanation easy for a student to understand.
"""

    return generate_text(prompt)