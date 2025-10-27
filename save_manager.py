import json
import os

SAVE_PATH = "saves/saved_data.json"

# ---checks if a save exists---
def save_exists():
    return os.path.exists(SAVE_PATH)

def load_save():
    if not save_exists():
        return None
    with open(SAVE_PATH, 'r') as f:
        return json.load(f)

def save_game(data):
    os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
    with open(SAVE_PATH, 'w') as f:
        return json.dump(data, f)