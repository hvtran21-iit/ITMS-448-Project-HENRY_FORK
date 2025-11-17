# This code is the start to grab authentication from Spotify to be able to get songs on the website. -Henry

from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

