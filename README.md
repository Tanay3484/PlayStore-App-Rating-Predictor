# Google Playstore App Rating Prediction

---

Dataset Used : https://www.kaggle.com/datasets/lava18/google-play-store-apps

---

This application uses a machine learning model trained using the Random Forest Regressor in order to predict the ratings of an application based on the following criteria :

- Category          
- Rating            
- Reviews           
- Type              
- Price             
- Content Rating

The ipynb shows the training of the model and the Forest_Regressor is the binary file of the model which is used in the frontend described in the app.py to perform predictions using the user's entries.

The frontend is built using a library called Streamlit.

Steps to run the application : 

Step 1 : 
```console
git clone https://github.com/Tanay3484/PlayStore-App-Rating-Predictor.git
```

Step 2 : 
```console
cd playstore-app-rating-predictor
```

Step 3 : 
```console
pip install -r requirements.txt
```

Step 4 : 
```console
streamlit run app.py
```

Step 5: 
The application should open automatically on the local browser. You can use it from there.

Thank you!