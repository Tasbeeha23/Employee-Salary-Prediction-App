# Imports

import streamlit as st
import joblib
import numpy as np
import plotly.express as px
import pandas as pd

# Page config and title
st.set_page_config(page_title="Salary Estimation App", layout="wide")
st.title("💼 Salary Estimation App")
st.markdown("👩‍💻 Predict your expected salary based on company experience!")

# Cute animated gif
st.image("https://media.giphy.com/media/bolghismAzrpisoqut/giphy.gif", 
         caption="Let's predict!", use_column_width=True)

# Divider
st.divider()

# Input section
st.subheader("Input Your Details")

col1, col2, col3 = st.columns(3)

with col1:
    years_at_company = st.number_input("Years at Company", min_value=0, max_value=20, value=3)

with col2:
    satisfaction_level = st.slider("Satisfaction Level", min_value=0.0, max_value=1.0, step=0.01, value=0.7)

with col3:
    average_monthly_hours = st.slider("Average Monthly Hours", min_value=129, max_value=318, step=1, value=160)

# Divider
st.divider()

# Predict section
X = [years_at_company, satisfaction_level, average_monthly_hours]

# Load model and scaler
scaler = joblib.load(r"C:\Users\91990\TECHNICAL TRAINING\scaler.pkl")
model = joblib.load(r"C:\Users\91990\TECHNICAL TRAINING\model.pkl")

predict_button = st.button("🎯 Predict Salary")

if predict_button:
    st.balloons()
    
    X_array = scaler.transform([np.array(X)])
    prediction = model.predict(X_array)

    st.success(f"💰 Predicted Salary: ₹ {prediction[0]:,.2f}")

    # Visualize user input
    input_df = pd.DataFrame({
        "Feature": ["Years at Company", "Satisfaction Level", "Average Monthly Hours"],
        "Value": X
    })

    fig = px.bar(input_df, x="Feature", y="Value", color="Feature", 
                 title="Your Input Profile", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Enter details and press the **Predict Salary** button.")
