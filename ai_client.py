from typing import Any

from google import genai
from google.genai import types

from config import DEMO_MODE, GEMINI_API_KEY, GEMINI_MODEL


client = None

if GEMINI_API_KEY:
    client = genai.Client(api_key=GEMINI_API_KEY)


def generate_text(prompt: str) -> str:
    """Generate a normal text response using Gemini."""

    if DEMO_MODE or client is None:
        return (
            "Demo response: EduGenie is currently running in demo mode. "
            "Add your Gemini API key and set DEMO_MODE=false to use Gemini."
        )

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )

    return response.text or ""


def generate_json(prompt: str, schema: Any) -> Any:
    """Generate structured JSON using Gemini."""

    if DEMO_MODE or client is None:
        return None

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=schema,
        ),
    )

    return response.parsed