from lib.todo import Todo
from lib.todo_list import TodoList

'''
Adds new todo to 
incomplete tasks list
'''


def test_adds_todo_to_incomplete_tasks_list():
    todo_list = TodoList()
    task_1 = Todo("Grocery")
    todo_list.add(task_1)
    incomplete_tasks = [task.task for task in todo_list.incomplete()]
    assert incomplete_tasks == ["Grocery"]


'''
Adds complete todo to 
complete tasks list
'''


def test_adds_todo_to_complete_tasks_list():
    todo_list = TodoList()
    task_1 = Todo("Call mama")
    task_2 = Todo(" House Clean")
    todo_list.add(task_1)
    todo_list.add(task_2)
    task_1.mark_complete()
    complete_tasks = [task.task for task in todo_list.complete()]
    assert complete_tasks == ["Call mama"]


def test_marks_all_tasks_as_complete():
    todo_list = TodoList()
    task_1 = Todo("Task one")
    task_2 = Todo("Task two")
    task_3 = Todo("Task three")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    todo_list.give_up()
    complete_tasks = [task.task for task in todo_list.complete()]
    assert complete_tasks == ["Task one", "Task two", "Task three"]
