#1. Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності, закон якої задається за допомогою функції користувача.
 # Крім цього параметром генераторної функції повинні бути значення першого члена прогресії та кількість членів, що видаються послідовностю.
 # Генератор повинен зупинити свою роботу або по досягненню n-го члена, або при передачі команди на завершення.

def my_function(*args):
    x, y = args
    if isinstance(x, int) and isinstance(y, int):
        def gen_function():
            nonlocal x, y
            for i in range(x, y + 1):
                yield i
        return gen_function()
    raise TypeError

x = my_function(4, 10)
for i in x:
    if i == 7:
        x.close()
    print(i)

# 2. Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація - https://en.wikipedia.org/wiki/Memoization .
# Використовуйте отриманий механізм для прискорення функції рекурсивного обчислення n - го члена ряду Фібоначчі.
# Порівняйте швидкість виконання із просто рекурсивним підходом.
import timeit

def fibonashy_memo():
    x = [0, 1]
    def my_next():
        x.append(x[-1] + x[-2])
        return x[-1]
    return my_next
x = fibonashy_memo()
c = 0
while c < 30:
    print(x())
    c += 1

def fibonashy():
    pref, curent = 0, 1
    def my_next():
        nonlocal pref, curent
        pref, curent = curent, pref + curent
        return curent
    return my_next
y = fibonashy()
j = 0
while j < 30:
    print(y())
    j += 1
print(timeit.timeit(x, number=10000))
print(timeit.timeit(y, number=10000))

# 3. Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне суми елементів отриманого списку.

y = [2, 2, 3, 4, 5, 6]
def function_1():
    def my_function(x):
        list_sum = len(x)
        return list_sum
    return my_function
x = function_1()
print(x(y))