import tabulate
from collections import UserDict
import pickle

from save_load import SaverLoader


class AddressBook(UserDict, SaverLoader):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
            self.data.pop(name)
   
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
