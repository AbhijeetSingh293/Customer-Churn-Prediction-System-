from pydantic import BaseModel, Field, field_validator
from typing import Literal

class CustomerData(BaseModel):

    gender: Literal["Male", "Female"] = Field(...)

    SeniorCitizen: Literal[0, 1] = Field(...)

    Partner: Literal["Yes", "No"] = Field(...)

    Dependents: Literal["Yes", "No"] = Field(...)

    tenure: int = Field(..., ge=0, le=72)

    PhoneService: Literal["Yes", "No"] = Field(...)

    MultipleLines: Literal[
        "Yes",
        "No",
        "No phone service"
    ] = Field(...)

    InternetService: Literal[
        "DSL",
        "Fiber optic",
        "No"
    ] = Field(...)

    OnlineSecurity: Literal[
        "Yes",
        "No",
        "No internet service"
    ] = Field(...)

    OnlineBackup: Literal[
        "Yes",
        "No",
        "No internet service"
    ] = Field(...)

    DeviceProtection: Literal[
        "Yes",
        "No",
        "No internet service"
    ] = Field(...)

    TechSupport: Literal[
        "Yes",
        "No",
        "No internet service"
    ] = Field(...)

    StreamingTV: Literal[
        "Yes",
        "No",
        "No internet service"
    ] = Field(...)

    StreamingMovies: Literal[
        "Yes",
        "No",
        "No internet service"
    ] = Field(...)

    Contract: Literal[
        "Month-to-month",
        "One year",
        "Two year"
    ] = Field(...)

    PaperlessBilling: Literal[
        "Yes",
        "No"
    ] = Field(...)

    PaymentMethod: Literal[
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ] = Field(...)

    MonthlyCharges: float = Field(..., gt=0)

    TotalCharges: float = Field(..., ge=0)
    

    # ----------------------------
    # Custom Validators
    # ----------------------------
    
    @field_validator("tenure")
    @classmethod
    def validate_tenure(cls, value):
        if value < 0:
            raise ValueError("Tenure cannot be negative.")
        if value > 72:
            raise ValueError("Tenure cannot exceed 72 months.")
        return value

    @field_validator("MonthlyCharges")
    @classmethod
    def validate_monthly_charges(cls, value):
        if value <= 0:
            raise ValueError("MonthlyCharges must be greater than 0.")
        return value

    @field_validator("TotalCharges")
    @classmethod
    def validate_total_charges(cls, value):
        if value < 0:
            raise ValueError("TotalCharges cannot be negative.")
        return value

    @field_validator("gender", "Partner", "Dependents", mode="before")
    @classmethod
    def strip_spaces(cls, value):
        if isinstance(value, str):
            return value.strip()
        return value