import tabulate
from collections import UserDict
import pickle

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        try:
            self.data.pop(name)
        except KeyError:
            return 'You have no contacts with this name'
        
        return f'Сontact with the name {name} has been deleted'
        
        
    def save(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self, file)

    def load(self, file_name):
            try:
                with open(file_name, 'rb') as file:
                    file.seek(0)
                    self.data = pickle.load(file)
            except FileNotFoundError:
                pass    
    
    def create_table(self):

        data = [
        ['name', 'phones', 'birthday', 'emails', 'address']
    ]

        for contact in self.data.values():
            line = [contact.name, contact.phones, contact.birthday, contact.emails, contact.address]
            data.append(line)
        
    
        result = tabulate.tabulate(data)
        return result

    def upcoming_birthdays(self, period):

        result = []

        for user in self.data.values():
            if user and user.birthday:
       
                if 0 <= user.days_to_birthday() <= period:

                    result.append(f'Name: {user.name.value}, days to birthday: {user.days_to_birthday()}')

        return result
