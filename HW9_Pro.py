# 1. Створіть декоратор, який підраховуватиме, скільки разів була викликана декорована функція.
class My_count:
    def __init__(self, calls):
        self.calls = calls
        self.count = 0
    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.calls(*args, **kwargs)
    def __str__(self):
        return f'Worked out {self.count}'

@My_count
def greetings(name):
    return f'Hello, {name}'

for i in range(10):
    pass
    print(greetings('Pavlo'))
print(greetings)

# 2. Створіть декоратор, який зареєструє декоровану функцію у списку.

function_list = []
def decorator_list(x):
    def add(arg):
        tmp = x(arg)
        if tmp not in function_list:
            function_list.append(tmp)
            return f'{tmp}!'
    return add

@decorator_list
def function_1(name):
    return f'Hello, {name}'

@decorator_list
def function_2(name):
    return f'Aloha, {name}'
x = function_1('Pavlo')
y = function_2('Pavlo')
print(function_list[0])
print(function_list[1])

# 3. Припустимо, у класі визначено метод str. Створіть такий декоратор для цього методу, щоб отриманий рядок зберігався у текстовий файл.
# Ім'я файлу має збігатися з ім'ям класу, в якому визначено метод str.

def list_to_file(x):
    def add(*args, **kwargs):
        cls = x(args)
        with open(f'{name_class}.txt', 'a') as file:
            file.write(f'{cls}' + '\n')
        return f'{cls}!'
    return add

class A:
    def __init__(self):
        self.a = self
    @list_to_file
    def __str__(self):
        return 'Helo World'
name_class = A.__name__
print(A())

# 4. Створіть декоратор із параметрами для проведення хронометражу роботи тієї чи іншої функції.
# Параметрами повинні виступати те, скільки разів потрібно запустити функцію, що декорується, і в який файл зберегти результати хронометражу.

def hronometr(count, x, safe_file):
    def decorator(func):
        def ineer(args):
            y = func(args)
            rez = f'{y}{x}'
            for item in range(count):
                with open(safe_file, 'a') as file:
                    file.write(f'{item+1}, '+ rez +'\n')
            return rez
        return ineer
    return decorator


@hronometr(3,'!', 'Hronomet.txt')
def x_1(name):
    return f'Hello {name}'
print(x_1('Pavlo'))


