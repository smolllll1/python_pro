# 1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
# 2) На його основі створіть клас Студент (перевизначте метод виведення інформації).
# 3) Створіть клас Група, який містить масив із 10 об'єктів класу Студент.
# Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.
# Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.

class Man:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name}. {self.surname[0]}'

class Student(Man):
    def __init__(self, name, surname, phon):
        super().__init__(name, surname)
        self.phon = phon

    def listed(self):
        return [self.name, self.surname, self.phon]


    def __str__(self):
        return f'{super().__str__()} - {self.phon}'

class Group:
    def __init__(self, castomer: Student):
        self.castomer = castomer
        self.__students = []
        self.limit = 1
        self.input_name = input('enter a name: ')
        self.output = ''

    def add_student(self, arg: Student):
        if Student.listed(arg) not in self.__students and self.limit <= 10:
            self.__students.append(Student.listed(arg))
            self.limit += 1

    def remove_student(self, arg: Student):
        self.__students.remove(Student.listed(arg))

    def search(self):
        for i in self.__students:
            for j in i:
                if self.input_name == j:
                    return f'{" ".join(i)}'

    def __str__(self):
        for i in self.__students:
            self.output += " ".join(i[:-1]) + ', '
        return self.output[:-2]




m1 = Student('Ivanov', 'Ivan', '11111111')
m2 = Student('Stepanov', 'Stepan', '22222222')
m3 = Student('Petrov', 'Petro', '33333333')
m4 = Student('Semenov', 'Semen', '44444444')
m5 = Student('Pavlov', 'Pavlo', '55555555')
m6 = Student('Igorov', 'Igor', '666666666')
m7 = Student('Mashanov', 'Masha', '77777777')
m8 = Student('Olyanov', 'Olya', '88888888')
m9 = Student('Iranov', 'Ira', '9999999999')
m10 = Student('Vityanov', 'Vitya', '1000000000')

s = Group(m1)

s.add_student(m1)
s.add_student(m2)
s.add_student(m3)
s.add_student(m4)
s.add_student(m5)
s.add_student(m6)
s.add_student(m7)
s.add_student(m8)
s.add_student(m9)
s.add_student(m10)

s.remove_student(m2)

print(s.search())
print(s)