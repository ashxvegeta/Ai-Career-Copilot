from fastapi import APIRouter
from app.schemas.career_schema import ResumeInput
from app.services.resume_service import analyze_resume

router = APIRouter()
@router.post("/career/analyze")
def analyze(data: ResumeInput):
    return analyze_resume(data)
