import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "passwords.json")


def load_profiles():
    """
    Load all saved profiles.

    Returns an empty list if the JSON file
    does not exist or is invalid.
    """

    if not os.path.exists(FILE_PATH):
        return []

    try:

        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return []


def save_profiles(profile_list):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(profile_list, file, indent=4, ensure_ascii=False)