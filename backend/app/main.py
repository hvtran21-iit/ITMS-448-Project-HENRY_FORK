# This code is the start to grab authentication from Spotify to be able to get songs on the website. -Henry

import numpy as np
import pandas as pd
import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
from fuzzywuzzy import process
import spacy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from typing import Union, List, Dict

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

