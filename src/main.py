import streamlit as st
import openai
from config import config
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
    gpt_gen = openai.Completion.create(model=openai_text, prompt = text_prompt, max_tokens = 1000)
    gpt_gen_clean = gpt_gen['choices'][0]['text']
    
    image_prompt_head = "Generate a commercial-grade image of a dish composed of the following ingredients and styles: "
    com_prompt = image_prompt_head + query
    dish_image = openai.Image.create( prompt = com_prompt, n = 1, size = "256x256")
    dish_image_clean = dish_image['data'][0]['url']

    st.image(dish_image_clean)
    st.write(gpt_gen_clean)
