# todo.py

def display_todos(todos):
    print("\nYour Todo List:")
    for idx, todo in enumerate(todos, 1):
        print(f"{idx}. {todo}")

def load_todos(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_todos(filename, todos):
    with open(filename, 'w') as file:
        file.write("\n".join(todos))

def main():
    filename = "todos.txt"
    todos = load_todos(filename)

    while True:
        display_todos(todos)
        print("\nOptions:")
        print("1. Add Todo")
        print("2. Remove Todo")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            new_todo = input("Enter a new todo: ")
            todos.append(new_todo)
            save_todos(filename, todos)
        elif choice == '2':
            todo_num = int(input("Enter the number of the todo to remove: "))
            if 1 <= todo_num <= len(todos):
                todos.pop(todo_num - 1)
                save_todos(filename, todos)
            else:
                print("Invalid number")
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
