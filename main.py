from typing import List, Dict
import json
import os

TODO_FILE = "todos.json"

def load_todos() -> List[Dict]:
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_todos(todos: List[Dict]):
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        json.dump(todos, file, indent=2, ensure_ascii=False)

def add_todo(title: str):
    todos = load_todos()
    todos.append({"title": title, "completed": False})
    save_todos(todos)
    print(f"✅ Dodano: {title}")

def list_todos():
    todos = load_todos()
    if not todos:
        print("🔍 Lista zadań jest pusta.")
        return
    print("📝 Lista zadań:")
    for i, todo in enumerate(todos, start=1):
        status = "✅" if todo["completed"] else "❌"
        print(f"{i}. [{status}] {todo['title']}")

def toggle_todo(index: int):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos[index]["completed"] = not todos[index]["completed"]
        save_todos(todos)
        print(f"🔄 Zmieniono status: {todos[index]['title']}")
    else:
        print("🚫 Nieprawidłowy numer zadania.")

def main():
    while True:
        print("\nWybierz opcję:")
        print("1. Dodaj zadanie")
        print("2. Pokaż zadania")
        print("3. Zmień status zadania")
        print("0. Wyjście")

        choice = input("➤ Wpisz numer opcji: ").strip()

        if choice == "1":
            title = input("Wpisz treść zadania: ")
            add_todo(title)
        elif choice == "2":
            list_todos()
        elif choice == "3":
            list_todos()
            try:
                idx = int(input("Podaj numer zadania: ")) - 1
                toggle_todo(idx)
            except ValueError:
                print("⚠️ Wpisz prawidłowy numer.")
        elif choice == "0":
            print("👋 Do zobaczenia!")
            break
        else:
            print("🚫 Nieznana opcja.")

if __name__ == "__main__":
    main()