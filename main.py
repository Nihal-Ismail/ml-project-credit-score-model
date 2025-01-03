import streamlit as st
from prediction_helper import predict

# Set the page configuration and title
st.set_page_config(
    page_title="Lauki Finance: Credit Risk Modelling",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inline CSS using st.markdown (Streamlit-compatible)
st.markdown(
    """
    <style>
        /* Styling the main container */
        .main-container {
            background-color: #FAFAFA;
            color: #212121;
            padding: 20px;
            border-radius: 8px;
            margin-top: 10px;
        }

        /* Title text styling */
        .title-text {
            color: #00796B;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 30px;
        }

        /* Button styling */
        div.stButton > button {
            background-color: #1E88E5; /* Royal Blue */
            color: white; /* White text for contrast */
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            transition: background-color 0.3s ease;
        }
        div.stButton > button:hover {
            background-color: #1565C0; /* Darker Royal Blue for hover effect */
        }

        /* Metric styling */
        .stMetric {
            background-color: #E8F5E9;
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        /* Input fields styling */
        .stNumberInput input, .stSelectbox select {
            background-color: #E1F5FE;
            border-radius: 8px;
            padding: 10px;
            border: 1px solid #B3E5FC;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# App title
st.markdown('<div class="title-text">📊 Lauki Finance: Credit Risk Modelling</div>', unsafe_allow_html=True)

# Inputs: Organize with columns and sections
st.markdown('<div class="main-container">', unsafe_allow_html=True)
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

# Loan-to-Income Ratio with label above the yellow box
loan_to_income_ratio = loan_amount / income if income > 0 else 0
with row2[0]:
    st.markdown(
        """
        <div style="color: #212121; font-weight: Medium; font-size: 16px; margin-bottom: 1px;">
            Loan-to-Income Ratio
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div style="background-color: #FFF8E1; padding: 5px; border-radius: 5px; 
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); text-align: center;">
            <div style="font-size: 20px; font-weight: bold; color: #212121;">{loan_to_income_ratio:.2f}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

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

    # Conditional coloring based on the rating
    rating_colors = {
        "Poor": "#D32F2F",      # Red for Poor
        "Average": "#FFB74D",   # Lighter Amber for Average
        "Good": "#388E3C",      # Green for Good
        "Excellent": "#1976D2", # Blue for Excellent
    }
    rating_color = rating_colors.get(rating, "#000000")  # Default to black if the rating isn't recognized

    # Display results in an attractive layout
    st.markdown("#### Results")
    result_col1, result_col2, result_col3 = st.columns(3)

    # Default Probability
    with result_col1:
        st.markdown(
            f"""
            <div style="background-color: #EDE7F6; padding: 15px; border-radius: 10px; 
                        text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                <div style="font-size: 18px; font-weight: bold; color: #7E57C2;">Default Probability</div>
                <div style="font-size: 24px; font-weight: bold; color: #7E57C2;">{probability:.2%}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Credit Score
    with result_col2:
        st.markdown(
            f"""
            <div style="background-color: #E8F5E9; padding: 15px; border-radius: 10px; 
                        text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                <div style="font-size: 18px; font-weight: bold; color: #388E3C;">Credit Score</div>
                <div style="font-size: 24px; font-weight: bold; color: #388E3C;">{credit_score}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Rating
    with result_col3:
        st.markdown(
            f"""
            <div style="background-color: {rating_color}; padding: 15px; border-radius: 10px; 
                        text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                <div style="font-size: 18px; font-weight: bold; color: white;">Rating</div>
                <div style="font-size: 24px; font-weight: bold; color: white;">{rating}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
else:
    st.info("Enter all inputs and click '🔍 Calculate Risk' to see results.")

# Footer
st.markdown("---")
st.markdown("📊 **Powered by Muhammed Nihal C.** Designed for smarter credit decisions.")
st.markdown('</div>', unsafe_allow_html=True)
