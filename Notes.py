import json
import os
import datetime

notes = []


def load_notes():
    global notes
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes = json.load(file)


def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)


def create_note():
    id = len(notes) + 1
    title = input("Enter note title: ")
    body = input("Enter note body: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    note = {
        "id": id,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }

    notes.append(note)
    save_notes()
    print("Note created successfully!")


def read_note():
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Body: {note['body']}")
        print(f"Timestamp: {note['timestamp']}")
        print("")


def delete_note():
    id = int(input("Enter note ID to delete: "))
    for note in notes:
        if note["id"] == id:
            notes.remove(note)
            save_notes()
            print("Note deleted successfully!")
            return
    print("Note not found!")


def edit_note():
    id = int(input("Enter note ID to edit: "))
    for note in notes:
        if note["id"] == id:
            note["title"] = input("Enter new title: ")
            note["body"] = input("Enter new body: ")
            note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes()
            print("Note edited successfully!")
            return
    print("Note not found!")


load_notes()

while True:
    print("1. Create note")
    print("2. Read notes")
    print("3. Edit note")
    print("4. Delete note")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        create_note()
    elif choice == "2":
        read_note()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")