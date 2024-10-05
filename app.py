import streamlit as st
import numpy as np
import pickle
with open('house_price_model.pkl', 'wb') as file:
    pickle.dump(model, file)


st.title("House Price Prediction App")

area = st.number_input("Area (in square feet)", min_value=500, max_value=10000, step=100)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, step=1)
stories = st.number_input("Number of Stories", min_value=1, max_value=5, step=1)
mainroad = st.selectbox("Main Road Access", options=["yes", "no"])
guestroom = st.selectbox("Guestroom Available", options=["yes", "no"])
basement = st.selectbox("Has Basement", options=["yes", "no"])
hotwaterheating = st.selectbox("Hot Water Heating", options=["yes", "no"])
airconditioning = st.selectbox("Air Conditioning", options=["yes", "no"])
parking = st.number_input("Parking Spaces", min_value=0, max_value=5, step=1)
prefarea = st.selectbox("Preferred Area", options=["yes", "no"])
furnishingstatus = st.selectbox("Furnishing Status", options=["furnished", "semi-furnished", "unfurnished"])


mainroad = 1 if mainroad == 'yes' else 0
guestroom = 1 if guestroom == 'yes' else 0
basement = 1 if basement == 'yes' else 0
hotwaterheating = 1 if hotwaterheating == 'yes' else 0
airconditioning = 1 if airconditioning == 'yes' else 0
prefarea = 1 if prefarea == 'yes' else 0

furnishingstatus_dict = {"furnished": 2, "semi-furnished": 1, "unfurnished": 0}
furnishingstatus = furnishingstatus_dict[furnishingstatus]

features = np.array([[area, bedrooms, bathrooms, stories, mainroad, guestroom,
                      basement, hotwaterheating, airconditioning, parking,
                      prefarea, furnishingstatus]])


if st.button("Predict House Price"):
    prediction = model.predict(features)
    st.success(f"Estimated House Price: ₹{prediction[0]:,.2f}")


# st.markdown("---") 
# st.markdown("Made by **Ishatva Singh Panwar**")
