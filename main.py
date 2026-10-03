from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from config import APP_NAME
from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import generate_learning_path


app = FastAPI(
    title=APP_NAME,
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0",
)

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


class TextRequest(BaseModel):
    text: str
    level: str = "beginner"


class QuestionRequest(BaseModel):
    question: str
    level: str = "beginner"


class LearningRequest(BaseModel):
    goal: str
    level: str = "beginner"


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "app_name": APP_NAME,
        },
    )


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "app": APP_NAME,
    }


@app.post("/qa")
async def qa(request: QuestionRequest):
    answer = answer_question(
        request.question,
        request.level,
    )

    return {
        "success": True,
        "answer": answer,
    }


@app.post("/explain")
async def explain(request: TextRequest):
    explanation = explain_topic(
        request.text,
        request.level,
    )

    return {
        "success": True,
        "explanation": explanation,
    }


@app.post("/quiz")
async def quiz(request: TextRequest):
    result = generate_quiz(
        request.text,
        request.level,
    )

    return {
        "success": True,
        "quiz": result.model_dump(),
    }


@app.post("/summarize")
async def summarize(request: TextRequest):
    summary = summarize_text(
        request.text,
        request.level,
    )

    return {
        "success": True,
        "summary": summary,
    }


@app.post("/learn/recommendations")
async def learning_recommendations(request: LearningRequest):
    result = generate_learning_path(
        request.goal,
        request.level,
    )

    return {
        "success": True,
        "learning_path": result.model_dump(),
    }