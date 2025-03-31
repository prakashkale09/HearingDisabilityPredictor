import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open('../Hearing_pickle.pkl', 'rb'))

# Title and description
st.title("Hearing Disability Prediction")
st.markdown("""
    **Instructions:**
    - Enter your age and physical score in the inputs below.
    - Click the 'Predict' button to find out if you are likely to have a hearing disability.
    - The model is based on certain parameters, so the prediction is just an estimate.
""")

# Sidebar for user inputs
with st.sidebar:
    st.header("User Input")
    Age = st.number_input("Enter Age", min_value=0, max_value=100, step=1, help="Enter your age in years")
    Physical_score = st.number_input("Enter Physical Score", min_value=0.0, max_value=100.0, step=0.1, help="Enter your physical score based on the given test")

submit_button = st.button("Predict")

if submit_button:
    if Age <= 0 or Physical_score <= 0:
        st.error("Please enter valid values for both age and physical score.")
    else:
        # Create dataframe for prediction
        df_predict = pd.DataFrame({
            "Age": [Age],
            "Physical_score": [Physical_score],
        })

        # Prediction with spinner
        with st.spinner("Making prediction..."):
            predictions = model.predict(df_predict)
            st.success('Prediction Complete!')

        # Display results
        if predictions[0] == 1:
            st.write("You are likely to have hearing disability 🦻")
            st.image("images.png", use_column_width=True)
        else:
            st.write("You are likely to not have hearing disability 👂")
            st.image("path_to_no_hearing_disability_image.png", use_column_width=True)
