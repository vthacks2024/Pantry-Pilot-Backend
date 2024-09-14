import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from the .env file
api_key = os.getenv("SPOONACULAR_API_KEY")

# Define the ingredients and the Spoonacular API URL
ingredients = "apples,flour,sugar"
url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=5&apiKey={api_key}"

# Make the request
response = requests.get(url)
recipes = response.json()

# Print the recipe titles
for recipe in recipes:
    print(recipe)