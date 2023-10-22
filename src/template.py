import weaviate
import openai
from config import config

from llama_index import SimpleDirectoryReader
from llama_index.node_parser import SimpleNodeParser
from llama_index.vector_stores import WeaviateVectorStore
from llama_index import VectorStoreIndex, StorageContext

client = weaviate.Client(
    url = "https://my-sandbox-csjz1k6w.weaviate.network",  # Replace with your endpoint
    auth_client_secret=weaviate.AuthApiKey(api_key=config["WEAV_KEY"]),  # Replace w/ your Weaviate instance API key
    additional_headers = {
        "X-OpenAI-Api-Key": config["OPENAI_KEY"]
    }
)
openai.api_key = config["OPENAI_KEY"]

# load the blogs in using the reader

# chunk up the blog posts into nodes
parser = SimpleNodeParser.from_defaults(chunk_size=1024, chunk_overlap=20)


# construct vector store
vector_store = WeaviateVectorStore(weaviate_client = client, index_name="BlogPost", text_key="content")

# setting up the storage for the embeddings
storage_context = StorageContext.from_defaults(vector_store = vector_store)

# set up the index


query_engine = index.as_query_engine()
response = query_engine.query("What is the intersection between LLMs and search?")
print(response)