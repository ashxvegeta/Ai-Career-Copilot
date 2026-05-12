# used to connect to the database
from multiprocessing import process

from app.database.db import SessionLocal
# → database model/table
from app.database.models import Task


def get_dashboard_data(user_id: int):

    db = SessionLocal()

    try:
        tasks = db.query(Task).filter(Task.user_id == user_id).all()
        total_tasks = len(tasks)
        completed_tasks = len([task for task in tasks if task.status == "completed"])
        pending_tasks = total_tasks - completed_tasks
        process_percentage = (
            (completed_tasks/total_tasks) *100 if total_tasks > 0 else 0
        )
        # get top skills

        skills = {}
        for task in tasks:
            skill  = task.skill_name
            if skill not in skills:
                skills[skill] = 0
            skills[skill] += 1
        top_skills = list(skills.keys())

        return {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "process_percentage": process_percentage,
            "top_skills": top_skills
        }

    finally:
        db.close()