# Employee-Salary-Prediction-Using-ML
**Salary Estimation App**
This project is a Machine Learning-based Streamlit web application that predicts an employee's salary based on:

Years at the company

Satisfaction level

Average monthly working hours

It provides a clean user interface, visualizations using Plotly, and integrates a pre-trained ML model for prediction.

** Features?*
Predict salary based on input features
 Interactive sliders for entering input
 Beautiful visualizations for:

Input profile

Salary comparison
 Warning for potential burnout conditions
 User-friendly interface built with Streamlit
 Model built using scikit-learn, joblib, and NumPy

**Tech Stack**
Frontend: Streamlit

Backend: Python (scikit-learn, joblib, numpy)

Visualization: Plotly

Model Serialization: joblib

Deployment Ready: Yes (Streamlit sharing / local server)

**ML Model Used**
The model is trained using historical employee data and uses:

StandardScaler (for input normalization)

Linear Regression / Random Forest (as per your training model)

Trained and saved using joblib as:

scaler.pkl

**Install dependencies**
Make sure you have Python 3.7+ installed.
pip install -r requirements.txt

Sample Output
Here’s how the interface looks:

🎛**Input Form**
Sliders for entering:

Years at Company

Satisfaction Level

Average Monthly Hours

 **Output**
Salary prediction (₹ in Indian Rupees)

Input profile bar chart

Salary comparison chart

Burnout warning if applicable
model.pkl
