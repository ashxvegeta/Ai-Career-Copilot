import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()
_client = None


def _get_client() -> OpenAI:
    global _client
    if _client is not None:
        return _client
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Add it to your .env or environment before calling analyze_with_ai."
        )
    _client = OpenAI(api_key=api_key)
    return _client


def analyze_resume_content(resume_text: str):

    prompt = f"""
    Analyze this resume:

    {resume_text}

    Return ONLY valid JSON:

    {{
        "skills": ["skill1", "skill2"],
        "experience_level": "junior/mid/senior",
        "strengths": ["strength1"],
        "weaknesses": ["weakness1"]
    }}
    """

    client = _get_client()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except:
        return {"error": "Invalid JSON", "raw": content}
    


def match_with_job_description(resume: str, job: str):

    prompt = f"""
    Compare resume with job description.

    Resume:
    {resume}

    Job:
    {job}

    Return ONLY valid JSON:

    {{
        "match_score": 0,
        "missing_skills": ["skill1"],
        "suggestions": ["suggestion1"]
    }}
    """

    client = _get_client()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except:
        return {"error": "Invalid JSON", "raw": content}
    
    