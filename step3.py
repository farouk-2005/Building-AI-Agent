from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

import PIL.Image

load_dotenv()

MODEL = os.getenv("MODEL_NAME")

client = genai.Client(api_key=os.getenv("API_KEY"))

img = PIL.Image.open("img.jpg")

response = client.models.generate_content(
    model=MODEL,
    contents=["What does this photo show?", img],
    config=types.GenerateContentConfig(
        max_output_tokens=300,
    )
)
print(response.text)