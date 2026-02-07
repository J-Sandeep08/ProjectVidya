from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

# =====================================================
# Request Model
# =====================================================

class DashboardRequest(BaseModel):
    # From resume analysis
    extracted_skills: List[str]

    # From job recommendation result
    jobs_matched: int

    # Flags for profile completion
    has_resume: bool
    has_projects: bool
    has_experience: bool
    has_certifications: bool


# =====================================================
# Dashboard Summary Endpoint
# =====================================================

@router.post("/dashboard/summary")
def dashboard_summary(data: DashboardRequest):

    # -------------------------
    # Profile Completion Logic
    # -------------------------
    completed_sections = sum([
        data.has_resume,
        data.has_projects,
        data.has_experience,
        data.has_certifications
    ])

    total_sections = 4
    profile_completion = int((completed_sections / total_sections) * 100)

    # -------------------------
    # Skills Assessed
    # -------------------------
    skills_assessed = len(data.extracted_skills)

    # -------------------------
    # Jobs Matched
    # -------------------------
    jobs_matched = data.jobs_matched

    return {
        "profile_completion": profile_completion,   # percentage
        "skills_assessed": skills_assessed,          # number
        "jobs_matched": jobs_matched                 # number
    }
