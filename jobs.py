from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
import google.generativeai as genai
import os
import json

# -------------------------------
# Router setup
# -------------------------------
router = APIRouter()

# -------------------------------
# Load env & configure Gemini
# -------------------------------
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


# =====================================================
# Request Models
# =====================================================

class JobRequest(BaseModel):
    resume_skills: List[str]
    interests: List[str]
    domain: str


class JobAnalysisRequest(BaseModel):
    job_title: str
    resume_skills: List[str]


# =====================================================
# 1. Job Recommendations
# =====================================================

@router.post("/jobs/recommend")
def recommend_jobs(data: JobRequest):

    prompt = f"""
You are an AI Job Recommendation Engine.

User profile:
- Skills: {data.resume_skills}
- Interests: {data.interests}
- Domain: {data.domain}

Generate 5 personalized job recommendations.

IMPORTANT:
- Do NOT include location
- Companies must be EXAMPLES of well-known companies
  that usually hire for the given role
- Use 1 or 2 company names per job

Each job must contain:
- job_title
- companies (array of example company names)
- job_type (Full-time or Part-time)
- estimated_salary
- match_percentage
- short_description

Return ONLY valid JSON like:

[
  {{
    "job_title": "Senior Software Engineer",
    "companies": ["Google", "Microsoft"],
    "job_type": "Full-time",
    "estimated_salary": "$120,000 - $160,000",
    "match_percentage": 92,
    "description": "Build scalable web applications using modern technologies."
  }},
  {{
    "job_title": "Frontend Developer",
    "companies": ["Meta", "Shopify"],
    "job_type": "Full-time",
    "estimated_salary": "$90,000 - $120,000",
    "match_percentage": 88,
    "description": "Create responsive and accessible user interfaces."
  }}
]

Return ONLY JSON.
"""

    response = model.generate_content(prompt)

    try:
        jobs = json.loads(response.text)
    except:
        raise HTTPException(
            status_code=500,
            detail="AI response was not valid JSON"
        )

    return {
        "message": "Job recommendations generated successfully",
        "jobs": jobs
    }
