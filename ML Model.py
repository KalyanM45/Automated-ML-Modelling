import streamlit as st
import pandas as pd
import os
from PIL import Image
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report  

from pycaret import classification, regression

st.title("Let me Do your Work")

df = None

with st.sidebar:
    st.title("I'm the Data God....!")
    image = Image.open("C:/Users/KALYAN/Desktop/databot-icon.png")
    st.image(image, use_column_width=True)
    Choice = st.radio("Navigation", ["Upload", "Profile Report", "Model Training"])

df = None

if os.path.exists("sourcedata.csv"):
    df = pd.read_csv("sourcedata.csv", index_col = None)

if Choice == "Upload":
    st.title("Push Your Dataset Here✌️")
    file = st.file_uploader("Upload Here")
    if file:       
        df = pd.read_csv(file, index_col = None)
        df.to_csv("sourcedata.csv", index = None)
        st.dataframe(df)

if Choice == "Profile Report":
    if df is not None:
        st.title("Automated Exploratory Data Analysis")
        if st.button("Generate Report"):
            profile_report = df.profile_report()
            st_profile_report(profile_report)
            with open('profile_report.html', 'w') as f:
                f.write(profile_report.to_html())
            st.download_button('Download Report', data=profile_report.to_html(), file_name='Profile Report.html', mime='text/html')
    else:
        st.warning("Please upload the dataset first ⚠️")
            
if Choice == "Model Training":
    if df is not None:
        target = st.selectbox("Select the Target Feature in the Dataset", df.columns)
        type = st.selectbox("Select the Problem Type",("Regression", "Classification"))

        if type == "Regression":
            if st.button("Train the Model"):
                regression.setup(df, target=target)
                setup_df = regression.pull()
                best_model = regression.compare_models()
                compare_df = regression.pull()
                st.dataframe(compare_df)
                best_model
                regression.save_model(best_model, 'best_model')

                with open('best_model.pkl', 'rb') as f: 
                    st.download_button('Download Model', f, file_name="best_model.pkl")

                os.remove("sourcedata.csv")

        if type == "Classification":
            if st.button("Train the Model"):
                classification.setup(df, target=target)
                setup_df = classification.pull()
                best_model = classification.compare_models()
                compare_df = classification.pull()
                st.dataframe(compare_df)
                best_model
                classification.save_model(best_model, 'best_model')

                with open('best_model.pkl', 'rb') as f: 
                    st.download_button('Download Model', f, file_name="best_model.pkl")
                os.remove("sourcedata.csv")
   
    else:
        st.warning("Please upload the dataset first ⚠️")
