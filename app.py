import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import pickle
import sklearn
import streamlit
import numpy as np
import pandas as pd
loaded_model = pickle.load(open('C:/Users/USER/Documents/Streamlit ML APPS/Diabetes Project/Saved_model.pkl', 'rb'))
input_data = (5,166,72,19,175,25.8,0.587,51)

# changing the input_data to numpy array
input_data_as_numpy_array = np.array(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')