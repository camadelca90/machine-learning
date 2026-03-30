Machine Learning App – House Price Prediction

This project is a Machine Learning web application developed using Flask and Scikit-learn.  
The main objective is to predict house prices using Linear Regression.

Project Description

The application allows users to enter property characteristics such as:

- Area
- Number of rooms
- Bathrooms
- Location features

Based on this data, the system predicts the estimated house price.

This project was developed as part of an academic activity to understand supervised learning and linear regression concepts.

Machine Learning Type

- Supervised Learning
- Regression Problem
- Algorithm: Linear Regression

---

Dataset

The dataset contains real-estate related features such as:

- Size (m²)
- Number of bedrooms
- Number of bathrooms
- Price

Data preprocessing steps include:

- Cleaning missing values
- Feature selection
- Model training and evaluation

Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn
- Bootstrap
- HTML / CSS

How to Run the Project

Clone the repository

bash
git clone https://github.com/camadelca90/machine-learning.git

Project Structure

machine-learning/
│
├── app.py
├── house_price.py
├── requirements.txt
├── logistic_regression/
│   └── dataset_precios_inmuebles.xlsx
│
├── templates/
│   ├── home.html
│   ├── linear_regression.html
│   ├── form.html
│
└── static/
    └── images/

Machine Learning Model

The project uses a Linear Regression model implemented with Scikit-learn.

Steps:

- Load dataset using Pandas
- Select relevant features
- Train model using LinearRegression()
- Predict house price from user input
