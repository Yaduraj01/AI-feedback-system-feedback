import json
import os

DATA_FILE = "reviews.json"

def load_reviews():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_reviews(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
