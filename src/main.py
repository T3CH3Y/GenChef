import streamlit as st
import openai
from config import config
from template import callchef
import os
import sys

openai.api_key = config["OPENAI_KEY"]
openai_text = config["OPENAI_MODEL"]



if __name__ == "__main__":
    st.title("Let GenChef Help You Make The Most Of Your Ingredients")
    st.image("graphix/genchef.png")
    query = st.text_input(label = "Tell the chef what you're working with.", value = "Saltines and Tomatoes")
    
    text_prompt_head = "You are a helpful chef that will provide step-by-step recipes based primary around the ingredients and styles specified here: "
    text_prompt = text_prompt_head + query
    gpt_gen = callchef(text_prompt)
    
    image_prompt_head = "Generate a commercial-grade image of a dish composed of the following recipe: "
    com_prompt = image_prompt_head + gpt_gen
    dish_image = openai.Image.create( prompt = com_prompt, n = 1, size = "256x256")
    dish_image_clean = dish_image['data'][0]['url']

    st.image(dish_image_clean)
    st.write(gpt_gen)
