from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

def get_api_key():
    return os.getenv("HUGGINGFACE_API_KEY")

def load_config(path="config.json"):
    with open(path, "r") as f:
        return json.load(f)
