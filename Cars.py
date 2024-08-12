import streamlit as st 
import pandas as pd
import pickle 

# Load the saved data using pickel
model_path = 'C:/Users/user/Documents/Data Science/Models/Diabetes and Car/Car/Car Prediction Model 1.sav'
with open (model_path, 'rb')as file:
    model = pickle.load(file)



# Initialize the input fields in Streamlit
st.title('Car price Prediction Model')
st.write('Input Some Information to Predict the price of your vehicle')

# Create Sidebar to input details or features
st.sidebar.title('Input The Featues Of Your Car')
st.sidebar.title('Fill in the details below')

# Input Fields
# List of encoded car names (0 to 9)
encoded_car_names = list(range(0, 10))

# # Use st.sidebar.selectbox to select an encoded car name
# car_Name = st.sidebar.selectbox('Car_Name', options=encoded_car_names, index=0)
# year = st.sidebar.slider('Year', min_value=2003, max_value=2018, value=2018)
# Present_Price = st.sidebar.slider('Present Price (in thousands)', min_value=0.0, max_value=100.0, value=5.59)
# kms_driven = st.sidebar.slider('Kms Driven', min_value=0, max_value=100000, value=27000)
# fuel_type = st.sidebar.selectbox('Fuel Type', options=['Petrol', 'Diesel'])
# seller_type = st.sidebar.selectbox('Seller Type', options=['Dealer', 'Individual'])
# transmission = st.sidebar.selectbox('Transmission', options=['Manual', 'Automatic'])
# owner = st.sidebar.selectbox('Owner', options=[0, 1, 2, 3]

car_name = st.sidebar.selectbox('Car_Name', options=encoded_car_names, index=0)
year = st.sidebar.slider('Year', min_value=2000, max_value=2023, value=2014)
present_price = st.sidebar.slider('Present Price (in thousands)', min_value=0.0, max_value=100.0, value=5.59)
kms_driven = st.sidebar.slider('Kms Driven', min_value=0, max_value=100000, value=27000)
fuel_type = st.sidebar.selectbox('Fuel Type', options=['Petrol', 'Diesel'])
seller_type = st.sidebar.selectbox('Seller Type', options=['Dealer', 'Individual'])
transmission = st.sidebar.selectbox('Transmission', options=['Manual', 'Automatic'])
owner = st.sidebar.selectbox('Owner', options=[0, 1, 2, 3])

# Convert categorical variables to numerical values if needed
# You may need to encode these as your model requires
fuel_type_encoded = 1 if fuel_type == 'Diesel' else 0
seller_type_encoded = 1 if seller_type == 'Individual' else 0
transmission_encoded = 1 if transmission == 'Automatic' else 0

# Create a DataFrame with all features (excluding Selling_Price)
input_data = pd.DataFrame({
    'Car_Name': [car_name],
    'Year': [year],
    'Present_Price': [present_price],  # in thousands
    'Kms_Driven': [kms_driven],
    'Fuel_Type': [fuel_type_encoded],
    'Seller_Type': [seller_type_encoded],
    'Transmission': [transmission_encoded],
    'Owner': [owner]
})

# Predict Button
if st.button('Predict'):
    try:
        # Make the prediction
        prediction = model.predict(input_data)
        
        # Convert the predicted price from thousands to millions
        predicted_price_million = prediction[0] * 1_000_000

        # Display the prediction with increased font size
        st.subheader('Prediction:')
        st.write(f"Predicted Selling Price: ${predicted_price_million:.2f}")

    except Exception as e:
        st.write(f"Error: {e}")