from fastapi import APIRouter, status

from utils.model_loader import model
from utils.model_loader import encoders

router = APIRouter()

@router.get(
    "/health",
    tags=["Health Check"],
    status_code=status.HTTP_200_OK
)
def health():

    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "encoders_loaded": encoders is not None
    }