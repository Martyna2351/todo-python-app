import todo
import os

def test_add_and_toggle():
    test_file = "test_todos.json"
    todo.TODO_FILE = test_file  # Użyj pliku testowego

    # Test dodawania
    todo.add_todo("Zrobić testy")
    todos = todo.load_todos()
    assert len(todos) == 1
    assert todos[0]["title"] == "Zrobić testy"
    assert todos[0]["completed"] == False

    # Test zmiany statusu
    todo.toggle_todo(0)
    todos = todo.load_todos()
    assert todos[0]["completed"] == True

    # Sprzątanie
    os.remove(test_file)
    print("✅ Testy zakończone sukcesem!")

if __name__ == "__main__":
    test_add_and_toggle()
