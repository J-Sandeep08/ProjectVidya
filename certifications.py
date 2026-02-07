from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
import google.generativeai as genai
import os
import json

# =====================================================
# Router Setup
# =====================================================
router = APIRouter()

# =====================================================
# Load Environment Variables
# =====================================================
load_dotenv()

# =====================================================
# Configure Gemini API
# =====================================================
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


# =====================================================
# Temporary Database (Prototype)
# =====================================================
earned_certifications_db = []


# =====================================================
# Certification Models
# =====================================================

class EarnedCertification(BaseModel):
    name: str
    date_earned: str
    expiry: Optional[str] = None
    credential_id: Optional[str] = None


class CertificationDashboard(BaseModel):
    earned_count: int
    in_progress_count: int
    recommended_count: int


# =====================================================
# 1. Add Earned Certification
# =====================================================

@router.post("/certifications/earned/add")
def add_earned_certification(cert: EarnedCertification = Body(...)):

    earned_certifications_db.append(cert.dict())

    return {
        "message": "Certification added successfully",
        "earned_certifications": earned_certifications_db
    }


# =====================================================
# 2. View Earned Certifications
# =====================================================

@router.get("/certifications/earned")
def get_earned_certifications():
    return {
        "earned_certifications": earned_certifications_db
    }


# =====================================================
# 3. Get Recommended Certifications (AI)
# =====================================================

class RecommendationRequest(BaseModel):
    career_domain: str


@router.post("/certifications/recommended")
def recommend_certifications(data: RecommendationRequest = Body(...)):

    prompt = f"""
You are an AI Career Certification Advisor.

Suggest 5 certifications for someone pursuing:

Career Domain: {data.career_domain}

For each certification, return:

- name
- duration
- relevance
- official_url (must be a real official company certification page)

Return output ONLY in valid JSON format like:

[
  {{
    "name": "AWS Solutions Architect Associate",
    "duration": "2 months",
    "relevance": "85%",
    "official_url": "https://aws.amazon.com/certification/"
  }},
  {{
    "name": "Google Cloud Professional Architect",
    "duration": "3 months",
    "relevance": "70%",
    "official_url": "https://cloud.google.com/certification"
  }}
]

Return ONLY JSON. No extra explanation.
"""

    response = model.generate_content(prompt)

    try:
        recommended = json.loads(response.text)
    except:
        raise HTTPException(
            status_code=500,
            detail="AI response not valid JSON"
        )

    return {
        "message": "Recommended certifications generated successfully",
        "recommended_certifications": recommended
    }
