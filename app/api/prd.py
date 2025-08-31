from fastapi import APIRouter
from app.models import PRDRequest, PRDResponse
from app.services.prd_service import generate_prd

router = APIRouter()

@router.post("/generate", response_model=PRDResponse)
def generate_prd_endpoint(request: PRDRequest):
    """
    Generate a PRD from user input (vision, goals, audience, etc.).
    """
    prd_content = generate_prd(request)
    return PRDResponse(content=prd_content)
