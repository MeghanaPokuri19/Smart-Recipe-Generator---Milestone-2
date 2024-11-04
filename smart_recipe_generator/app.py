import streamlit as st
from utils.image_processing import load_image, preprocess_image
from utils.ocr_tool import perform_ocr
from models.recipe_recommender import generate_recipe_suggestion
from db.database import connect_db

st.title("Smart Recipe Generator")

st.write("Upload one or more images of products or fruits/vegetables to get recipe suggestions.")
uploaded_files = st.file_uploader("Choose images...", accept_multiple_files=True)

if st.button("Get Recipe"):
    ingredients = []
    for file in uploaded_files:
        img_path = f"assets/sample_images/{file.name}"
        with open(img_path, "wb") as f:
            f.write(file.getbuffer())

        recognized_text = perform_ocr(img_path)
        ingredients.append(recognized_text)

    recipe = generate_recipe_suggestion(ingredients)
    st.write("Generated Recipe:", recipe)
