# SecureScan: Advanced Fraud Detection System

SecureScan is a comprehensive machine learning project for detecting fraudulent financial transactions. It combines robust data analysis, state-of-the-art modeling, and an interactive web application to help users and organizations identify and prevent fraud in real time.

## Features

- **End-to-End Fraud Detection Pipeline:** From data exploration and feature engineering to model training and evaluation.
- **Multiple ML Models:** Logistic Regression, Random Forest, XGBoost, and LightGBM, with XGBoost as the deployed model.
- **Interactive Streamlit App:** User-friendly web interface for analyzing transactions and visualizing fraud risk.
- **Custom UI/UX:** Modern, responsive design with clear risk indicators and actionable recommendations.
- **Example Transactions:** Quickly test the system with built-in transaction scenarios.
- **High Accuracy:** Achieves over 99% accuracy and AUC on the provided dataset.

## Demo

![SecureScan UI Screenshot](#) <!-- Add a screenshot or GIF if available -->

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/BIA_capstone.git
cd BIA_capstone
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Prepare the Data

Ensure the dataset file `Fraud_Analysis_Dataset(in).csv` is present in the project directory.

### 4. Train the Model (Optional)

To retrain the model or experiment with different algorithms, run the Jupyter notebook:

```bash
jupyter notebook fraud_detection.ipynb
```

This notebook covers:
- Data exploration and visualization
- Feature engineering
- Model training and evaluation
- Exporting the trained XGBoost model as `xgboost_fraud_model.pkl`

### 5. Launch the Streamlit App

Start the web application:

```bash
streamlit run fraud.py
```

Open the provided local URL in your browser to interact with SecureScan.

## Project Structure

```
.
├── fraud.py                      # Streamlit web app
├── fraud_detection.ipynb         # Data analysis & model training notebook
├── xgboost_fraud_model.pkl       # Trained XGBoost model
├── requirements.txt              # Python dependencies
├── Fraud_Analysis_Dataset(in).csv# Transaction dataset
├── Fraud Detection in Mobile.pdf # Project report (optional)
├── Fraud Detection in Mobile.pptx# Project presentation (optional)
├── fraud_detection.pbix          # Power BI dashboard (optional)
└── ...
```

## Dataset

- **Source:** `Fraud_Analysis_Dataset(in).csv`
- **Rows:** 11,142
- **Features:** step, type, amount, nameOrig, oldbalanceOrg, newbalanceOrig, nameDest, oldbalanceDest, newbalanceDest, isFraud

## Model Performance

| Model               | Accuracy | AUC    |
|---------------------|----------|--------|
| Logistic Regression | 95.6%    | 0.987  |
| Random Forest       | 99.6%    | 0.995  |
| XGBoost             | 99.7%    | 0.998  |
| LightGBM            | 99.7%    | 0.999  |

## Requirements

- Python 3.7+
- See `requirements.txt` for all dependencies:
  - pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost, lightgbm, joblib, streamlit

## Usage

- Enter transaction details in the app to analyze fraud risk.
- Use example transactions for quick testing.
- The app displays fraud probability, risk level, and recommendations.

## Screenshots

<!-- Add screenshots or GIFs here if available -->

## License

[MIT License](LICENSE) <!-- Update if you use a different license -->

## Acknowledgments

- Inspired by real-world financial fraud detection challenges.
- Built with open-source tools and libraries. 