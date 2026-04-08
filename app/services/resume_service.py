from app.services.ai_service import (
    analyze_resume_content,
    match_with_job_description
)

def analyze_resume(data):

    resume_text = data.resume_text
    job_desc = data.job_description

    analysis = analyze_resume_content(resume_text)
    job_match = match_with_job_description(resume_text, job_desc)

    return {
        "analysis": analysis,
        "job_match": job_match
    }
