import requests
from dotenv import load_dotenv
import os
import random
from typing import List
from llm_call import *
from testVision import cv_model_call


# Load environment variables from .env file
load_dotenv()

# Get the API key from the .env file
api_key = os.getenv("SPOONACULAR_API_KEY")

# Define the ingredients and the Spoonacular API URL
ingredients = cv_model_call()
print(ingredients)
url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=5&apiKey={api_key}"

def execute_recipe_search(ingredients: List[str]) -> None:
    # Make the request
    response = requests.get(url)
    recipe = random.choice(response.json())

    recipe_title = recipe.get('title', 'Untitled Recipe')  # Get recipe title
    recipe_instructions = recipe.get('instructions', 'No instructions provided.')  # Get recipe instructions


    # Prepare the used and missed ingredients and call LLM for each recipe
    used_ingredients = [
        f"{ingredient['name']} ({ingredient['amount']} {ingredient['unit']})"
        for ingredient in recipe['usedIngredients']
    ]
    missed_ingredients = [
        f"{ingredient['name']} ({ingredient['amount']} {ingredient['unit']})"
        for ingredient in recipe['missedIngredients']
    ]

    # Combine used and missed ingredients into a prompt
    used_str = ", ".join(used_ingredients)
    missed_str = ", ".join(missed_ingredients)

    # Debug prints to check used and missed ingredients
    print(f"Used Ingredients: {used_str}")
    print(f"Missed Ingredients: {missed_str}")

    # Create the prompt for the LLM
    prompt = (
        f"Here is a recipe for {recipe_title}: \n\n"
        f"{recipe_instructions}\n\n"
        f"Used ingredients: {used_str}. \n"
        f"Missing ingredients: {missed_str}. \n"
        f"Please reformat the recipe in a user-friendly way and provide substitutions for the missing ingredients. "
        f"Only suggest substitutions for key ingredients where necessary, and organize the recipe with headings for ingredients and instructions. "
    )

    # Call the function in llm_call.py to generate a recipe with substitutions
    generate_recipe_with_substitutions(recipe['title'], prompt)

execute_recipe_search(ingredients)
