import textwrap
import pathlib
import requests
import PIL.Image
from flask import Flask, render_template, redirect


app = Flask(__name__)

import google.generativeai as genai
GOOGLE_API_KEY = "AIzaSyDQkFoW96TA2eIl2SiAx6L3gqVAXVT0Dp0"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro-vision')

def classify_image(img):
    response = model.generate_content(["In 2 words return what is the food?",img], stream = True)
    response.resolve()
    return response.text

def index():
    return render_template("Home.html")

@app.route("/classify", methods=["POST"])
def classify():
    pass
    






spoonacular = "https://api.spoonacular.com/recipes/complexSearch"

params = {
    "apiKey": "13ee048810644849b4beadcb08d1c1b2",
    "query": response.text
}

recipes = requests.get(spoonacular, params=params)

if recipes.status_code == 200 :
    data = recipes.json()

for i in range(len(data['results'])):
    id = data['results'][i]['id']
    print(data['results'][i]['id'], data['results'][i]['title'])
    stepByStep = f"https://api.spoonacular.com/recipes/{id}/information?apiKey=13ee048810644849b4beadcb08d1c1b2&includeNutrition=true"
    print("Recipe: ", stepByStep)


