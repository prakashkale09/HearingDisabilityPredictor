import streamlit as st
import pandas as pd
import pickle
model= pickle.load(open('../Hearing_pickle.pkl', 'rb'))
st.title("Hearing Disability Prediction")
Age=st.number_input("Enter Age")
Physical_score=st.number_input("Enter Physical Score")
if st.button("Predict"):
    # create a dataframe for prediction
    df_predict = pd.DataFrame({
        "Age": Age,
        "Physical_score": Physical_score,
    }, index=["Age"])

    # predict the salary
    predictions = model.predict(df_predict)
    if predictions[0] == 1:
        st.write("You are likely to have hearing disability")
    else:
        st.write("You are likely to not have hearing disability")
 
