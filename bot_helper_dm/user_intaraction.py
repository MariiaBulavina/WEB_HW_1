from abc import ABC, abstractmethod

from tabulate import tabulate



class Table(ABC):
    @abstractmethod
    def create_table(self):
        ...





class AddressbookTable(Table):

    def create_table(self):
        data = [
        ['name', 'phones', 'birthday', 'emails', 'address']
    ]
        for contact in self.data.values():
            line = [contact.name,  '; '.join([str(p.value) for p in contact.phones]), contact.birthday, '; '.join([str(em.value) for em in contact.emails]), contact.address]
            data.append(line)

        result = tabulate(data,headers='firstrow',tablefmt='fancy_grid')
        return result



class NotebookTable(Table):

    def create_table(self):
        data = [
        ['title', 'text', 'tegs']
    ]

        for note in self.data.values():
            line = [note.title, note.text, "; ".join([str(teg) for teg in note.tegs])]
            data.append(line)

        result = tabulate(data,headers='firstrow',tablefmt='fancy_grid')
        return result
    

class ContactTable(Table):

    def create_table(self, contacts):
        data = [
        ['name', 'phones', 'birthday', 'emails', 'address']
    ]
        
        for contact in contacts:
            line = [contact.name, '; '.join([str(p.value) for p in contact.phones]), contact.birthday, '; '.join([str(em.value) for em in contact.emails]), contact.address]
            data.append(line)

        result = tabulate(data,headers='firstrow',tablefmt='fancy_grid')
        return result
    

class NoteTable(Table):

    def create_table(self, notes):
        data = [
        ['title', 'text', 'tegs']
    ]
        
        for note in notes:
            line = [note.title, note.text, "; ".join([str(teg) for teg in note.tegs])]
            data.append(line)

        result = tabulate(data,headers='firstrow',tablefmt='fancy_grid')
        return result