from ai_client import generate_text


def summarize_text(text: str, level: str = "beginner") -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Student level: {level}

Summarize the following educational content.

Content:
{text}

Instructions:
- Use simple English.
- Keep the important points.
- Use short paragraphs or bullet points.
- Do not add information that is not present in the content.
"""

    return generate_text(prompt)