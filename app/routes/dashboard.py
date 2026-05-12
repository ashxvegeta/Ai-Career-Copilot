from fastapi import APIRouter, Depends
from app.utils.dependencies import get_current_user
from app.services.dashboard_service import get_dashboard_data
from app.database.models import User

router = APIRouter()

@router.get("/dashboard")
def dashboard(
    current_user: User = Depends(get_current_user)
):
    return get_dashboard_data(current_user.id)