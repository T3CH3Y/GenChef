from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "OPENAI_KEY" : os.environ["OPENAI_KEY"],
    "WEAVIATE_KEY" : os.environ["WEAVIATE_KEY"],
    "OPENAI_MODEL" : "gpt-3.5-turbo-instruct",
    "WEAVIATE_URL" : "https://my-sandbox-csjz1k6w.weaviate.network"
}