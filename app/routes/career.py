from fastapi import FastAPI
from app.schemas.career_schema import ResumeInput
from app.services.ai_service import analyze_with_ai

router = FastAPI()
@router.post("/career/analyze")
def analyze(data: ResumeInput):
    result = analyze_with_ai(
        data.resume_text,
        data.job_description
    )
    return {
        "result": result
    }