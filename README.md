# Automated-ML-Modelling

This is the Python web application that allows users to upload a dataset, generate an automated exploratory data analysis (EDA) report using the pandas-profiling library, and train an automatic machine learning model using the pycaret library.

# Installation
To run this application, you need to have Python 3.x and the following packages installed:

Streamlit

Pandas

Pandas-profiling

Streamlit-pandas-profiling

Pycaret

Otherwise You can install them via pip by running:

pip install -r requirements.txt

# Usage

To run the application, clone this repository, navigate to the directory where the code is located, and run:

streamlit run app.py

This will launch the Streamlit app in your web browser.

Once the app is running, you will see a sidebar with three options:

Upload: Allows you to upload a CSV file with your dataset. Once the file is uploaded, it will be displayed in a table on the app.

Profile Report: Generates an automated EDA report using the pandas-profiling library. You can download the report as an HTML file by clicking the "Download Report" button.

Automatic Model Training: Trains an automatic machine learning model using the pycaret library. When you select the "Automatic Model Training" option, you will need to select a target feature and a problem type (regression or classification). The app will then train an automatic machine learning model using the pycaret library and display a table with the performance metrics of several models. You can download the best model as a pickle file by clicking the "Download Model" button.
 
# Contributing

We welcome contributions from the community! If you have any ideas or suggestions for improving the project, please feel free to create an issue or submit a pull request.
