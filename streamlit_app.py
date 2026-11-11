
import streamlit as st
import requests

st.set_page_config(page_title="Customer Churn Prediction", page_icon="📊", layout="wide")
st.title("📊 Customer Churn Prediction")
st.write("Fill in the customer details and click **Predict Churn**.")

API_URL = "http://127.0.0.1:8000/predict"

with st.form("prediction_form"):
    c1, c2 = st.columns(2)

    with c1:
        gender = st.selectbox("Gender", ["Male","Female"], index=None, placeholder="Select gender")
        senior = st.selectbox("Senior Citizen", [0,1], index=None, placeholder="Select")
        partner = st.selectbox("Partner", ["Yes","No"], index=None, placeholder="Select")
        dependents = st.selectbox("Dependents", ["Yes","No"], index=None, placeholder="Select")
        tenure = st.text_input("Tenure", placeholder="Enter tenure")
        phone = st.selectbox("Phone Service", ["Yes","No"], index=None, placeholder="Select")
        multiple = st.selectbox("Multiple Lines", ["Yes","No","No phone service"], index=None, placeholder="Select")
        internet = st.selectbox("Internet Service", ["DSL","Fiber optic","No"], index=None, placeholder="Select")
        security = st.selectbox("Online Security", ["Yes","No","No internet service"], index=None, placeholder="Select")
        backup = st.selectbox("Online Backup", ["Yes","No","No internet service"], index=None, placeholder="Select")

    with c2:
        protection = st.selectbox("Device Protection", ["Yes","No","No internet service"], index=None, placeholder="Select")
        support = st.selectbox("Tech Support", ["Yes","No","No internet service"], index=None, placeholder="Select")
        tv = st.selectbox("Streaming TV", ["Yes","No","No internet service"], index=None, placeholder="Select")
        movies = st.selectbox("Streaming Movies", ["Yes","No","No internet service"], index=None, placeholder="Select")
        contract = st.selectbox("Contract", ["Month-to-month","One year","Two year"], index=None, placeholder="Select")
        billing = st.selectbox("Paperless Billing", ["Yes","No"], index=None, placeholder="Select")
        payment = st.selectbox("Payment Method", ["Electronic check","Mailed check","Bank transfer (automatic)","Credit card (automatic)"], index=None, placeholder="Select")
        monthly = st.text_input("Monthly Charges", placeholder="Enter monthly charges")
        total = st.text_input("Total Charges", placeholder="Enter total charges")

    submit = st.form_submit_button("Predict Churn", use_container_width=True)

if submit:
    try:
        payload = {
            "gender": gender,
            "SeniorCitizen": int(senior),
            "Partner": partner,
            "Dependents": dependents,
            "tenure": int(tenure),
            "PhoneService": phone,
            "MultipleLines": multiple,
            "InternetService": internet,
            "OnlineSecurity": security,
            "OnlineBackup": backup,
            "DeviceProtection": protection,
            "TechSupport": support,
            "StreamingTV": tv,
            "StreamingMovies": movies,
            "Contract": contract,
            "PaperlessBilling": billing,
            "PaymentMethod": payment,
            "MonthlyCharges": float(monthly),
            "TotalCharges": float(total)
        }

        r = requests.post(API_URL, json=payload, timeout=30)

        if r.status_code == 200:
            result = r.json()
            if result["prediction"] == "Churn":
                st.error("⚠️ Customer is likely to Churn")
            else:
                st.success("✅ Customer is likely to Stay (No Churn)")
            st.metric("Prediction", result["prediction"])
            st.metric("Churn Probability", f"{result['churn_probability']}%")
            st.metric("No Churn Probability", f"{result['no_churn_probability']}%")
        else:
            st.error(r.text)

    except ValueError:
        st.error("Please enter valid numeric values.")
    except requests.exceptions.ConnectionError:
        st.error("FastAPI server is not running.")
    except Exception as e:
        st.error(str(e))
