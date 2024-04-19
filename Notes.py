import json
import os

notes = []


def load_notes():
    global notes
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes = json.load(file)


def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)

