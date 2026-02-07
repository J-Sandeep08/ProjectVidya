from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
import google.generativeai as genai
import os
import json

# -------------------------------
# Router setup
# -------------------------------
router = APIRouter()

# -------------------------------
# Load environment variables
# -------------------------------
load_dotenv()

# -------------------------------
# Configure Gemini
# -------------------------------
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


# =====================================================
# Request Model
# =====================================================

class RoadmapRequest(BaseModel):
    current_role: str
    current_level: str
    domain: str
    extracted_skills: List[str]
    preferred_paths: Optional[List[str]] = None
    number_of_alternatives: int = 3


# =====================================================
# Career Roadmap Generator
# =====================================================

@router.post("/roadmap/generate")
def generate_career_roadmap(data: RoadmapRequest):

    prompt = f"""
You are an AI Career Roadmap Generator.

User details:
- Current Role: {data.current_role}
- Current Level: {data.current_level}
- Domain: {data.domain}
- Skills: {data.extracted_skills}
- Preferred Paths: {data.preferred_paths}
- Number of alternative paths required: {data.number_of_alternatives}

Generate:
1. EXACTLY one "current" career path.
2. EXACTLY {data.number_of_alternatives} alternative career paths.

Each path must contain:
- path_type: current / alternative
- title
- stages (3 or 4 stages)

Each stage must contain:
- stage_title
- estimated_time
- skills_required

Return ONLY valid JSON in this format:

{{
  "paths": [
    {{
      "path_type": "current",
      "title": "Your Current Path",
      "stages": [
        {{
          "stage_title": "Junior Developer",
          "estimated_time": "0–6 months",
          "skills_required": ["HTML", "CSS", "JavaScript"]
        }}
      ]
    }},
    {{
      "path_type": "alternative",
      "title": "Frontend Specialist Path",
      "stages": [
        {{
          "stage_title": "Frontend Developer",
          "estimated_time": "0–6 months",
          "skills_required": ["HTML", "CSS", "JavaScript", "React"]
        }}
      ]
    }}
  ]
}}

Return ONLY JSON. No explanations.
"""

    response = model.generate_content(prompt)

    try:
        roadmap = json.loads(response.text)
    except:
        raise HTTPException(
            status_code=500,
            detail="AI response was not valid JSON"
        )

    return {
        "message": "Career roadmap generated successfully",
        "roadmap": roadmap
    }
