from fastapi import FastAPI



from routers.home import router as home_router
from routers.health import router as health_router
from routers.prediction import router as prediction_router

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predict whether a customer will churn",
    version="1.0.0"
)

app.include_router(home_router)
app.include_router(health_router)
app.include_router(prediction_router)