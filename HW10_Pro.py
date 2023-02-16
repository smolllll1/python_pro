# 1. Створіть декоратор, який зареєструє декорований клас у списку.
class_list = []
def registr(funtion):
    def ineer(*args, **kwargs):
        class_list.append(funtion)
        return funtion(*args, **kwargs)
    return ineer

@registr
class A:
    def __str__(self):
        return 'Hello'

x = A()
print(x)
print(class_list)

# 2. Створіть клас декоратора з параметром. Параметром має бути рядок, який повинен дописуватись (ліворуч) до результату роботи методу str.

class A:
    def __init__(self, arg):
        self.__x = arg
    @property
    def my_param(self):
        return self
    def __str__(self):
        return f'{self.my_param} {self.__x}'

x = A('Pavlo')
A.my_param = 'Hello'
print(x)

# 3. Для класу Box напишіть статичний метод, який підраховуватиме сумарний обсяг двох ящиків, які будуть його параметрами.

class Box:
    __sum = 0
    @staticmethod
    def sum_box(x, y):
        return x + y
    def __str__(self):
        return self.sum_box
print(Box.sum_box(10, 20))

# 4. Створіть дескриптор, який робитиме поля доступними лише для читання.

class Product:
    def __init__(self, title, color):
        self.title = title
        self.color = color
    def __getattr__(self, item):
        return item
    def __setattr__(self, key, value):
        if key == self.title or key == self.color:
            self.__dict__[key] = value
        else:
            pass
    def __delattr__(self, item):
        pass
    def __str__(self):
        return ','.join(map(lambda item: f' {item[0]} = {item[1]}', self.__dict__.items()))

x = Product('Apple', 'Red')
x.count = '123'
x.title = 'black'
del x.color
print(x)


# 5. Реалізуйте функціонал, який заборонятиме встановлення полів класу будь-якими значеннями, крім цілих чисел.

class My_class:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def __setattr__(self, key, value):
        if key == 'number' and not isinstance(value, int):
            raise ValueError()
        else:
            self.__dict__[key] = value
    def __str__(self):
        return f'{self.name} : {self.number}'

x = My_class('Pavlo', 12)
print(x)

# 6. Реалізуйте властивість класу, яка має наступний функціонал: при установці значення цієї властивості у файл із заздалегідь визначеним ім'ям
# повинен зберігатися час (коли встановлювали значення властивості) та встановлене значення.
import time
class Save_value:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def __setattr__(self, key, value):
        if key == 'number':
            x = time.asctime(time.localtime(time.time()))
            with open('log.txt', 'a') as file:
                file.write(str(x[11:-5]) + f'   value changed to {value}' + '\n')

y = Save_value('Pavlo', 22)
y1 = Save_value('Pavlo', 3)
y2 = Save_value('Pavlo', 345)
y3 = Save_value('Pavlo', 233)

# 7. Створіть ABC клас із абстрактним методом перевірки цілого числа на простоту.
# Тобто якщо параметром цього методу є ціле число і воно просте, то метод повинен повернути True,
# а в іншому випадку False. Створіть похідний клас. Перевірте працездатність проекту.

from abc import ABC, abstractmethod
class My_ABC(ABC):
    @abstractmethod
    def integer(self):
        pass
class Integer(My_ABC):
    def __init__(self, x):
        self.x = x
    def integer(self):
        if isinstance(self.x, int):
            return True
        else:
            return False
def abc(obj: My_ABC):
    if obj.integer():
        return True
    else:
        return False

x = Integer(12)
print(abc(x))