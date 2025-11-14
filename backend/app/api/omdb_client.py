import requests 
import os

class OMDBClient:
    BASE_URL = "https://www.omdbapi.com/"
    

    def __init__(self):
        self.api_key = os.getenv("OMDB_API_KEY")
        if not self.api_key:
            raise ValueError("OMDB_API_KEY not found in .env")
        
    def get_movie_details(self, title):
        params = { 
            "t": title,
            "plot": "full",
            "apikey": self.api_key
        }
        return requests.get(self.BASE_URL, params=params).json()
    
    def get_by_id(self, imdb_id):
        params = {
            "i": imdb_id,
            "plot": "full",
            "apikey": self.api_key
        }
        return requests.get(self.BASE_URL, params=params).json()
