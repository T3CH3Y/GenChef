from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "OPENAI_KEY" : os.environ["OPENAI_KEY"],
    "WEAVIATE_KEY" : os.environ["WEAVIATE_KEY"],
    "OPENAI_MODEL" : "gpt-3.5-turbo",
    "WEAVIATE_URL" : "https://gen-chef-grbe0axw.weaviate.network/"
}