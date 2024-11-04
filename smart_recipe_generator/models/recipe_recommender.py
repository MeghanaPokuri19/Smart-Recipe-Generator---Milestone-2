import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_recipe_suggestion(ingredients):
    prompt = f"Suggest a recipe using the following ingredients: {', '.join(ingredients)}"
    
    # Update the API call to use gpt-3.5-turbo, which requires `messages` instead of `prompt`
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for generating recipes."},
            {"role": "user", "content": prompt}
        ]
    )
    
    # Extract the response text
    return response.choices[0].message["content"].strip()
