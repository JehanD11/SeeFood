import textwrap
import pathlib
import requests
import PIL.Image

import google.generativeai as genai


GOOGLE_API_KEY = "AIzaSyDQkFoW96TA2eIl2SiAx6L3gqVAXVT0Dp0"

genai.configure(api_key=GOOGLE_API_KEY)


model = genai.GenerativeModel('gemini-pro-vision')

my_url = "https://upload.wikimedia.org/wikipedia/commons/6/65/Dhokla_on_Gujrart.jpg"
img = PIL.Image.open(requests.get(my_url, stream=True).raw)

response = model.generate_content(["In 2 words return what is the food?",img], stream = True)
response.resolve()
print(response.text)



