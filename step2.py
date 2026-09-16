from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

MODEL = os.getenv("MODEL_NAME")

client = genai.Client(api_key=os.getenv("API_KEY"))

response = client.models.generate_content(
    model=MODEL,
    contents="Summarize the key steps of an MLOps pipeline.",
    config=types.GenerateContentConfig(
        system_instruction="You are a concise MLOps mentor for engineering students.",
        temperature=0.4,
        max_output_tokens=300,
    ),
)
print(response.text)
