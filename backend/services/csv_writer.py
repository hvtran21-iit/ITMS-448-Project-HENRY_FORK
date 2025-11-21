import csv
import os

#this file makes sure the data values are written correctly to a csv file in the repo. If the csv file cannot be found, it makes a new one
CSV_PATH = "data/recommend.csv"

HEADER = {
    "song_title", 
    "song_artist",
    "song_genre", 
    "movie-title",
    "movie_director", 
    "movie_genre", 
    "movie_year",
    "movie_plot"
}

def append_row(row: dict):
    #create folder if need for CSV
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
    #check if file exists
    file_exists = os.path.isfile(CSV_PATH)

    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADER)

        #make sure header is only written once
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)