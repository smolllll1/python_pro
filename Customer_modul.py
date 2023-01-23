class Customer:

    def __init__(self, surname, name, phone):
        self.surname = surname
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'\n{self.surname} {self.name[0]}. tel:  {self.phone}\n{"*"*35}'
