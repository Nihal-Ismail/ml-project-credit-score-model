import streamlit as st
from prediction_helper import predict

# Set the page configuration and title
st.set_page_config(
    page_title="Lauki Finance: Credit Risk Modelling",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for a light theme
st.markdown(
    """
    <style>
        /* Main light theme styling */
        .main {
            background-color: #FFFFFF;  /* White background */
            color: #333333;  /* Dark gray text for readability */
        }

        /* Styling the button container and text */
        .stButton > button {
            background-color: #007BFF !important;  /* Bright blue for buttons */
            color: white !important;  /* White text inside the button */
            border-radius: 8px;
            padding: 12px 25px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            transition: 0.3s ease;
        }

        /* Hover effect for the button */
        .stButton > button:hover {
            background-color: #0056b3 !important;  /* Darker blue for hover */
        }

        /* Title and content styling */
        .title-text {
            color: #1A237E;  /* Indigo for title */
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 30px;
        }

        .result-container {
            background-color: #E8F5E9;  /* Light green background for results */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }

        .metric-title {
            color: #2E7D32;  /* Dark green for metric titles */
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .input-section {
            margin-bottom: 20px;
        }

        .stSelectbox, .stNumberInput {
            background-color: #F1F8FF;  /* Light blue for input fields */
            color: #333333;  /* Dark text for inputs */
            border-radius: 8px;
            padding: 12px;
            margin: 8px 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .stMetric {
            background-color: #FFF9C4;  /* Light pastel yellow-green for metrics */
            border-radius: 8px;
            padding: 12px;
            color: #333333;  /* Dark text inside the metric boxes */
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* Progress bar color */
        .stProgress > div > div {
            background-color: #4CAF50;  /* Green progress bar */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# App title
st.markdown('<div class="title-text">📊 Lauki Finance: Credit Risk Modelling</div>', unsafe_allow_html=True)

# Add an option to choose theme (always light in this implementation)
st.sidebar.markdown("### App Customization")
st.sidebar.info("Currently, only the **light theme** is available for a consistent experience.")

# Inputs: Organize with columns and sections
st.markdown("### 🔢 Input Customer Details")
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Assign inputs to the first row
with row1[0]:
    age = st.number_input('📅 Age', min_value=18, step=1, max_value=100, value=28)
with row1[1]:
    income = st.number_input('💰 Annual Income', min_value=0, value=1200000)
with row1[2]:
    loan_amount = st.number_input('🏦 Loan Amount', min_value=0, value=2560000)

# Loan-to-Income Ratio
loan_to_income_ratio = loan_amount / income if income > 0 else 0
with row2[0]:
    st.metric(label="Loan-to-Income Ratio", value=f"{loan_to_income_ratio:.2f}")

# Other inputs
with row2[1]:
    loan_tenure_months = st.number_input('📆 Loan Tenure (Months)', min_value=0, step=1, value=36)
with row2[2]:
    avg_dpd_per_delinquency = st.number_input('📉 Avg Days Past Due (DPD)', min_value=0, value=20)

with row3[0]:
    delinquency_ratio = st.number_input('⚖️ Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=30)
with row3[1]:
    credit_utilization_ratio = st.number_input('📊 Credit Utilization Ratio (%)', min_value=0, max_value=100, step=1,
                                               value=30)
with row3[2]:
    num_open_accounts = st.number_input('🔓 Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)

with row4[0]:
    residence_type = st.selectbox('🏠 Residence Type', ['Owned', 'Rented', 'Mortgage'])
with row4[1]:
    loan_purpose = st.selectbox('🎯 Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
with row4[2]:
    loan_type = st.selectbox('📜 Loan Type', ['Unsecured', 'Secured'])

# Risk Calculation Button
st.markdown("### 📈 Credit Risk Evaluation")
if st.button('🔍 Calculate Risk'):
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    # Display results in an attractive layout
    st.markdown("#### Results")
    result_col1, result_col2, result_col3 = st.columns(3)
    with result_col1:
        st.markdown('<div class="metric-title">Default Probability</div>', unsafe_allow_html=True)
        st.progress(probability)  # Progress bar for probability
        st.write(f"{probability:.2%}")

    with result_col2:
        st.markdown('<div class="metric-title">Credit Score</div>', unsafe_allow_html=True)
        st.metric(label="Score", value=credit_score)

    with result_col3:
        st.markdown('<div class="metric-title">Rating</div>', unsafe_allow_html=True)
        st.metric(label="Rating", value=rating)

else:
    st.info("Enter all inputs and click '🔍 Calculate Risk' to see results.")

# Footer
st.markdown("---")
st.markdown("📊 **Powered by Muhammed Nihal C.** Designed for smarter credit decisions.")
