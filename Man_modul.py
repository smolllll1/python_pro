class Man:
    def __init__(self, surname, name):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname}. {self.name[0]}'