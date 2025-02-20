import pickle
import streamlit as st

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

st.title('DiaWise')

Pregnancies = st.text_input('Nilai Pregnancies')

Glucose = st.text_input('Nilai Glucose')

BloodPressure = st.text_input('Nilai BloodPressure')

SkinThickness = st.text_input('Nilai SkinThickness')

Insulin = st.text_input('Nilai Insulin')

BMI = st.text_input('Nilai BMI')

DiabetesPedigreeFunction = st.text_input('Nilai DiabetesPedigreeFunction')

Age = st.text_input('Umur')


diab_diagnosis = ''

if st.button('Test prediksi Diabetes'): 
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Pasien terkena diabetes'
    else:
        diab_diagnosis = 'Pasien sehat'

    st.success(diab_diagnosis)

