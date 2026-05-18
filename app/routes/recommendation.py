from fastapi import APIRouter, Depends
from app.database.models import User
from app.utils.dependencies import get_current_user
from app.services.recommendation_service import generate_ai_recommendations


router = APIRouter()
@router.get("/ai-recommendations")
def ai_recommendations(
    current_user: User = Depends(get_current_user)
):
    return generate_ai_recommendations(current_user.id)