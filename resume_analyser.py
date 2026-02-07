from fastapi import APIRouter, UploadFile, File, HTTPException
from dotenv import load_dotenv
import google.generativeai as genai
import os

router = APIRouter()

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


# =====================================================
# Resume Upload + Analyze Endpoint
# =====================================================

@router.post("/resume/analyze")
async def analyze_resume(uploaded_file: UploadFile = File(...)):

    # Allow only PDF or DOCX
    if uploaded_file.content_type not in [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]:
        raise HTTPException(status_code=400, detail="Only PDF or DOCX files allowed")

    # Read file bytes
    content = await uploaded_file.read()

    # Temporary simple text extraction
    resume_text = content[:2000].decode("utf-8", errors="ignore")

    # Gemini Prompt
    prompt = f"""
    You are an AI Resume Reviewer.

    Analyze the resume content below and provide:

    1. Strengths
    2. Weaknesses
    3. Suggestions for improvement

    Resume Content:
    {resume_text}
    """

    # Generate AI Response
    response = model.generate_content(prompt)

    return {
        "message": "Resume analyzed successfully",
        "analysis": response.text
    }
