# 1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
# 2) На його основі створіть клас Студент (перевизначте метод виведення інформації).
# 3) Створіть клас Група, який містить масив із 10 об'єктів класу Студент.
# Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.
# Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.

# HW3 2. Модифікуйте Друге домашнє завдання так, щоб при спробі додавання до групи більше 10-ти студентів,
# викликалася виняткова ситуація (тип виняткової ситуації треба самостійно реалізувати).

import logging
class Incorrect_number(Exception):
    def __init__(self, msg, correct):
        self.msg = msg
        self.correct = correct

    def __str__(self):
        return f'{self.msg}, {self.correct}'

class Man:
    def __init__(self, surname, name):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname}. {self.name[0]}'

class Student(Man):
    def __init__(self, surname, name, phon):
        super().__init__(surname, name)
        self.phon = phon

    def listed(self):
        return [self.name, self.surname, self.phon]


    def __str__(self):
        return f'{super().__str__()} - {self.phon}'

class Group:
    def __init__(self, title, max_limit=10):
        self.title = title
        self.max_limit = max_limit
        self.__students = []


    def add_student(self, arg: Student):
        if len(self.__students) >= self.max_limit:
            raise Incorrect_number('limit exceeded!!!', f'  maximum value: {self.max_limit}')
        for item in self.__students:
            if (item.surname, item.name, item.phon) == (arg.surname, arg.name, arg.phon):
                return None
        self.__students.append(arg)
        logger.info(f'appending student! {arg}')

    def remove_student(self, arg: Student):
        if arg in self.__students:
            self.__students.remove(arg)
            logger.info(f'removing student! {arg}')

    def search(self, surname: str):
        res = []
        for item in self.__students:
            if item.surname == surname:
                res.append(item)
        return res

    def __str__(self):
        return f'{self.title}\nStudents:\n' + '\n'.join(map(str, self.__students))

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')

filehandler = logging.FileHandler('logger.log')
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)


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
m11 = Student('Viktorov', 'Viktor', '21212121212')

gpuop_1 = Group('Gruop 1')
gpuop_2 = Group('Gruop 2')
try:
    gpuop_1.add_student(m1)
    gpuop_2.add_student(m2)
    gpuop_1.add_student(m3)
    gpuop_2.add_student(m4)
    gpuop_1.add_student(m5)
    gpuop_2.add_student(m6)
    gpuop_1.add_student(m7)
    gpuop_1.add_student(m8)
    gpuop_2.add_student(m9)
    gpuop_2.add_student(m10)
except Incorrect_number as error:
    print(error)
finally:
    gpuop_2.remove_student(m2)



print(gpuop_2)
print(gpuop_1)

search_name = 'Petrov'
res = gpuop_1.search(search_name)
print('\n', '*'*40, '\n')
print('*'.join(map(str, res)))