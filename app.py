import streamlit as st
import pandas as pd
import numpy as np
import time
from src.components.model_prediction import ModelPrediction


st.set_page_config(page_title='myapp')

def process_input(dictionary):

    df = pd.DataFrame.from_dict(data=dictionary, orient='index').T

    model_prediction = ModelPrediction()
    prediction = model_prediction.make_predictions(data=df)
    # print('from function', df)
    # st.dataframe(df)
    #st.write('Predicted price:', prediction[0])
    alert = st.progress(0, text='Making Predictions...')
    for i in range(100):
        time.sleep(0.01)
        alert.progress(i + 1, text='Making Predictions...')
    st.subheader(f' Predicted price of the house is:  {prediction[0]}')
    st.success('Yay! You made it!')
    alert.empty()



tab1, tab2, tab3 = st.tabs(["Train", "Predict", "About"])

with tab1:
    st.title('Model Training')
    st.write("""
    We have tried using the following models for the training of the model.
    1. LinearRegression
    2. Lasso Regression
    3. Ridge Regression
    4. Support Vector Regressor 
    5. DecisionTree Regressor
    6. RandomForest Regressor 
    
    From all of the above models we have found the best model as *RandomForest Regressor* for the predicting the prices of houses \
    and the dataset used was innercity-1.xlsx.
    """)

    st.subheader('Dataset used in the project:')

    with open('data/innercity-1.xlsx', 'rb') as file:
        st.download_button(label='Download the dataset',
                            data= file,
                            file_name='innercity-1.xlsx')

    st.write("""
    We have recorded the performance of each model in the following table
    """)

    results = pd.read_csv('data/results.csv', index_col=False)
    results = results.rename(columns={'Unnamed: 0': 'models'})
    results.index = list(range(1,7))
    st.dataframe(results)



with tab2:
    dictionary = {'long': 0, 'total_area': 0, 'room_bed': 0, 'sight': 0, 'quality': 0, 'ceil_measure': 0, 'zipcode': 0, 'lat': 0}
    # ['room_bed', 'sight','quality', 'ceil_measure','zipcode', 'lat','long','total_area','price']
    # long,total_area,room_bed,sight,quality,ceil_measure,zipcode,lat,
    st.title('Make Predictions')
    st.write("""
    Please provide the following information to make predictions""")
    with st.form("my_form", clear_on_submit=True):

        st.write("Fill out the following details")

        dictionary['room_bed'] = st.number_input('Enter number of bed rooms:', min_value=1, placeholder='enter your value', value=None)
        dictionary['total_area'] = st.number_input('Enter total area:', placeholder='enter your value', value=None)
        dictionary['ceil_measure'] = st.number_input('Enter ceiling measure:', placeholder='enter your value', value=None)
        

        dictionary['lat'] = st.number_input("Enter latitude:", placeholder='enter your value', value=None)
        dictionary['long'] = st.number_input("Enter longitude:", placeholder='enter your value', value=None)
        
        
        dictionary['sight'] = st.number_input('Enter sight value:', min_value=1, max_value=5, placeholder='enter your value', value=None)
        dictionary['quality'] = st.number_input('Enter quality:', min_value=1, max_value=10, placeholder='enter your value', value=None)
        
        dictionary['zipcode'] = st.number_input('Enter zipcode:', min_value=111111, max_value=999999, placeholder='enter your value', value=None)
        
        submitted = st.form_submit_button("Submit")

        if all(dictionary.values()) and submitted:
            alert = st.warning("Thanks for submitting..!\nPlease wait while we process your request")
            time.sleep(2)
            alert.empty()
            process_input(dictionary)
        elif submitted:
            st.warning('Something went wrong')
        else:
            st.warning("Please fill all the fields")

with tab3:
    st.balloons()
    st.header("House Price Prediction App")
    st.write("""
    More information about the project""")