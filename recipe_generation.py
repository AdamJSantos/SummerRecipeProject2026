from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import os

from apikey import gemini_api_key

# API KEY
os.environ["GEMINI_API_KEY"] = gemini_api_key

# prompt for LLMChain
template = """You are a chef who is extremely adaptable and capable when it comes to creating multilple types of dishes with just a few ingredients.
Please create a recipe using the following ingredients: {ingredients}
The recipe should include the name of the dish and a list of the ingredients."""

prompt = PromptTemplate(template=template, input_variables=["ingredients"])

#
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", temperature=0.9, max_tokens=30000)

recipe_chain = prompt | llm | StrOutputParser()


ingredients = "chicken, rice, broccoli, soy sauce, garlic"

recipe = recipe_chain.invoke({"ingredients": ingredients})

print(recipe)
