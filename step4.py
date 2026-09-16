from dotenv import load_dotenv
import os
from google import genai

from google.genai import types

load_dotenv()

MODEL = os.getenv("MODEL_NAME")

client = genai.Client(api_key=os.getenv("API_KEY"))

from pydantic import BaseModel

class RecipeStep(BaseModel):
    step_number: int
    instruction: str

class Recipe(BaseModel):
    name: str
    steps: list[RecipeStep]

response = client.models.generate_content(
    model=MODEL,
    contents="Give me a simple recipe for shakshuka.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Recipe, #json contain {"name":...,"steps":list of steps (another json)}
    ),
)

"""
{
  "name": "Shakshuka",
  "steps": [
    {
      "step_number": 1,
      "instruction": "Heat olive oil in a large pan."
    },
    {
      "step_number": 2,
      "instruction": "Cook the onion and bell pepper."
    },
    {
      "step_number": 3,
      "instruction": "Add tomatoes and simmer."
    },
    {
      "step_number": 4,
      "instruction": "Crack the eggs into the sauce and cook."
    }
  ]
}
"""

recipe: Recipe = response.parsed  # already a validated Pydantic object
print(recipe.name, len(recipe.steps))