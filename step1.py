from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
MODEL = os.getenv("MODEL_NAME")

client = genai.Client(api_key=os.getenv("API_KEY"))

response = client.models.generate_content(
    model=MODEL,
    contents="Hi my name is Farouk."
)
print(response.text)

response = client.models.generate_content(
    model=MODEL,
    contents="Hi whats my name."
)
print(response.text)

print(" ===== Multi-turn chat ===== ")

#The chats module keeps conversation history for you automatically:
chat = client.chats.create(model=MODEL)

r1 = chat.send_message("Hi my name is Farouk.")
print(r1.text)

r2 = chat.send_message("Say my name")
print(r2.text)

