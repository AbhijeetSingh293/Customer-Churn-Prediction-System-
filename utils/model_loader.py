import pickle

with open("Model/customer_churn_model.pkl", "rb") as f:
    model_data = pickle.load(f)

model = model_data["model"]
feature_names = model_data["features_names"]

with open("Model/encoders.pkl", "rb") as f:
    encoders = pickle.load(f)