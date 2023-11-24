
class Note:

    def __init__(self, title: str, text: str) -> None:

        self.title = title
        self.text = text
        self.tegs = []


    def add_text(self, text):
        self.text += text

    def add_tegs(self, tegs):
        tegs = tegs.split(' ')
        for teg in tegs:
            self.tegs.append(teg)

    def change_note(self, text):
        self.text = text
                
        

    def __str__(self) -> str:
        return f'{self.title}: {self.text} {self.tegs}'    
    
    def __repr__(self) -> str:
        return f'{self.title}: {self.text} {self.tegs}'  