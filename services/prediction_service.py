import pandas as pd

from utils.model_loader import model
from utils.model_loader import encoders
from utils.model_loader import feature_names


def predict_customer(customer):

    input_data = pd.DataFrame([customer.model_dump()])

    for column, encoder in encoders.items():
        if column in input_data.columns:
            input_data[column] = encoder.transform(input_data[column])

    input_data = input_data[feature_names]

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    return {
        "prediction": "Churn" if prediction == 1 else "No Churn",
        "prediction_value": int(prediction),
        "churn_probability": round(float(probability[1]) * 100, 2),
        "no_churn_probability": round(float(probability[0]) * 100, 2)
    }