# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.

# As a user
# So that I can focus on tasks to complete
# I want to mark tasks as complete and have them disappear from the list.
from lib.task_tracker import TaskTracker
import pytest


@pytest.fixture
def test_tracker():
    return TaskTracker([])


def test_task_tracker(test_tracker):
    assert test_tracker.task_list == []


def test_add_task(test_tracker):
    test_tracker.add_task("grocery")
    assert test_tracker.task_list == ["grocery"]


def test_add_multiple_tasks(test_tracker):
    test_tracker.add_task("wash")
    test_tracker.add_task("call mama")
    assert test_tracker.task_list == ["wash", "call mama"]


def test_show_list_of_tasks(test_tracker):
    test_tracker.task_list = ["grocery", "wash", "call mama"]
    assert test_tracker.show_task_list() == test_tracker.task_list


def test_remove_task(test_tracker):
    test_tracker.task_list = ["grocery", "wash", "call mama"]
    test_tracker.mark_task_complete("grocery")
    assert test_tracker.task_list == ["wash", "call mama"]


def test_remove_nonexistent_task(test_tracker):
      test_tracker.task_list = ["grocery", "wash", "call mama"]
      with pytest.raises(ValueError) as err:
        test_tracker.mark_task_complete("shopping")
      assert str(err.value) == "Task shopping not found in task list"
