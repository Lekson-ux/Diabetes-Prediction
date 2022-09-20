import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import pickle
#import sklearn
import streamlit
import numpy as np
import pandas as pd
loaded_model = pickle.load(open('C:/Users/USER/Documents/Streamlit ML APPS/Diabetes Project/Saved_model.pkl', 'rb'))

#creating a function for prediction
def diabetes_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.array(input_data)
    #input_data_as_numpy_array = to_numeric(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'


def main():
    #giving title
    st.title('Diabetes Prediction web Application')
    st.subheader('Developer: Usman Oladapo :sunglasses:')
    st.write("### We need some information to predict the diabetic status")

    #getting input from user
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI= st.text_input('Body Mass Index Value')
    DiabetesPedigreeFunction= st.text_input('Diabetes Pedigree Function value')
    Age= st.text_input('Age of the Person')

    #code for prediction
    diagnosis = ''

    #creating a button for prediction

    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    st.success(diagnosis)

if __name__ == '__main__':
    main()