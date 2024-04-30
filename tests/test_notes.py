import pytest

from lib.notes import Note, Notebook


@pytest.fixture
def notebook():
    return Notebook()




