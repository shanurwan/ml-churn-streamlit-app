# 📉 Recruiter Churn Radar: A Streamlit-Powered Prototype for Customer Success Teams

## 🔍 Overview
This project simulates a real-world churn prediction system for a B2B recruitment platform (like JobStreet or SEEK). The goal was to identify customers likely to churn — based on historical engagement behavior — using a machine learning pipeline and deploy it in real-time with Streamlit.

---

## 📁 Dataset Description
A synthetic dataset was generated using Python’s `Faker` library to reflect customer behaviors realistically. Each row represents one customer.

| Column                | Description                                      |
|-----------------------|--------------------------------------------------|
| `customer_id`         | Unique identifier                                |
| `signup_date`         | Date of registration                             |
| `last_login_date`     | Most recent platform login                       |
| `job_posts`           | Number of job postings created                   |
| `applications_received` | Total applications received from job posts     |
| `support_tickets`     | Number of support tickets submitted              |
| `plan_type`           | Subscription type (Free, Basic, Pro)             |
| `is_churned`          | Target label: 1 = churned, 0 = retained          |

---

## 🔄 Project Pipeline

### 1. Data Simulation
- Generated ~1000 customer records using `Faker`
- Simulated churn logic (e.g., long inactivity + low usage → high churn chance)

### 2. Data Preprocessing
- Converted dates to datetime
- Engineered features:
  - `days_since_signup`
  - `days_since_last_login`
  - `login_frequency`
  - `engagement_score`
  - `support_intensity`
- Encoded categorical features (`plan_type`)
- Scaled features for logistic regression

### 3. Exploratory Data Analysis (EDA)
- Visualized distributions & class imbalance
- Found strong churn indicators:
  - Free-tier usage
  - Long inactivity
  - Low engagement

### 4. Modeling
- Models tested:
  - Logistic Regression (baseline)
  - Random Forest Classifier (best)
- Metrics:
  - Accuracy, Precision, Recall, F1-score, ROC-AUC
- **Best Model (Random Forest):**
  - F1-score: **0.86**
  - ROC-AUC: **0.91**

### 5. Model Insights
- Strongest churn predictors:
  - Days since last login (inactivity)
  - Plan type (Free)
  - Low job posting & engagement

---

## 🚀 Streamlit App (Deployed Demo)
The app allows users to:
- Upload customer CSV files
- View churn predictions in real-time
- Identify customers likely to churn

🔗 [https://shanurwan-ml-churn-streamlit-app-main-wgt3kz.streamlit.app/]

### 📄 Sample Input CSV
```csv
customer_id,signup_date,last_login_date,job_posts,applications_received,support_tickets,plan_type
CUS1234,2023-01-02,2024-03-15,10,120,1,Pro
CUS5678,2022-07-10,2023-12-01,1,10,3,Free
```

✅ Output

```csv
is_churned = 1 → likely to churn
is_churned = 0 → likely to stay
```

### 💡 Key Insights & Business Value
1. From Code to Context
Even high-performing models fail if behavior isn’t well captured. This project replicates a real SaaS environment where churn prediction must be both technical and contextual.

2. Data Quality = Product Trust
Working with synthetic data revealed how good metrics can be misleading without realistic input. Business-critical models must start with valid data.

3. Retention = Revenue
Churn signals like inactivity or plan usage help businesses take action, such as customer re-engagement or upselling.

4. Actionable, Explainable AI
Predictors like login gaps or low job activity are easily interpreted, making the model usable by non-technical teams.

5. Deployment as a Service
The Streamlit app acts as a prototype for internal tools that serve live business decisions instead of just static reports.

### 🔧 Potential Improvements
- Validate with real-world datasets (e.g., Kaggle, HuggingFace)

- Add more behavioral metrics (e.g., session duration, click-through)

- Incorporate time-series trends (e.g., monthly job post volume)

- Use SHAP for explainability

- Build a Power BI dashboard for reporting

### 🌟 Why This Project Matters
This isn’t just another ML notebook. It's a full pipeline that mimics real product challenges:

✅ End-to-end execution (from data gen to deployment)

✅ Business alignment (customer retention strategies)

✅ Resourcefulness (realism with synthetic data)

✅ Deployment thinking (Streamlit app as a usable tool)

### 🛠️ How to Run
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Launch the Streamlit app
streamlit run main.py
```


