from pydantic import BaseModel
from typing import List

from ai_client import generate_json


class QuizQuestion(BaseModel):
    question: str
    options: List[str]
    correct_answer: str
    explanation: str


class Quiz(BaseModel):
    questions: List[QuizQuestion]


def generate_quiz(topic: str, level: str = "beginner") -> Quiz:
    prompt = f"""
Create a short educational multiple-choice quiz.

Topic:
{topic}

Student level:
{level}

Requirements:
- Create exactly 3 questions.
- Each question must have exactly 4 options.
- Each question must have one correct answer.
- Add a short explanation for the correct answer.
- Keep the questions suitable for the student's level.
- Return only structured quiz data.
"""

    result = generate_json(prompt, Quiz)

    if result is not None:
        return result

    # Demo mode response
    return Quiz(
        questions=[
            QuizQuestion(
                question=f"What is the main purpose of studying {topic}?",
                options=[
                    "To understand the topic",
                    "To avoid learning",
                    "To stop practicing",
                    "None of these",
                ],
                correct_answer="To understand the topic",
                explanation="Learning helps us understand and use the topic.",
            ),
            QuizQuestion(
                question=f"Which approach is useful when learning {topic}?",
                options=[
                    "Practice regularly",
                    "Never practice",
                    "Ignore examples",
                    "Avoid questions",
                ],
                correct_answer="Practice regularly",
                explanation="Regular practice improves understanding.",
            ),
            QuizQuestion(
                question=f"What can help a student learn {topic} better?",
                options=[
                    "Examples and practice",
                    "Skipping all lessons",
                    "Avoiding revision",
                    "Not asking questions",
                ],
                correct_answer="Examples and practice",
                explanation="Examples and practice make learning easier.",
            ),
        ]
    )