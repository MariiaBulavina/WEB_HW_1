import tabulate

from collections import UserDict

from save_load import SaverLoader


class NoteBook(UserDict, SaverLoader):
    
    def add_note(self, note):
        self.data[note.title] = note


    def delete_note(self, title):
        
        try:
            self.data.pop(title)
        except KeyError:
            return 'You have no notes with this title'
        
        return f'Note with the title {title} has been deleted'

    def create_table(self):

        data = [
        ['title', 'text', 'tegs']
    ]

        for note in self.data.values():
            line = [note.title, note.text, note.tegs]
            data.append(line)
        
    
        result = tabulate.tabulate(data)
        return result

 