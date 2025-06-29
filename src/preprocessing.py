import pandas as pd
import numpy as np

def preprocess_customer_data(df: pd.DataFrame, today: str = "2030-06-16") -> pd.DataFrame:
   
    # Replace missing last_login_date with signup_date
    df['last_login_date'] = df['last_login_date'].fillna(df['signup_date'])

    # Convert date columns to datetime
    df['signup_date'] = pd.to_datetime(df['signup_date'])
    df['last_login_date'] = pd.to_datetime(df['last_login_date'])

    # Reference point for time features
    today = pd.to_datetime(today)

    # Feature engineering
    df['days_since_signup'] = (today - df['signup_date']).dt.days
    df['days_since_last_login'] = (today - df['last_login_date']).dt.days

    # Avoid zero division in login_gap
    df['login_gap'] = df['days_since_signup'] - df['days_since_last_login']
    df['login_gap'] = df['login_gap'].replace(0, 1e-6)

    df['login_frequency'] = df['days_since_signup'] / df['login_gap']
    df['engagement_score'] = (df['job_posts'] + df['applications_received']) / df['days_since_signup'].replace(0, 1e-6)
    df['support_intensity'] = df['support_tickets'] / df['days_since_signup'].replace(0, 1e-6)

    # Encode plan_type
    plan_map = {"free": 0, "basic": 1, "premium": 2, "enterprise": 3}
    df['plan_type'] = df['plan_type'].str.lower().map(plan_map)

    return df
