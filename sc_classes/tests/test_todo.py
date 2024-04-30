from lib.todo import Todo


def test_todo_initialization():
    todo = Todo("Task 1")
    assert todo.task == "Task 1"
    assert todo.complete == False


def test_mark_complete():
    todo = Todo("Task 1")
    todo.mark_complete()
    assert todo.complete == True
