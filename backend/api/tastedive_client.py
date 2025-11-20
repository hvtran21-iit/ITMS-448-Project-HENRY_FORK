import requests
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from repo root
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)
#get API key from .env
API_KEY = os.getenv("TASTEDIVE_API_KEY")
BASE_URL = "https://tastedive.com/api/similar"
# run query based on technically any type of media, but we use it to query songs and pull movies
def search_tastedive(query, media_type):
    """
    Query TasteDive for a given search term and type.
    media_type can be: 'music', 'movie', 'show', 'book', 'author', etc.
    """
    
    if media_type.lower() == "movies":
        media_type = "movie"

    params = {
        "q": query,  # requests handles URL encoding
        "type": media_type,
        "k": API_KEY,
        "limit": 10
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()
