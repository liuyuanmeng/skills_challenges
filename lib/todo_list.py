from lib.todo import Todo


class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        # Check if the todo is an instance of Todo
        if isinstance(todo, Todo):
            self.todos.append(todo)
        else:
            raise ValueError("Only instances of Todo can be added to the list")

    def incomplete(self):
        return [todo for todo in self.todos if not todo.complete]

    def complete(self):
        return [todo for todo in self.todos if todo.complete]

    def give_up(self):
        for todo in self.todos:
            todo.mark_complete()


#  Create an instance of TodoList
todo_list = TodoList()

# Add some todo items
todo_list.add(Todo("Complete homework"))
todo_list.add(Todo("Read a book"))
todo_list.add(Todo("Go for a run"))

print("Incomplete Todo Items:")
for todo in todo_list.incomplete():
    print(todo.task)

# Print out the complete todo items
print("\nComplete Todo Items:")
for todo in todo_list.complete():
    print(todo.task)
