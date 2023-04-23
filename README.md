# Automated-ML-Modelling

This is the Streamlit web application that allows users to upload a dataset, generate an automated exploratory data analysis (EDA) report using the pandas-profiling library, and and train a machine learning model for regression or classification tasks.

# Installation
To run this application, you need to have Python 3.x and the following packages installed:

 - Streamlit
 - Pandas
 - Pandas-profiling
 - Pycaret

Otherwise you can install all the requirements by executing the following Command  

```sh
pip install -r requirements.txt
```

# Getting Started
This is make you understand how you may give instructions on setting up your project locally. To get a local copy up and running follow these simple example steps.

 1. Clone this repository
 ```sh
 git clone https://github.com/KalyanMurapaka45/Automated-ML-Modelling.git
 ```
 
 2. Install the required Python libraries listed in the requirements.txt
 ```sh
 pip install -r requirements.txt
 ```
3. Run the ML Model.py file 
```sh
streamlit run ML Model.py
```

# Usage Instructions

After running the ML Model.py file, a Streamlit app will be launched in your web browser. The app will have a sidebar with three options:

 - ```Upload```: Clicking on the "Upload" option allows you to upload a CSV file with your dataset. Once the file is uploaded, it displays the datafarame.

 - ```Profile Report```: Clicking on the "Profile Report" option generates an automated EDA report using the pandas-profiling library. You can download the report as an HTML file by clicking the "Download Report" button.

 - ```Automatic Model Training```: Selecting the "Automatic Model Training" option will train an automatic machine learning model using the ```Pycaret Library```. You will need to select a target feature and a problem type (regression or classification) in the sidebar. The app will then train an automatic machine learning model using the pycaret library and display a table with the performance metrics of several models. You can download the best model as a pickle file by clicking the "Download Model" button.

```sh
Note: The app requires a CSV file as input. Make sure to have a CSV file ready before running the app.
```

# Contributing
If you find a bug or have a feature request, please open an issue on this repository. Pull requests are also welcome.

# License
This Repository licensed under the MIT License. See the LICENSE file for more information.
