class Note:
    def __init__(self, text, tag=None):
        self.text = text
        self.tag = tag


class Notebook:
    def __init__(self):
        self.notes = []

    def create_note(self, text, tag=None):
        note = Note(text, tag)
        self.notes.append(note)

    def search_by_tag(self, tag):
        return [note for note in self.notes if note.tag == tag]



