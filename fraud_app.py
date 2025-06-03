# Step 1: Load the saved model
import joblib
import pandas as pd
import gradio as gr

model = joblib.load('xgboost_fraud_model.pkl')  # Replace with your model filename

# Step 2: Define the prediction function
def predict_fraud(type, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, balancedifforg, balancediffdest):
    input_df = pd.DataFrame([{
        'type': type,
        'amount': float(amount),
        'oldbalanceOrg': float(oldbalanceOrg),
        'newbalanceOrig': float(newbalanceOrig),
        'oldbalanceDest': float(oldbalanceDest),
        'newbalanceDest': float(newbalanceDest),
        'balancedifforg': float(balancedifforg),
        'balancediffdest': float(balancediffdest)
    }])
    
    prediction = model.predict(input_df)[0]
    return "Fraud" if prediction == 1 else "Not Fraud"




iface = gr.Interface(
    fn=predict_fraud,
    inputs=[
        gr.Dropdown(['TRANSFER', 'CASH_OUT', 'PAYMENT', 'DEBIT', 'CASH_IN'], label="Transaction Type"),
        gr.Number(label="Amount"),
        gr.Number(label="Old Balance Origin"),
        gr.Number(label="New Balance Origin"),
        gr.Number(label="Old Balance Destination"),
        gr.Number(label="New Balance Destination"),
        gr.Number(label="Balance Diff Origin"),
        gr.Number(label="Balance Diff Destination")
    ],
    outputs="text",
    title="Fraud Detection Model",
    description="Enter transaction details to predict if it's fraud or not"
)

iface.launch()
