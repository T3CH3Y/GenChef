import weaviate
import json

client = weaviate.Client(
    url = "https://gen-chef-grbe0axw.weaviate.network/",  # Replace with your endpoint
    auth_client_secret=weaviate.AuthApiKey(api_key="rF9pAPONKDg6HyxoP7f0Q4iC3A5MRdIiLaZW"),  # Replace w/ your Weaviate instance API key
    additional_headers = {
        "X-OpenAI-Api-Key": "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"  # Replace with your inference API key
    }
)

response = (
    client.query
    .get("Recipe", ["name", "keywords", "ingredients"])
    .with_near_text({"concepts": ["white rice", "butter", "chicken"]})
    .with_limit(10)
    .do()
)

print(json.dumps(response, indent=4))