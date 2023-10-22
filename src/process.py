import json
import re

import pandas as pd

csv_file = 'recipes.csv'

input_json_file = 'output.json'

df = pd.read_csv(csv_file)
df.to_json(input_json_file, orient='records', lines=True)


output_json_file = 'processed_output.json'

processed_data = []

keys_to_remove = ["AuthorId", "AuthorName", "DatePublished", "AggregatedRating", "ReviewCount", "RecipeId", "Images"]

keys_to_update = ["RecipeIngredientParts", "RecipeIngredientQuantities", "Keywords", "RecipeInstructions"]

keys_with_issue = ["recipeServings"]

with open(input_json_file, 'r') as json_file:
    for line in json_file:
        data = json.loads(line)

        for key in keys_to_remove:
            data.pop(key, None)

        for key in keys_to_update:
            value_string = data[key]

            if value_string:
                value_array = re.findall(r'"(.*?)"', value_string)
                data[key] =  value_array

        for key in keys_with_issue:
            data[key] = int(data[key])

        processed_data.append(data)

with open(output_json_file, 'w') as json_file:
    json.dump(processed_data, json_file, indent=4)

