from app.database.db import SessionLocal
from app.database.models import Task, User
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_ai_recommendations(user_id: int):
    db = SessionLocal()
    try:
        tasks = db.query(Task).filter(Task.user_id == user_id).all()
        completed = [
            task.skill_name
            for task in tasks
            if task.status == "completed"
        ]
        pending = [
            task.skill_name
            for task in tasks
            if task.status == "pending"
        ]

        prompt = f"""
        The user has completed skills:
        {completed}

        The user is still learning:
        {pending}

        Give:
        1. Best focus area
        2. Next project idea
        3. Career improvement recommendation

        Return ONLY valid JSON:

        {{
            "focus_area": "",
            "next_project": "",
            "recommendation": ""
        }}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response.choices[0].message.content
        import json
        return json.loads(content)
    finally:
        db.close()