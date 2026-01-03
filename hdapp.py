# import streamlit as st
# import pickle
# import numpy as np

# st.title('Welcome to Heart Disease Prediction!')
# with open('heart_disease.pkl','rb') as pickle_file:
#     model = pickle.load(pickle_file)

# st.image('heart.png', width=500, caption='Heart Disease Prediction App Image.')

# st.sidebar.header('How to Use!')
# st.sidebar.markdown(
#     """
# 1. Enter the Patient's Medical Information
# 2. Click "Predict" to find out the risk
# 3. The App Uses a Trained ML Model to Help you Make Informed Hearlth Decisions!
# DISCLAIMER!
# Consult a Doctor for More Information
# """
# )

# st.header('Enter Patient Details')
# col1, col2 = st.columns(2)
# with col1:
#     age = st.number_input('Age', min_value=1, max_value=120, value=45)
#     cp = st.selectbox('Chest Pain Type (cp)', [0,1,2,3])
#     thalach = st.number_input('Maximum Heart Rate Achieved (thalach)', min_value=60, max_value=220, value=150)
# with col2:
#     restecg = st.selectbox('Resting ECG Results (restecg)', [0,1,2])
#     exang = st.selectbox('Exercise Induced Angina (exang)', [0,1])

# if st.button('Predict'):
#     #Preparing the input for the model by converting the user inputs into 2D array
#     input_data = np.array([[age, cp, thalach, restecg, exang]])
#     prediction = model.predict(input_data)[0]
#     if prediction == 1:
#         st.error('The Patient is at Risk of Heart Disease!')
#     else:
#         st.success('The Patient is Not at Risk of Heart Disease!')

########################VERSION 2##################################
import streamlit as st
import pickle
import numpy as np

# Load trained model
with open('heart_disease.pkl', 'rb') as file:
    model = pickle.load(file)

# App title & image
st.title('❤️ Heart Disease Prediction App')
st.image('heart.png', width=500, caption='Early Detection Saves Lives')

# Sidebar instructions
st.sidebar.header('How to Use')
st.sidebar.markdown("""
1. Enter the patient's medical details  
2. Click **Predict**  
3. This app predicts heart disease severity  
⚠️ **Disclaimer:** This is not a medical diagnosis.
""")

# Input fields
st.header('Enter Patient Details')

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Age', 1, 120, 45)
    sex = st.selectbox('Sex', [0, 1])  # 0 = Female, 1 = Male
    cp = st.selectbox('Chest Pain Type (cp)', [0, 1, 2, 3])

with col2:
    trestbps = st.number_input('Resting Blood Pressure (trestbps)', 80, 200, 120)
    chol = st.number_input('Serum Cholesterol (chol)', 100, 600, 200)
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (fbs)', [0, 1])

with col3:
    restecg = st.selectbox('Resting ECG Results (restecg)', [0, 1, 2])
    thalach = st.number_input('Max Heart Rate Achieved (thalach)', 60, 220, 150)
    exang = st.selectbox('Exercise Induced Angina (exang)', [0, 1])

# Severity mapping
severity_map = {
    0: ('No Heart Disease', 'success'),
    1: ('Mild Heart Disease', 'warning'),
    2: ('Moderate Heart Disease', 'warning'),
    3: ('Severe Heart Disease', 'error'),
    4: ('Very Severe Heart Disease', 'error')
}

# Prediction
if st.button('Predict'):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang]])
    prediction = model.predict(input_data)[0]

    label, msg_type = severity_map[prediction]

    if msg_type == 'success':
        st.success(f'✅ Prediction: {label}')
    elif msg_type == 'warning':
        st.warning(f'⚠️ Prediction: {label}')
    else:
        st.error(f'🚨 Prediction: {label}')
