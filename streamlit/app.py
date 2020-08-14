from predict import process

import streamlit as st
import os

st.title(f"Ma première WebAPP ML")

# fastapi endpoint
# Run en local docker-compose
# url = 'http://fastapi:8000'
url = 'https://honchoappgender.herokuapp.com'
prefix = '/gender'
endpoint = '/predict_gender'

server_url = url + prefix + endpoint

st.subheader('Questions fermées')
favorite_color_list = ['Cool', 'Neutral', 'Warm']
color = st.selectbox(
    label='What is your Favorite Kind of Color ?',
    options=favorite_color_list
)

favorite_music_list = ['Rock', 'Hip hop', 'Folk/Traditional', 'Jazz/Blues', 'Pop', 'Electronic', 'R&B and soul']
music = st.selectbox(
    label='What is your Favorite Kind of Music ?',
    options=favorite_music_list
)

favorite_beverage_list = ['Vodka', 'Wine', 'Whiskey', 'Doesnt drink', 'Beer', 'Other']
beverage = st.selectbox(
    label='What is your Favorite Beverage (alcohol) ?',
    options=favorite_beverage_list
)

favorite_drink_list = ['7UP/Sprite', 'Coca Cola/Pepsi', 'Fanta', 'Other']
soft_drink = st.selectbox(
    label='What is your Favorite soft drink ?',
    options=favorite_drink_list
)

response_dict = {"Favorite Color": color,
                 "Favorite Music Genre": music,
                 "Favorite Beverage": beverage,
                 "Favorite Soft Drink": soft_drink}
if st.button('Predict !'):
    results = process(response_dict, server_url)
    st.write(results)
