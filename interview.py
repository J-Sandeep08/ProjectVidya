from fastapi import APIRouter, HTTPException,Body
from typing import Annotated
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
import os
import json

# =====================================================
# Router Setup
# =====================================================
router = APIRouter(include_in_schema=False)

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


# =====================================================
# Request Models
# =====================================================

class QuestionRequest(BaseModel):
    category: Literal["Behavioral", "Technical", "Situational"]   # behavioural / technical / situational
    domain: str     # example: "Software Engineer"


class AnswerSubmit(BaseModel):
    question: str
    user_answer: str


# =====================================================
# 1. Generate Practice Questions
# =====================================================

@router.post("/interview/questions")
def generate_questions(
    data: Annotated[QuestionRequest, Body()]
    ):

    prompt = f"""
You are an Interview Preparation Assistant.

Generate 2 interview questions for:

Category: {data.category}
Domain: {data.domain}

Return ONLY JSON like:

[
  {{
    "question_number": 1,
    "question": "Tell me about yourself."
  }},
  {{
    "question_number": 2,
    "question": "Describe a challenge you faced."
  }}
]

Return ONLY JSON.
"""

    response = model.generate_content(prompt)

    try:
        questions = json.loads(response.text)
    except:
        raise HTTPException(status_code=500, detail="Invalid AI JSON output")

    return {
        "message": "Questions generated successfully",
        "questions": questions
    }


# =====================================================
# 2. Submit Answer + Get Feedback
# =====================================================

@router.post("/interview/submit")
def evaluate_answer(
    data: Annotated[AnswerSubmit,Body()]
    ):

    prompt = f"""
You are an AI Interview Evaluator.

Question:
{data.question}

User Answer:
{data.user_answer}

Now provide output ONLY in JSON:

{{
  "correct_answer": "A strong ideal answer example...",
  "ai_feedback": {{
    "strengths": ["Point 1", "Point 2"],
    "suggestions": ["Suggestion 1", "Suggestion 2"]
  }}
}}

Return ONLY JSON.
"""

    response = model.generate_content(prompt)

    try:
        feedback = json.loads(response.text)
    except:
        raise HTTPException(status_code=500, detail="AI response not valid JSON")

    return {
        "message": "Answer evaluated successfully",
        "result": feedback
    }


# =====================================================
# 3. Learning Resources Tab (Simple Hackathon Version)
# =====================================================

@router.get("/interview/resources")
def get_resources():

    resources = [
        {
            "title": "Top 50 Behavioural Interview Questions",
            "url": "https://www.indeed.com/career-advice/interviewing/behavioral-interview-questions"
        },
        {
            "title": "LeetCode Practice for Technical Interviews",
            "url": "https://leetcode.com/"
        },
        {
            "title": "System Design Primer (GitHub)",
            "url": "https://github.com/donnemartin/system-design-primer"
        }
    ]

    return {
        "message": "Resources loaded successfully",
        "resources": resources
    }
