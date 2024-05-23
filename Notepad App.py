# notepad.py

def display_notes(notes):
    print("\nYour Notes:")
    for idx, note in enumerate(notes, 1):
        print(f"{idx}. {note}")

def load_notes(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_notes(filename, notes):
    with open(filename, 'w') as file:
        file.write("\n".join(notes))

def main():
    filename = "notes.txt"
    notes = load_notes(filename)

    while True:
        display_notes(notes)
        print("\nOptions:")
        print("1. Add Note")
        print("2. Delete Note")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            new_note = input("Enter a new note: ")
            notes.append(new_note)
            save_notes(filename, notes)
        elif choice == '2':
            note_num = int(input("Enter the number of the note to delete: "))
            if 1 <= note_num <= len(notes):
                notes.pop(note_num - 1)
                save_notes(filename, notes)
            else:
                print("Invalid number")
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
