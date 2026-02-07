from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
import google.generativeai as genai
import os


# -------------------------------
# Router Setup
# -------------------------------
router = APIRouter()

# -------------------------------
# Load Environment Variables
# -------------------------------
load_dotenv()

# -------------------------------
# Configure Gemini API
# -------------------------------
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


# =====================================================
# 1. Sub-Models (Education, Experience, Projects)
# =====================================================

class Education(BaseModel):
    degree: str
    institution: str
    location: str
    gpa: Optional[str] = None
    start_date: str
    end_date: str


class Experience(BaseModel):
    job_title: str
    company: str
    location: str
    start_date: str
    end_date: Optional[str] = None
    description: str


class Project(BaseModel):
    project_name: str
    role: str
    technologies: str
    project_link: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    description: str


# =====================================================
# 2. Main Resume Survey Model (All Fields)
# =====================================================

class ResumeSurvey(BaseModel):

    # -------------------------
    # Personal Details
    # -------------------------
    full_name: str
    email: str
    phone: str
    location: str

    linkedin: Optional[str] = None
    github: Optional[str] = None
    portfolio: Optional[str] = None

    professional_summary: str

    # -------------------------
    # Education (Multiple Entries)
    # -------------------------
    education: List[Education]

    # -------------------------
    # Experience (Multiple Entries)
    # -------------------------
    experience: List[Experience]

    # -------------------------
    # Projects (Multiple Entries)
    # -------------------------
    projects: List[Project]

    # -------------------------
    # Skills Section
    # -------------------------
    technical_skills: str
    frameworks: Optional[str] = None
    tools: Optional[str] = None
    soft_skills: str

    # -------------------------
    # Certificates (Names for now)
    # -------------------------
    certificates: List[str] = []

    # -------------------------
    # Additional Sections
    # -------------------------
    languages: Optional[str] = None
    awards: Optional[str] = None
    publications: Optional[str] = None
    volunteer_work: Optional[str] = None
    interests: Optional[str] = None


# =====================================================
# 3. Resume Generation Endpoint (Gemini AI)
# =====================================================

@router.post("/resume/generate")
def generate_resume(data: ResumeSurvey = Body(...)):

    try:
        # -------------------------
        # Gemini Prompt
        # -------------------------
        prompt = f"""
        You are an AI Resume Builder.

        Create a professional resume in a clean, simple, ATS-friendly format.
        Do not exaggerate. Keep it suitable for students and freshers.

        =====================================================
        PERSONAL DETAILS
        =====================================================
        Name: {data.full_name}
        Email: {data.email}
        Phone: {data.phone}
        Location: {data.location}

        LinkedIn: {data.linkedin}
        GitHub: {data.github}
        Portfolio: {data.portfolio}

        =====================================================
        PROFESSIONAL SUMMARY
        =====================================================

        {data.professional_summary}

        =====================================================
        EDUCATION
        =====================================================

        education_text = "\n".join(
            [f"- {e.degree}, {e.institution}, {e.location} ({e.start_date} - {e.end_date})"
             for e in data.education]
        )

        =====================================================
        EXPERIENCE
        =====================================================
        
        experience_text = "\n".join(
            [f"- {x.job_title} at {x.company}, {x.location}\n  {x.description}"
             for x in data.experience]
        )

        =====================================================
        PROJECTS
        =====================================================
        
        projects_text = "\n".join(
            [f"- {p.project_name} ({p.technologies})\n  {p.description}"
             for p in data.projects]
        )

        =====================================================
        SKILLS
        =====================================================
        Technical Skills: {data.technical_skills}
        Frameworks & Libraries: {data.frameworks}
        Tools & Platforms: {data.tools}
        Soft Skills: {data.soft_skills}

        =====================================================
        CERTIFICATES
        =====================================================
        {data.certificates}

        =====================================================
        ADDITIONAL INFORMATION
        =====================================================
        Languages: {data.languages}
        Awards & Achievements: {data.awards}
        Publications & Research: {data.publications}
        Volunteer Work & Leadership: {data.volunteer_work}
        Interests & Hobbies: {data.interests}

        =====================================================
        Output Rules:
        - Use headings and bullet points.
        - Keep resume length to 1 page if possible.
        - Make it clean and professional.
        """

        # -------------------------
        # Gemini Response
        # -------------------------
        response = model.generate_content(prompt)

        return {
            "message": "Resume generated successfully",
            "resume_text": response.text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Resume generation failed: {str(e)}")
