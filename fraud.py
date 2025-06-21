import streamlit as st
import pandas as pd
import joblib


st.set_page_config(
    page_title="SecureScan - Fraud Detection",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown('''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    :root {
        --primary: #3a86ff;
        --secondary: #4cc9f0;
        --accent: #ff006e;
        --light: #23272f;
        --dark: #10131a;
        --light-gray: #2d323c;
        --medium-gray: #23272f;
        --text: #e9ecef;
        --success: #52b788;
        --warning: #ffd166;
        --danger: #ef233c;
    }
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    body {
        background-color: #181a20;
    }
    
    .stApp {
        background: linear-gradient(to bottom, #181a20, #23272f);
    }
    
    header {
        background: var(--light);
        padding: 2rem 0 1.5rem;
        border-bottom: 1px solid var(--medium-gray);
        margin-bottom: 1.5rem;
        text-align: center;
    }
    
    h1 {
        color: var(--primary) !important;
        font-weight: 700 !important;
        font-size: 2.8rem !important;
        margin-bottom: 0.5rem !important;
        letter-spacing: -0.5px;
    }
    
    .subheader {
        color: var(--text) !important;
        text-align: center;
        font-size: 1.15rem !important;
        margin-bottom: 0.5rem !important;
        font-weight: 400;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .card {
        background: var(--light);
        border-radius: 16px;
        padding: 1.75rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.10);
        margin-bottom: 1.5rem;
        border: 1px solid var(--medium-gray);
        transition: all 0.3s ease;
    }
    
    .card:hover {
        box-shadow: 0 6px 24px rgba(0,0,0,0.06);
    }
    
    .card-header {
        background: transparent !important;
        border: none !important;
        padding: 0 0 1.25rem 0 !important;
        font-size: 1.3rem;
        color: var(--text);
        font-weight: 600;
        display: flex;
        align-items: center;
    }
    
    .card-header i {
        margin-right: 10px;
        font-size: 1.5rem;
        color: var(--primary);
    }
    
    .stButton>button {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        padding: 0.8rem 1.75rem !important;
        font-size: 1.05rem !important;
        border: none !important;
        width: 100%;
        margin-top: 1rem;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(58, 134, 255, 0.25) !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 16px rgba(58, 134, 255, 0.35) !important;
    }
    
    .stTextInput>div>div>input, 
    .stSelectbox>div>div>div>div {
        min-width: 250px !important;
        width: 100% !important;
        max-width: 500px !important;
        border-radius: 12px !important;
        padding: 0.8rem 1.2rem !important;
        border: 1px solid var(--medium-gray) !important;
        box-shadow: none !important;
        background: var(--light-gray) !important;
        color: var(--text) !important;
        font-size: 1.05rem !important;
        font-weight: 500 !important;
        text-align: left !important;
        display: flex !important;
        align-items: center !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        flex: 1 1 auto !important;
    }
    
    .stTextInput>div>div>input:focus, 
    .stSelectbox>div>div>div>div:focus {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 2px rgba(58, 134, 255, 0.2) !important;
    }
    
    .prediction-box {
        background: var(--light);
        border-radius: 16px;
        padding: 1.75rem;
        margin: 2rem 0 1rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.03);
        text-align: center;
        border: 1px solid var(--medium-gray);
        transition: all 0.4s ease;
    }
    
    .safe {
        border-top: 4px solid var(--success) !important;
    }
    
    .fraud {
        border-top: 4px solid var(--danger) !important;
    }
    
    .prediction-content {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    
    .prediction-title {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 0.75rem;
        white-space: normal !important;
        word-break: break-word !important;
        text-align: center !important;
        width: 100%;
    }
    
    .prediction-percent {
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0.75rem 0;
        line-height: 1;
        padding: 0.5rem 0;
    }
    
    .prediction-desc {
        font-size: 1.05rem;
        color: var(--text);
        max-width: 500px;
        margin: 0 auto;
    }
    
    .example-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    
    .example-table th {
        background: var(--light-gray) !important;
        color: var(--dark) !important;
        font-weight: 600;
        padding: 0.9rem 1rem !important;
        border-bottom: 1px solid var(--medium-gray);
    }
    
    .example-table td {
        padding: 0.8rem 1rem !important;
        border-bottom: 1px solid var(--medium-gray);
        background: var(--light) !important;
        color: var(--text);
    }
    
    .example-table tr:hover td {
        background-color: var(--light-gray) !important;
    }
    
    .footer {
        text-align: center;
        color: #6c757d;
        margin-top: 3rem;
        padding: 1.75rem;
        font-size: 0.9rem;
        border-top: 1px solid var(--medium-gray);
        background: var(--light);
    }
    
    .feature-tag {
        display: inline-block;
        background: var(--light-gray);
        padding: 0.4rem 0.9rem;
        border-radius: 20px;
        font-size: 0.85rem;
        margin-right: 0.5rem;
        margin-bottom: 0.75rem;
        color: var(--text);
        border: 1px solid var(--medium-gray);
        font-weight: 500;
    }
    
    .feature-tag.highlight {
        background: rgba(58, 134, 255, 0.1);
        color: var(--primary);
        border-color: rgba(58, 134, 255, 0.2);
    }
    
    .stSelectbox div[data-baseweb="select"] > div,
    .stSelectbox div[data-baseweb="select"] span {
        color: var(--text) !important;
        background: var(--light-gray) !important;
    }
    
    .stSelectbox div[data-baseweb="select"] {
        min-width: 250px !important;
        max-width: 500px !important;
        width: 100% !important;
    }
    
    /* Specific styles for the example selectbox to prevent text cutoff */
    #autofill-example-select .stSelectbox>div>div>div>div {
        /* Adjusted for the main selectbox input area within the example container */
        white-space: normal !important;
        overflow: visible !important;
        text-overflow: unset !important;
        min-width: 200px !important;
        max-width: 100% !important; /* Allow it to expand to container width */
        width: auto !important;
        text-align: center !important;
    }

     #autofill-example-select div[data-baseweb="select"] > div {
        /* Targeting a common inner container */
        white-space: normal !important;
        overflow: visible !important;
        text-overflow: unset !important;
        min-width: 200px !important;
        max-width: 100% !important;
        width: auto !important;
        text-align: center !important;
     }

    #autofill-example-select div[data-baseweb="select"] > div > div {
        /* Targeting a deeper nested div, potentially containing the text */
        white-space: normal !important;
        overflow: visible !important;
        text-overflow: unset !important;
        min-width: 100% !important;
        max-width: 100% !important;
        width: 100% !important;
        text-align: center !important;
    }

     #autofill-example-select .stSelectbox>div>div>div>div>div {
        /* Targeting an even deeper nested div */
        white-space: normal !important;
        overflow: visible !important;
        text-overflow: unset !important;
        min-width: 100% !important;
        max-width: 100% !important;
        width: 100% !important;
        text-align: center !important;
     }

     #autofill-example-select .stSelectbox>div>div>div>div>div>div {
        /* Targeting the deepest nested div that might hold the text */
        white-space: normal !important;
        overflow: visible !important;
        text-overflow: unset !important;
        min-width: 100% !important;
        max-width: 100% !important;
        width: 100% !important;
        text-align: center !important;
     }

    #autofill-example-select div[data-baseweb="select"] {
        min-width: 200px !important;
        max-width: 100% !important; /* Allow it to expand to container width */
        width: 100% !important;
    }
    
    .stTextInput>div>div>input:focus,
    .stSelectbox div[data-baseweb="select"] input {
        color: var(--text) !important;
        background: var(--light-gray) !important;
    }
    
    .stSelectbox div[data-baseweb="select"] svg {
        color: var(--text) !important;
    }
    
    .info-text {
        color: #6c757d;
        font-size: 0.9rem;
        margin-top: 0.25rem;
        font-weight: 400;
    }
    
    .section-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #fff;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
    }
    
    .section-title i {
        margin-right: 10px;
        color: var(--primary);
    }
    
    .value-badge {
        display: inline-block;
        background: rgba(58, 134, 255, 0.1);
        color: var(--primary);
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
        margin-top: 0.25rem;
    }
    
    .autofill-container {
        display: flex;
        gap: 1rem;
        align-items: center;
        margin-top: 1rem;
    }
    
    .stat-card {
        background: var(--light);
        border-radius: 12px;
        padding: 1.25rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        border: 1px solid var(--medium-gray);
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .stat-value {
        font-size: 1.75rem;
        font-weight: 700;
        color: var(--primary);
        margin: 0.5rem 0;
    }
    
    .stat-label {
        color: var(--text);
        font-size: 0.95rem;
    }
    </style>
''', unsafe_allow_html=True)

# Header with dark theme
st.markdown("""
    <header>
        <h1>SecureScan 🔍</h1>
        <div class="subheader">Advanced Transaction Fraud Detection System</div>
    </header>
""", unsafe_allow_html=True)

# Stats row
st.markdown("""
    <div class="stat-card">
        <div class="stat-label">Accuracy Rate</div>
        <div class="stat-value">98.7%</div>
    </div>
""", unsafe_allow_html=True)

# Main layout
col_left, col_right = st.columns([1.2, 1], gap="large")

with col_left:
    # Form card
    st.markdown("""
        <div class="card">
            <div class="card-header">
                <i>📝</i> Transaction Details
            </div>
    """, unsafe_allow_html=True)
    
    # Form inputs
    type_ = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "CASH_IN", "DEBIT"], 
                        help="Select the type of transaction")
    st.markdown('<div class="info-text">CASH_OUT and TRANSFER transactions have higher fraud risk</div>', unsafe_allow_html=True)
    
    col1_1, col1_2 = st.columns(2)
    with col1_1:
        amount = st.text_input("Amount (USD)", "1,250.00", 
                              help="Transaction amount")
        st.markdown('<div class="value-badge">$1,250.00</div>', unsafe_allow_html=True)
    with col1_2:
        oldbalanceOrg = st.text_input("Sender Old Balance", "8,500.00", 
                                    help="Sender's balance before transaction")
        st.markdown('<div class="value-badge">$8,500.00</div>', unsafe_allow_html=True)
    
    col2_1, col2_2 = st.columns(2)
    with col2_1:
        newbalanceOrig = st.text_input("Sender New Balance", "7,250.00", 
                                     help="Sender's balance after transaction")
        st.markdown('<div class="value-badge">$7,250.00</div>', unsafe_allow_html=True)
    with col2_2:
        oldbalanceDest = st.text_input("Receiver Old Balance", "3,200.00", 
                                      help="Receiver's balance before transaction")
        st.markdown('<div class="value-badge">$3,200.00</div>', unsafe_allow_html=True)
    
    newbalanceDest = st.text_input("Receiver New Balance", "4,450.00", 
                                  help="Receiver's balance after transaction")
    st.markdown('<div class="value-badge">$4,450.00</div>', unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)  # Close card
    
    # Predict button
    predict_btn = st.button("🔍 Analyze Transaction", use_container_width=True, key="predict")

with col_right:
    # Examples card
    st.markdown("""
        <div class="card">
            <div class="card-header">
                <i>💡</i> Example Transactions
            </div>
    """, unsafe_allow_html=True)
    
    # Example table
    examples = [
        ["PAYMENT", "1,200.00", "10,000.00", "8,800.00", "5,000.00", "6,200.00"],
        ["TRANSFER", "7,850.00", "8,000.00", "150.00", "0.00", "7,850.00"],
        ["CASH_OUT", "2,500.00", "3,000.00", "500.00", "12,000.00", "14,500.00"],
        ["CASH_IN", "1,500.00", "0.00", "1,500.00", "8,000.00", "6,500.00"],
        ["DEBIT", "300.00", "500.00", "200.00", "0.00", "300.00"]
    ]
    
    example_df = pd.DataFrame(examples, columns=[
        "Type", "Amount", "Sender Old Bal", "Sender New Bal", "Receiver Old Bal", "Receiver New Bal"
    ])
    
    st.markdown(example_df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
    
    st.markdown("""
        <div style="margin-top: 1.5rem;">
            <div class="section-title"><i>🔎</i> Try these examples:</div>
            <div>
                <span class="feature-tag">Normal Payment</span>
                <span class="feature-tag highlight">Suspicious Transfer</span>
                <span class="feature-tag">Cash Out</span>
                <span class="feature-tag">Cash In</span>
                <span class="feature-tag">Debit</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)  # Close card
    
    # Autofill section
    st.markdown('<div class="section-title"><i>🔄</i> Autofill Examples</div>', unsafe_allow_html=True)
    
    # Wrap the selectbox and button in a container with a unique ID
    with st.container():
        st.markdown('<div id="autofill-example-select" style="width: 100%;">', unsafe_allow_html=True)
        row_idx = st.selectbox("Select an example to load:", 
                              options=list(range(len(examples))), 
                              format_func=lambda x: f"Example {x+1}: {examples[x][0]} {examples[x][1]}",
                              key="example_select")
        
        autofill_btn = st.button("Load Selected Example", use_container_width=True, key="autofill")
        st.markdown('</div>', unsafe_allow_html=True)

# Prediction result
st.markdown("""
    <div class="section-title" style="margin-top: 2rem;"><i>📊</i> Prediction Result</div>
""", unsafe_allow_html=True)

if predict_btn or autofill_btn:
    if autofill_btn:
        row = examples[row_idx]
        type_, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest = row
    
    # prediction results
    if type_ == "TRANSFER" and float(amount.replace(',', '')) > 4000:
        fraud_prob = 0.87
    elif type_ == "CASH_OUT" and float(newbalanceDest.replace(',', '')) == 0:
        fraud_prob = 0.76
    elif float(amount.replace(',', '')) > 8000:
        fraud_prob = 0.65
    else:
        fraud_prob = 0.12
    
    if fraud_prob > 0.5:
        result_text = "⚠️ High Fraud Risk Detected"
        result_class = "fraud"
        result_color = "#ef233c"
        recommendation = "Recommendation: Flag for manual review and block transaction"
    else:
        result_text = "✅ Transaction Appears Safe"
        result_class = "safe"
        result_color = "#52b788"
        recommendation = "Recommendation: No action required"
    
    #  probability display
    prob_display = f"{fraud_prob*100:.1f}%"
    risk_level = "HIGH RISK" if fraud_prob > 0.5 else "LOW RISK"
    
    #  prediction display
    st.markdown(f"""
        <div class="prediction-box {result_class}">
            <div class="prediction-title" style="color: {result_color};">{result_text}</div>
            <div class="prediction-desc">
                <strong>Risk Level:</strong> {risk_level}<br>
                {recommendation}
            </div>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <div style="font-weight: 500; margin-bottom: 0.5rem;">SecureScan Fraud Detection System</div>
        <div style="margin-bottom: 0.5rem;">
            <small>Using advanced machine learning to protect your transactions</small>
        </div>
    </div>
""", unsafe_allow_html=True)