from pydantic import BaseModel
from typing import List

from ai_client import generate_json


class LearningStep(BaseModel):
    step: int
    topic: str
    difficulty: str
    description: str
    resources: List[str]


class LearningPath(BaseModel):
    goal: str
    steps: List[LearningStep]


def generate_learning_path(
    goal: str,
    level: str = "beginner"
) -> LearningPath:

    prompt = f"""
Create a personalized learning path.

Learning goal:
{goal}

Student level:
{level}

Requirements:
- Start from beginner level.
- Progress gradually from basic to advanced.
- Include suitable difficulty levels.
- Give a short description for every step.
- Suggest useful learning resources for every step.
- Keep the plan practical and easy to follow.
- Return only structured learning-path data.
"""

    result = generate_json(prompt, LearningPath)

    if result is not None:
        return result

    # Demo mode response
    return LearningPath(
        goal=goal,
        steps=[
            LearningStep(
                step=1,
                topic="Basic Concepts",
                difficulty="Beginner",
                description=f"Learn the basic concepts of {goal}.",
                resources=["Beginner tutorials", "Simple notes"],
            ),
            LearningStep(
                step=2,
                topic="Practice",
                difficulty="Intermediate",
                description=f"Practice important concepts related to {goal}.",
                resources=["Practice exercises", "Small projects"],
            ),
            LearningStep(
                step=3,
                topic="Advanced Concepts",
                difficulty="Advanced",
                description=f"Explore advanced topics in {goal}.",
                resources=["Advanced tutorials", "Project-based learning"],
            ),
        ],
    )