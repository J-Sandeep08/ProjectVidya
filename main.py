from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

#import routers
from auth import router as auth_router
from resume import router as resume_router
from resume_analyser import router as analyzer_router
from skills import router as skills_router
from certifications import router as certifications_router
from interview import router as interview_router
from jobs import router as jobs_router
from dashboard import router as dashboard_router




#Create FastAPI app
app = FastAPI()

#connecting Auth routes
app.include_router(auth_router)
app.include_router(resume_router)
app.include_router(analyzer_router)
app.include_router(skills_router)
app.include_router(certifications_router)
app.include_router(interview_router)
app.include_router(jobs_router)
app.include_router(dashboard_router)




#root test endpoint
@app.get("/")
def root():
    return{"message":"Backend is running"}

#Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
)
