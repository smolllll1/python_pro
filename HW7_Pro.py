# 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії із зазначеним множником.
#  Генератор повинен зупинити свою роботу або після досягнення зазначеного елементу, або при передачі команди на завершення.

def generation(x: int, y=10):
    if isinstance(x, int):
        if x == 0:
            raise ZeroDivisionError
        if y <= 1:
            raise ValueError
        for i in range(1, y):
            rez = x ** i
            yield rez

x = generation(2,20)
for i in x:
    print(i)

# 2. Реалізуйте свій аналог генераторної функції range().

def my_range(start: int, stop: int, step=1):
    if isinstance(start, int) and isinstance(stop, int) and isinstance(step, int):
        while start < stop:
            yield start
            start += step
for i in my_range(1,10,3):
    print(i)

# 3. Напишіть функцію-генератор, яка повертатиме прості числа. Верхня межа діапазону повинна бути задана параметром цієї функції.

def just_numder(stop: int):
    if isinstance(stop, int):
        for i in range(2, stop + 1):
            x = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    x += 1
            if x == 2:
                yield i

for i in just_numder(10):
    print(i)

# 4.  Напишіть генераторний вираз для заповнення списку. Список повинен бути заповнений кубами чисел від 2 до вказаної вами величини.

def add_list(max: int):
    if isinstance(max, int):
        x = [i**3 for i in range(2, max)]
        yield x
for i in add_list(20):
    print(i)
