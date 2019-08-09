# Movie classifier API

"""
Parse and POST the input strings to the movie classifier API
"""

import requests
import argparse
import joblib
import json

import text_wrangling_util

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Movie genre classifier predicts a movie's genre from its title and plot description. " +
    "Try: python3 movie_classifier.py --title \"The Matrix\" --description \"In the distant future, a hacker Neo " +
    " realizes he is part of a simulation called Matrix and he needs to save the surviving humans by fighting bad programs.\"")

    parser.add_argument("-t", "--title", help="English title of the movie", type=str)
    parser.add_argument("-d", "--description", help="Short description of the plot", type=str)

    args = parser.parse_args()

    url = 'http://localhost:5000/api'
    r = requests.post(url, json = {"title" : args.title, "description": args.description})

    print(json.dumps(r.json(),indent=4))
