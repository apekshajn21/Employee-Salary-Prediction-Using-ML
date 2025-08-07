import streamlit as st
import joblib 
import numpy as np
import plotly.express as px
import pandas as pd

# --------------------------- Page Config ---------------------------
st.set_page_config(page_title="Salary Estimation App", layout="wide")

# --------------------------- Sidebar ---------------------------
st.sidebar.title("🔧 Settings")
st.sidebar.info("Adjust values to estimate your salary based on experience.")
st.sidebar.markdown("---")
st.sidebar.markdown("📊 This model predicts salary using 3 key features:\n\n- Years at Company\n- Satisfaction Level\n- Average Monthly Hours")

# --------------------------- Title ---------------------------
st.title("💼 Salary Estimation App")
st.markdown("🔍 *Predict salary based on your experience and satisfaction at work!*")

st.image(
    "https://img.freepik.com/premium-photo/concept-artificial-satellites-viewed-from-space-forming-network-earth-providing-internet-services-3d-rendering_651547-1600.jpg",
    caption="Let's make some money!",
    use_container_width=True
)

st.divider()

# --------------------------- Input Section ---------------------------
st.subheader("📝 Enter Your Details:")

col1, col2, col3 = st.columns(3)

with col1:
    years_at_company = st.slider("Years at Company", 0, 20, 3)

with col2:
    satisfaction_level = st.slider("Satisfaction Level", 0.0, 1.0, 0.7, step=0.01)

with col3:
    avg_monthly_hrs = st.slider("Average Monthly Hours", 120, 310, 200)

x = [years_at_company, satisfaction_level, avg_monthly_hrs]

# --------------------------- Load Model ---------------------------
scaler = joblib.load('scaler.pkl')
model = joblib.load('model.pkl')

# --------------------------- Predict ---------------------------
predict_button = st.button("🚀 Predict Salary")
st.divider()

if predict_button:
    st.balloons()

    # Transform input and predict
    x_array = scaler.transform([np.array(x)])
    prediction = model.predict(x_array)

    # Display Prediction
    st.metric(label="💰 Predicted Salary", value=f"₹ {prediction[0]:,.2f}")

    # Bar Chart of Input Features
    df_input = pd.DataFrame({
        "Feature": ["Years at Company", "Satisfaction Level", "Average Monthly Hours"],
        "Value": x
    })
    fig = px.bar(df_input, x="Feature", y="Value", color="Feature", title="Your Input Profile", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

    # Comparison with average salary
    df_compare = pd.DataFrame({
        "Category": ["Predicted Salary", "Average Salary (sample)"],
        "Value": [prediction[0], 50000]  # Replace 50000 with real average if available
    })
    fig2 = px.bar(df_compare, x="Category", y="Value", color="Category", title="Salary Comparison", text_auto=True)
    st.plotly_chart(fig2, use_container_width=True)

    # Workload & satisfaction warning
    if satisfaction_level < 0.3 and avg_monthly_hrs > 280:
        st.warning("⚠️ High work hours and low satisfaction! Might indicate burnout.")

else:
    st.info("👆 Enter details and press the **Predict Salary** button.")
