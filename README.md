## 🚢 Titanic Survival Prediction – Random Forest Classifier

A Machine Learning project that predicts whether a passenger survived the Titanic disaster using a Random Forest Classifier.
The model is trained using the Titanic dataset and deployed using Streamlit, with the model saved using Joblib.

## 📘 Project Summary

This project demonstrates end-to-end ML workflow:

Loading and preprocessing Titanic dataset

Feature selection

Training a Random Forest model

Saving the trained model using Joblib

Building a Streamlit web application for predictions

The user can input passenger details, and the app will predict whether the passenger would have survived.

## 📊 Dataset

Dataset used:
Titanic CSV from Data Science Dojo (GitHub)

https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

Features Used for Model Training
Pclass  → Passenger class (1, 2, 3)
Sex     → Male/Female (encoded)
Age     → Passenger age
SibSp   → Number of siblings/spouses aboard
Parch   → Number of parents/children aboard
Fare    → Ticket fare

Target Variable
Survived (0 = No, 1 = Yes)

## 🛠 Technologies Used
Technology	Purpose
Python	Programming
Pandas, NumPy	Data preparation
Scikit-Learn	Machine Learning
RandomForestClassifier	Prediction model
Joblib	Save/load trained model
Streamlit	Web UI development
📁 Project Structure
## 📦 Titanic-RandomForest-Classifier
│
├── app.py                     # Streamlit web app
├── titanic_rf_model.joblib    # Saved model (joblib)
├── train_model.ipynb          # Training notebook
├── README.md                  # Project documentation
└── requirements.txt           # All dependencies

## 🚀 How to Run the Project
1️⃣ Install Dependencies
pip install -r requirements.txt


or install manually:

pip install pandas numpy scikit-learn joblib streamlit

2️⃣ Run the Streamlit App

Inside the project folder:

python -m streamlit run app.py


This will open the web app in your browser automatically.

## 🎛 Streamlit App Inputs

The app asks for:

Passenger Class (1, 2, or 3)

Sex

Age

Number of siblings/spouses aboard

Number of parents/children aboard

Ticket Fare

Upon clicking Predict, the app displays:

🟢 Survived

🔴 Did Not Survive

## 📈 Model Performance

The Random Forest model:

Performs well on mixed data

Handles non-linearity

Reduces overfitting

Easy to train and interpret

Accuracy may vary depending on the dataset and preprocessing.

## 📌 Requirements
Example requirements.txt:

pandas
numpy
scikit-learn
joblib
streamlit
## screenshort
<img width="794" height="733" alt="Screenshot 2025-11-16 190100" src="https://github.com/user-attachments/assets/1552fc0a-b8c5-42b8-8db4-3812f75a1641" />
