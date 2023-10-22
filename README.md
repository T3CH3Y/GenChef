# GenChef
A personal AI chef assistant to make meal planning much simpler. Utilizes over 450,000 real recipes, referenced through a vector databasse, to augment a large language model with retrieval augmented generation to bettter serve customers.

# How to run:

Set your environmental keys in a .env file in the /src directory as below:
export OPENAI_KEY = "YOUR-KEY-HERE"
export WEAVIATE_KEY = "YOUR-KEY-HERE"

How to get an OpenAI Key: https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/
How to get a Weaviate Key: https://weaviate.io/developers/weaviate/configuration/authentication

Install dependencies:
pip install -r requirements.txt

And run this command from the source directory:
streamlit run main.py

And now just run your queries through the UI! It will return images and text.

Make sure to use Python 3.10+


