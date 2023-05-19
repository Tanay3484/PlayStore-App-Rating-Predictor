import streamlit as st
#import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle

# Load the trained model
model = pickle.load(open("Forest_Regressor","rb"))

# Define the label encodings
category_encodings = {'Lifestyle': 0, 'Family': 1, 'Travel': 2, 'Entertainment': 3, 'Home and Decor': 4, 'Education and Business': 5}
content_rating_encodings = {'Everyone': 0, 'Teen': 1, 'Everyone 10+': 2, 'Mature 17+': 3, 'Adults only 18+': 4}

# Create a standard scaler
scaler = StandardScaler()

# Streamlit application
def main():
    st.title("App Rating Prediction")
    st.write("Please provide the following details:")

    feature_names = ['Category', 'Reviews', 'Type', 'Price', 'Content Rating']

    # Category input
    category = st.selectbox("Category", list(category_encodings.keys()))

    # Reviews input
    reviews = st.number_input("Reviews", step=1.0)

    # Type input
    app_type = st.selectbox("Type", ["Free", "Paid"])

    # Price input
    price = st.number_input("Price")

    # Content Rating input
    content_rating = st.selectbox("Content Rating", list(content_rating_encodings.keys()))

    # Predict button
    if st.button("Predict"):
        # Preprocess the input data
        category_encoded = category_encodings[category]
        content_rating_encoded = content_rating_encodings[content_rating]
        app_type_encoded = 1 if app_type == "Paid" else 0

        # Scale the numerical features
        reviews_scaled = scaler.fit_transform([[reviews]])[0][0]
        price_scaled = scaler.transform([[price]])[0][0]

        # Prepare the input data for prediction
        input_data = np.array([[category_encoded, reviews_scaled, app_type_encoded, price_scaled, content_rating_encoded]])

        # Make the prediction
        predicted_rating = model.predict(input_data)[0]

        predicted_rating = round(predicted_rating,2)

        # Display the predicted rating
        st.success("Your app's predicted rating is: {}".format(predicted_rating))


if __name__ == "__main__":
    main()