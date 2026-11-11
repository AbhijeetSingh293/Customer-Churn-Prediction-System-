from fastapi import APIRouter, HTTPException

from schemas.customer_schema import CustomerData
from services.prediction_service import predict_customer

router = APIRouter()

@router.post(
    "/predict",
    tags=["Prediction"]
)
def predict(customer: CustomerData):

    try:
        return predict_customer(customer)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )