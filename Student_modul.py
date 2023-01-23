import Man_modul
class Student(Man_modul.Man):
    def __init__(self, surname, name, phon):
        super().__init__(surname, name)
        self.phon = phon
    def listed(self):
        return [self.name, self.surname, self.phon]

    def __str__(self):
        return f'{super().__str__()} - {self.phon}'
