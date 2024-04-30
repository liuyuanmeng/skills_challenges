from typing import List, Dict, Union
from typing import List, Dict


class TaskTracker:

    def __init__(self, task_list: List[str]):
        self.task_list = task_list

    def add_task(self, task: str):
        self.task_list.append(task)

    # def mark_task_complete(self, task: str):
    #     if task not in self.task_list:
    #         raise ValueError(f"Task {task} not found in task list")
    #         # print(f"Error: Task '{task}' not found in task list")
    #     self.task_list.remove(task)

    def mark_task_complete(self, task: str):
        try:
            self.task_list.remove(task)
        except ValueError:
            raise ValueError(f"Task {task} not found in task list")


    def show_task_list(self):
        return self.task_list


# task_tracker = TaskTracker([])
# task_tracker.add_task("wash")
# task_tracker.add_task("grocery")
# print(task_tracker.task_list)
# print(task_tracker.mark_task_complete("call mama"))


# class CustomString:
#     def __init__(self, value: str):
#         self.value = value


# class CustomFloat:
#     def __init__(self, value: float):
#         self.value = value


# class CustomContainer:
#     def __init__(self, lst: List[int], dct: Dict[str, Union[int, str]]):
#         self.lst = lst
#         self.dct = dct


# # Usage
# x = CustomContainer([1, 2, 3], {'a': 1, 'b': 'two'})  # No error
# y = CustomContainer([1, 2, 3], {'a': 1, 'b': 2})  # No error
# z = CustomContainer([1, 2, 3], {'a': 1, 'b': 2.5})  # Raises TypeError
