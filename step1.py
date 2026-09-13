from google import genai
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv() #find .env file
load_dotenv(dotenv_path) #return True if there is envir vars

API_KEY = os.getenv("API_KEY")
