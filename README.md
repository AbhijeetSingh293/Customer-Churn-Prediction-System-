# Customer Churn Prediction System

An end-to-end Machine Learning application that predicts whether a customer is likely to leave a company (churn). The project uses multiple ML algorithms and provides predictions through a FastAPI backend and an interactive Streamlit frontend.

## Project Overview

Customer churn is a major challenge for businesses because losing existing customers affects revenue and growth.

This project analyzes customer data and predicts the likelihood of customer churn using Machine Learning models. It helps businesses identify customers who may leave and take preventive actions to improve customer retention.

## Features

- Customer churn prediction using Machine Learning.
- Multiple ML models: Decision Tree, Random Forest, and XGBoost.
- Handles imbalanced datasets using SMOTE.
- FastAPI backend for prediction APIs.
- Interactive Streamlit frontend.
- Pre-trained model integration.
- REST API documentation using Swagger UI.

## Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn, XGBoost |
| Data Processing | Pandas, NumPy |
| Data Visualization | Matplotlib |
| Imbalanced Data Handling | SMOTE |
| Backend | FastAPI |
| Frontend | Streamlit |
| API Server | Uvicorn |

## Project Structure

```text
CHURN_PRED_BY_FastAPI/
│
├── Model/              # Trained ML models
├── routers/            # API route definitions
├── schemas/            # Request and response schemas
├── services/           # Prediction and business logic
├── utils/              # Utility functions
│
├── app.py              # FastAPI application
├── streamlit_app.py    # Streamlit frontend
├── requirements.txt    # Project dependencies
├── Dockerfile          # Docker configuration
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/AbhijeetSingh293/Customer-Churn-Prediction-System-.git
```

### 2. Navigate to the Project Directory

```bash
cd Customer-Churn-Prediction-System-
```

### 3. Create a Virtual Environment

```bash
python -m venv myenv
```

### 4. Activate Virtual Environment

**Windows PowerShell:**

```powershell
.\myenv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

The application requires two separate terminals.

### Terminal 1: Start FastAPI Backend

```bash
uvicorn app:app --reload
```

Backend URL:

http://127.0.0.1:8000

API Documentation (Swagger UI):

http://127.0.0.1:8000/docs

### Terminal 2: Start Streamlit Frontend

Activate the virtual environment and run:

```bash
streamlit run streamlit_app.py
```

Frontend URL:

http://localhost:8501

## Machine Learning Workflow

1. Load and explore the customer dataset.
2. Perform data cleaning and preprocessing.
3. Handle class imbalance using SMOTE.
4. Train multiple Machine Learning models.
5. Evaluate and compare model performance.
6. Save the trained models.
7. Integrate the models with FastAPI.
8. Generate predictions through the Streamlit interface.

## How It Works

1. The user enters customer details through the Streamlit interface.
2. The frontend sends the input data to the FastAPI backend.
3. The backend processes the input and loads the trained ML model.
4. The model predicts whether the customer is likely to churn.
5. The prediction result is returned and displayed on the frontend.

## Future Improvements

- Add model performance comparison dashboards.
- Improve prediction accuracy through hyperparameter tuning.
- Deploy the application on a cloud platform.
- Add customer retention recommendations.
- Implement real-time prediction monitoring.

## Author

**Abhijeet Kumar Singh**

B.Tech – Computer Science and Engineering (AI & ML)  
Sikkim Manipal Institute of Technology

- GitHub: [AbhijeetSingh293](https://github.com/AbhijeetSingh293)

---

⭐ If you find this project useful, consider giving it a star!
