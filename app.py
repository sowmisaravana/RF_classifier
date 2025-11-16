import streamlit as st
import joblib
import numpy as np

model = joblib.load("titanic_rf_model.joblib")

st.title("🚢 Titanic Survival Prediction App")
st.write("Enter passenger details to predict whether they would survive.")


pclass = st.selectbox("Passenger Class (Pclass)", [1, 2, 3])

sex = st.selectbox("Sex", ["male", "female"])
sex_num = 1 if sex == "female" else 0  

age = st.number_input("Age", min_value=0, max_value=100, value=25)

sibsp = st.number_input("Siblings/Spouses Aboard (SibSp)", min_value=0, max_value=10, value=0)

parch = st.number_input("Parents/Children Aboard (Parch)", min_value=0, max_value=10, value=0)

fare = st.number_input("Fare", min_value=0.0, max_value=600.0, value=32.0)


if st.button("Predict Survival"):
    
    
    input_data = np.array([[pclass, sex_num, age, sibsp, parch, fare]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("🟢 The passenger would have **SURVIVED**.")
    else:
        st.error("🔴 The passenger would have **NOT SURVIVED**.")
