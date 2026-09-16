from dotenv import load_dotenv
import os
from google import genai

from google.genai import types

load_dotenv()

MODEL = os.getenv("MODEL_NAME")

client = genai.Client(api_key=os.getenv("API_KEY"))

# Function calling (tools)
def get_current_weather(location: str) -> str:
    """Returns the current weather for a given city."""
    return f"It's sunny and 27°C in {location}."

response = client.models.generate_content(
    model=MODEL,
    contents="What's the weather like in Sfax right now?",
    config=types.GenerateContentConfig(tools=[get_current_weather]),
)
print(response.text)
