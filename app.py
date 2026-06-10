# Adam Santos 6/9/2026

# Might have to swap out OpenAI for Gemini
# Will come back to this later, likely will be
# an irritating process to swap code-wise
import streamlit as st
import warnings
# from langchain import LLMChain

# Was originally: langchain.prompts import PromptTemplate
# could cause problems later
from langchain_core.prompts import PromptTemplate

# Was originally langchain.llms but swapped to langchain.chat_models
# could cause problems later
from langchain_google_genai import ChatGoogleGenerativeAI

from recipe_generation import recipe_chain

warnings.filterwarnings("ignore")

template = """
You are a chef who is extremely adaptable and capable when it comes to creating multilple types of dishes with just a few ingredients.
Please create a recipe using the following ingredients: {ingredients}
The recipe should just display the amount of ingredients and instructions on how to make the dish."""

prompt = PromptTemplate(
    input_variables=["ingredients"],
    template=template
)

# Might have to change this later
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", temperature=0.9, max_tokens=30000)

recipe_generator = recipe_chain

st.title("Ai Recipe Creator")

st.divider()

st.write("Welcome to the AI Recipe Creator! This app uses the power of AI to generate delicious recipes based on your preferences. Whether you're looking for a quick weeknight meal or a gourmet dish, simply input your desired ingredients and let the AI do the rest. Get ready to discover new culinary delights and impress your friends and family with your cooking skills!")

ingredients = st.text_area("Ingredients")

if st.button("Generate a Recipe"):
    if ingredients:
        recipe = recipe_generator.invoke(ingredients)
        st.subheader("Generated Recipe")
        st.write(recipe)
    else:
        st.error("Please enter some ingredients to generate a recipe.")
