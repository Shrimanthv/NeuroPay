from flask import Flask, request, render_template
import tensorflow as tf
import pandas as pd
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model('regression.h5')

# Load encoders and scaler
with open('onehotencoder_geo.pkl', 'rb') as f:
    label_encoder_geo = pickle.load(f)

with open('labelencoder_gender.pkl', 'rb') as f:
    label_encoder_gender = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)


@app.route('/')
def home():
    return render_template('index.html',
                           geography_options=label_encoder_geo.categories_[0],
                           gender_options=label_encoder_gender.classes_)


@app.route('/predict', methods=['POST'])
def predict():
    # Extract form data
    geography = request.form['geography']
    gender = request.form['gender']
    age = int(request.form['age'])
    balance = float(request.form['balance'])
    credit_score = float(request.form['credit_score'])
    tenure = int(request.form['tenure'])
    num_of_products = int(request.form['num_of_products'])
    has_cr_card = int(request.form['has_cr_card'])
    is_active_member = int(request.form['is_active_member'])
    exited = int(request.form['exited'])

    # Encode gender
    gender_encoded = label_encoder_gender.transform([gender])[0]

    # Encode geography using one-hot encoder
    geo_encoded = label_encoder_geo.transform([[geography]]).toarray()
    geo_encoded_df = pd.DataFrame(geo_encoded, columns=label_encoder_geo.get_feature_names_out(['Geography']))

    # Create DataFrame
    input_data = pd.DataFrame({
        'CreditScore': [credit_score],
        'Gender': [gender_encoded],
        'Age': [age],
        'Tenure': [tenure],
        'Balance': [balance],
        'NumOfProducts': [num_of_products],
        'HasCrCard': [has_cr_card],
        'IsActiveMember': [is_active_member],
        'Exited': [exited]
    })

    # Combine all features
    input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

    # Scale the input
    input_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_scaled)[0][0]

    return render_template('result.html', prediction=round(prediction, 2))


if __name__ == '__main__':
    app.run(debug=True)
