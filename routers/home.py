from fastapi import APIRouter

router = APIRouter()

@router.get(
    "/",
    tags=["Home"]
)
def home():

    return {
        "message": "Customer Churn Prediction API is running!"
    }