import streamlit as st
import openai
from config import config
import os
import sys

openai.api_key = config["OPENAI_KEY"]



if __name__ == "__main__":
    st.title("Let GenChef Help You Make The Most Of Your Ingredients")
    st.image("graphix/genchef.png")
    query = st.text_input(label = "Tell the chef what you're working with.")
<<<<<<< HEAD
    dish_image = openai.Image.create(prompt = query, n = 1, size = "256x256")
    dish_image_clean = dish_image['data'][0]['url']
    st.image(dish_image_clean)
=======
    dish_image = openai.Image.create
    
>>>>>>> parent of 3a1b163 (query stuff)

