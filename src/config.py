from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "OPENAI_KEY" : os.environ("OPENAI_KEY")
}