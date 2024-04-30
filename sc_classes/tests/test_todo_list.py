from lib.todo_list import  TodoList


def test_initially_incomplete_tasks():
    todo_list = TodoList()
    assert todo_list.incomplete() == []


def test_initially_complete_tasks():
    todo_list = TodoList()
    assert todo_list.complete() == []
