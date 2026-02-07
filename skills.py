from fastapi import APIRouter,UploadFile,File, HTTPException
from dotenv import load_dotenv


import google.generativeai as genai
import os
import json

#Router setup
router = APIRouter()

#Load new variables
load_dotenv()

#Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

#Skill Assessment Endpoint

@router.post("/skills/assess")
async def skill_assessment(file: UploadFile = File(...)):

    #Allow only PDF/DOCX
    if file.content_type not in [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]:
        raise HTTPException(status_code=400, detail="Only PDF or DOCX allowed")
    
    #Read file bytes
    content = await file.read()

    #Temporary extraction (prototype)
    resume_text = content[:2000].decode("utf-8", errors="ignore")

    #Gemini Prompt for Structured skill output
    prompt = f"""
    You are an AI Skill Assessment Engine.

    From the resume below, extract:

    1. Total number of skills
    2. High demand skills (top 3)
    3. Average proficiency %

    Then return structured output in JSON format like this:

    {{
      "total_skills": 8,
      "high_demand_skills": ["JavaScript", "React", "SQL"],
      "average_proficiency": 72,

      "technical_skills": [
        {{
          "name": "JavaScript",
          "category": "Programming",
          "demand": "High Demand",
          "level": "Expert",
          "percentage": 85
        }},
        {{
          "name": "SQL",
          "category": "Database",
          "demand": "Medium Demand",
          "level": "Intermediate",
          "percentage": 60
        }}
      ],

      "soft_skills": [
        {{
          "name": "Communication",
          "level": "Expert",
          "percentage": 88
        }}
      ],

      "recommendations": [
        "Learn Cloud Computing (AWS)",
        "Improve Data Structures and Algorithms"
      ]
    }}

    Resume Content:
    {resume_text}

    Return ONLY valid JSON.
    """

    #Generate response
    response = model.generate_content(prompt)

    #Convert AI text -> JSON
    try:
        skills_data = json.loads(response.text)
    except:
        raise HTTPException(
            status_code=500,
            detail="AI response was not valid JSON"
        )

    return {
        "message": "Skill Assessment Completed",
        "skills_report": skills_data
    }