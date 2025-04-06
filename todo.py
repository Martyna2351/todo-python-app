from typing import List, Dict
import json
import os

# Nazwa pliku do zapisu zadań
TODO_FILE = "todos.json"

# Wczytuje zadania z pliku JSON, jeśli plik istnieje
def load_todos() -> List[Dict]:
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

# Zapisuje listę zadań do pliku JSON
def save_todos(todos: List[Dict]):
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        json.dump(todos, file, indent=2, ensure_ascii=False)

# Dodaje nowe zadanie
def add_todo(title: str):
    todos = load_todos()
    todos.append({"title": title, "completed": False})
    save_todos(todos)
    print(f"✅ Dodano: {title}")

# Wyświetla wszystkie zadania
def list_todos():
    todos = load_todos()
    if not todos:
        print("🔍 Lista zadań jest pusta.")
        return
    print("📝 Lista zadań:")
    for i, todo in enumerate(todos, start=1):
        status = "✅" if todo["completed"] else "❌"
        print(f"{i}. [{status}] {todo['title']}")

# Zmienia status (zrobione/niezrobione) zadania na podstawie indeksu
def toggle_todo(index: int):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos[index]["completed"] = not todos[index]["completed"]
        save_todos(todos)
        print(f"🔄 Zmieniono status: {todos[index]['title']}")
    else:
        print("🚫 Nieprawidłowy numer zadania.")

# Główna pętla programu (interfejs tekstowy)
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
