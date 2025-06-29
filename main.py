
import streamlit as st
import pandas as pd
import joblib
from src.preprocessing import preprocess_customer_data

# Load trained model
@st.cache_resource
def load_model():
    return joblib.load("Model/random_forest_pipeline.joblib")


model = load_model()

st.title("Customer Churn Prediction")

# Upload CSV
uploaded_file = st.file_uploader("📁 Upload your customer CSV", type=["csv"])

if uploaded_file:
    raw_df = pd.read_csv(uploaded_file)
    processed_df = preprocess_customer_data(raw_df)

    # Drop unused cols
    drop_cols = ['customer_id', 'signup_date', 'last_login_date']
    X = processed_df.drop(columns=drop_cols, errors='ignore')

    # Predict
    predictions = model.predict(X)
    raw_df["is_churned"] = predictions

    # Split the data
    churned = raw_df[raw_df["is_churned"] == 1]
    retained = raw_df[raw_df["is_churned"] == 0]

    st.subheader("🔍 Prediction Summary")
    st.write(f"✅ Likely to Stay: {len(retained)} customers")
    st.write(f"⚠️ Likely to Churn: {len(churned)} customers")

    # Display both groups
    with st.expander("📉 View: Likely to Churn"):
        st.dataframe(churned)

    with st.expander("📈 View: Likely to Stay"):
        st.dataframe(retained)

    # Download buttons
    churned_csv = churned.to_csv(index=False).encode('utf-8')
    retained_csv = retained.to_csv(index=False).encode('utf-8')

    st.download_button("⬇️ Download Likely Churn CSV", churned_csv, "likely_churn.csv", "text/csv")
    st.download_button("⬇️ Download Likely Retained CSV", retained_csv, "likely_retained.csv", "text/csv")
