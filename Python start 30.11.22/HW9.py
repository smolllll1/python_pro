# 1. Існують такі послідовності чисел:
# 0,2,4,6,8,10,12
# 1,4,7,10,13
# 1,2,4,8,16,32
# 1,3,9,27
# 1,4,9,16,25
# 1,8,27,64,125
# Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
# Послідовність користувач вводить з клавіатури у вигляді рядка. Наприклад, користувач вводить рядок 0,5,10,15,20,25 та відповіддю програми має бути число 30.

a = input('enter the sequence: ')
def sequence(b):
    '''function to determine the next sequence number'''
    value = b.split(',')
    if len(value) < 4:
        return 'not enough values'

    for i in range(len(value)):
        if int(value[2]) - int(value[1]) == int(value[-1]) - int(value[-2]) and i >= 1:
            c = int(value[-1]) - int(value[-2])
            return f'{int(value[-1]) + c}'

    for i in range(len(value)):
        if int(value[-1]) == (int(value.index(value[-1]) + 1)) ** i:
            return (int(value.index(value[-1]) + 2)) ** i

    for i in range(len(value)):
        if int(value[i+1]) / int(value[i]) == int(value[-1]) / int(value[-2]) and i >= 1:
            c = int(value[-1]) / int(value[-2])
            return f'{int(value[-1]) * int(c)}'

print(sequence(a))

# 2. Число-паліндром з обох сторін (справа ліворуч і ліворуч) читається однаково.
# Найбільше число-паліндром, одержане множенням двох двозначних чисел: 9009 = 91 × 99.
# Знайдіть найбільший паліндром, одержаний множенням двох трицифрових чисел.
# Виведіть значення цього паліндрому і те, множенням яких чисел він є.


b = [str(i) for i in range(10000, 998002)]
def palind(value: str) -> str:
    '''the function selects a palindrome from numbers'''
    a = []
    for i in value:
        if list(i) == list(reversed(i)):
            a.append(i)
    return a
def syma(a: str) -> str:
    '''the function selects the largest palindrome from the product of three-digit numbers'''
    for i in reversed(range(100, 1000)):
        for j in reversed(range(100, 1000)):
            d = i * j
            if str(d) in a:
                return f'{str(d)} = {str(i)} * {str(j)}'
print(syma(palind(b)))