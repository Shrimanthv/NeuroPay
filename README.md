# NeuroPay--Neural Salary Intelligence: 

## Table of Contents
* [Demo](#demo)
* [Overview](#overview)
* [Motivation](#motivation)
* [Features](#features)
* [Installation](#installation)
* [Tech Stack](#tech-stack)
* [Deployment on Streamlit](#deployment-on-streamlit)
* [Project Structure](#project-structure)
* [Bug / Feature Request](#bug--feature-request)
* [Future Scope](#future-scope)
* [Author](#author)



## Demo
Link: https://aerofare-sdnre5xmvhrukj4nm7yftm.streamlit.app/ 

![](https://github.com/Shrimanthv/NeuroPay/blob/main/Screenshot%202025-05-25%20165937.png?raw=true)

![](https://github.com/Shrimanthv/NeuroPay/blob/main/Screenshot%202025-05-25%20170030.png?raw=true)

## Overview
NeuroPay is an AI-powered salary prediction system that uses an Artificial Neural Network (ANN) regression model to estimate salaries based on user inputs such as experience, education, and job title. Built with Python, Streamlit, and scikit-learn, the application provides accurate and real-time salary predictions through an intuitive web interface. It helps job seekers, HR professionals, and recruiters make informed decisions with data-driven insights.

## Motivation
In today’s competitive job market, understanding fair salary expectations is challenging for both job seekers and employers. Salary transparency is often limited, making it hard to make informed career or hiring decisions. NeuroPay was created to bridge this gap using machine learning—providing accurate salary predictions based on real data. The goal is to empower users with insights that help set realistic expectations and support better negotiation and planning.


## Features

- 📈 Accurate Salary Prediction: Predicts salaries using an Artificial Neural Network (ANN) regression model based on key inputs like experience, education, and job role.

🧠 Machine Learning Powered: Trained on real-world data to deliver reliable and data-driven salary estimates.

💡 User-Friendly Interface: Simple Streamlit web app that allows users to input data and get instant predictions.

📊 Customizable Inputs: Supports a variety of input features to reflect diverse job profiles and industries.

🔄 Real-Time Output: Dynamic prediction with immediate feedback as users adjust input values.


---

## Installation

1. Clone the Repository
```bash
git clone https://github.com/Shrimanthv/NeuroPay.git
cd NeuroPay
```
2. Create and Activate a Virtual Environment
Using conda:

```bash
conda create -n neuropay-env python=3.10
conda activate neuropay-env
```
Or using venv:
```bash

python -m venv neuropay-env
source neuropay-env/bin/activate  # On Windows use: neuropay-env\Scripts\activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Run the Application
```bash
streamlit run app.py

```


## Tech Stack

| Layer          | Tools Used                              |
|----------------|------------------------------------------|
| Frontend       | Streamlit                               |
| Backend        | Python, Scikit-learn, Pandas, NumPy     |
| Model Training | RandomForestRegressor, DecisionTreeRegressor |
| Deployment     | Local (can be extended to Streamlit Cloud, AWS, etc.) |

## Deployment on Streamlit
To deploy this project on Streamlit Cloud, follow these steps:

Sign up or log in to Streamlit.

Connect your GitHub account to Streamlit.

Create a new app by selecting the repository containing your project.

Choose the appropriate Python file (e.g., app.py) as the entry point.

Ensure your repository includes a requirements.txt file with all necessary dependencies.

## Project Structure 
```
NeuroPay/
│
├── app.py                  # Main Streamlit application
├── model.h5                # Trained ANN regression model
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── utils/                  # Helper functions (e.g., data processing)
│   └── preprocess.py
├── data/                   # Sample or processed datasets
│   └── salary_data.csv
└── notebooks/              # Jupyter notebooks for EDA & model training
    └── model_training.ipynb



```
## Bug / Feature Request
If you encounter any bugs or have suggestions for new features, please feel free to open an issue on the GitHub repository.

To report a bug:
Provide a clear description of the problem, steps to reproduce it, and any relevant screenshots or error messages.

To request a feature:
Describe the new functionality you'd like to see and explain how it would improve the project.

Your feedback helps improve AeroFare — thank you for contributing!

## Technologies Used


<img src="https://www.python.org/static/community_logos/python-logo.png" width="150" alt="Python Logo" /> <img src="https://www.tensorflow.org/images/tf_logo_social.png" width="150" alt="TensorFlow Logo" /> <img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg" width="180" alt="Streamlit Logo" /> <img src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width="200" alt="Scikit-learn Logo" /> <img src="https://pandas.pydata.org/static/img/pandas_mark.svg" width="150" alt="Pandas Logo" /> <img src="https://numpy.org/images/logo.svg" width="150" alt="NumPy Logo" />

## Author
Shrimanth V
Email: shrimanthv99@gmail.com
Feel free to reach out for any questions or collaboration!