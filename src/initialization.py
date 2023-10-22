import weaviate
import json
import requests

from config import config


client = weaviate.Client(
    url = "https://gen-chef-grbe0axw.weaviate.network/",  # Replace with your endpoint
    auth_client_secret=weaviate.AuthApiKey(api_key=config["WEAVIATE_KEY"]),  # Replace w/ your Weaviate instance API key
    additional_headers = {
        "X-OpenAI-Api-Key": config["OPENAI_KEY"]  # Replace with your inference API key
    }
)

# client.schema.delete_class("Recipe")  # Replace with your class name - e.g. "Question"

# # ===== add schema =====
# class_obj = {
#     "class": "Recipe",
#      'properties': [
#         {
#             'name': 'name',
#             'dataType': ['text'],
#         },
#         {
#             'name': 'cookTime',
#             'dataType': ['text'],
#         },
#         {
#             'name': 'prepTime',
#             'dataType': ['text'],
#         },
#         {
#             'name': 'totalTime',
#             'dataType': ['text'],
#         },
#         {
#             'name': 'description',
#             'dataType': ['text'],
#         },
#         {
#             'name': 'category',
#             'dataType': ['text'],
#         },

#         {
#             'name': 'keywords',
#             'dataType': ['text[]'],
#         },
#         {
#             'name': 'ingredientQuantities',
#             'dataType': ['text[]'],
#         },
#         {
#             'name': 'ingredients',
#             'dataType': ['text[]'],
#         },

#         {
#             'name': 'calories',
#             'dataType': ['number'],
#         },
#         {
#             'name': 'fatContent',
#             'dataType': ['number'],
#         },
#         {
#             'name': 'saturatedFatContent',
#             'dataType': ['number'],
#         },

#         {
#             'name': 'cholesterolContent',
#             'dataType': ['number'],
#         },
#         {
#             'name': 'sodiumContent',
#             'dataType': ['number'],
#         },
#         {
#             'name': 'carbohydrateContent',
#             'dataType': ['number'],
#         },
#         {
#             'name': 'fiberContent',
#             'dataType': ['number'],
#         },
#         {
#             'name': 'sugarContent',
#             'dataType': ['number'],
#         },
#         {
#             'name': 'proteinContent',
#             'dataType': ['number'],
#         },
#         {
#             'name': 'recipeServings',
#             'dataType': ['number'],
#         },

#         {
#             'name': 'recipeYield',
#             'dataType': ['text'],
#         },

#         {
#             'name': 'recipeInstructions',
#             'dataType': ['text[]'],
#         }
#     ],
#     "vectorizer": "text2vec-openai",  # If set to "none" you must always provide vectors yourself. Could be any other "text2vec-*" also.
#     "moduleConfig": {
#         "text2vec-openai": {},
#         "generative-openai": {}  # Ensure the `generative-openai` module is used for generative queries
#     }
# }

# client.schema.create_class(class_obj)

# ===== import data =====

file_path = 'output_processed.json'

with open(file_path, 'r') as json_file:
    data = json.load(json_file)


client.batch.configure(batch_size=100)  # Configure batch
with client.batch as batch:  # Initialize a batch process
    for i, d in enumerate(data):  # Batch import data
        print(f"importing recipe: {i+1}")
        properties = {
            "name": d["Name"],
            "cookTime": d["CookTime"],
            "prepTime": d["PrepTime"],
            "totalTime": d["TotalTime"],

            "description": d["Description"],

            "category": d["RecipeCategory"],

            "keywords": d["Keywords"],

            "ingredientQuantities": d["RecipeIngredientQuantities"],

            "ingredients": d["RecipeIngredientParts"],

            "calories": d["Calories"],

            "fatContent": d["FatContent"],
            "saturatedFatContent": d["CholesterolContent"],
            "cholesterolContent": d["CholesterolContent"],
            "sodiumContent": d["SodiumContent"],
            "carbohydrateContent": d["CarbohydrateContent"],
            "fiberContent": d["FiberContent"],
            "sugarContent": d["SugarContent"],
            "proteinContent": d["ProteinContent"],
            "recipeServings": d["RecipeServings"],

            "recipeYield": d["RecipeYield"],

            "recipeInstructions": d["RecipeInstructions"]
        }
        batch.add_data_object(
            data_object=properties,
            class_name="Recipe"
        )
