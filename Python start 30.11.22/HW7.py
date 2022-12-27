# 1.Використовуючи словник, напишіть програму, яка виведе на екран назву дня тижня за номером.
# Наприклад, 1 - "Monday".

x = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
print(x.get(int(input('day number:'))))

# 2.Опишіть кота (домашня тварина) на основі словника.

cat = {'name': 'Simda', 'breed': 'homely', 'color': 'gray'}
print(cat.get('name'))

#3. Напишіть програму, яка читає рядок тексту з клавіатури і виводить на екран статистику, скільки разів яка літера зустрічається в цьому рядку.
#Наприклад, для рядка «Hello world» ця статистика виглядає так: «H» - 1, «e» - 1, «l» - 3 і т.д.

x = input('Text: ')
y = {}
for i in x:
    key = y.get(i)
    if key:
        y[i] = key + 1
    if i == ' ':
        continue
    else:
        y[i] = 1
print(y)

# 4. Напишіть програму, яка прочитає два рядки тексту з клавіатури і виведе на екран літери, які є одночасно і в першому, і в другому рядку.
# Наприклад, для рядків «Hello» та «World» на екрані мають бути літери «l» та «o».

x = set(input('Text1: '))
y = set(input('Text2: '))
print(x.intersection(y))

# 5. Напишіть програму, яка згенерує два списки. Один із числами кратними 3, інший із числами кратними 5.

print(f'{[i for i in range(1, 50) if not i % 3]}\n{[i for i in range(1, 50) if not i % 5]}')

# 6. Створіть список із числами, які є в обох списках.
import random
x = [random.randint(0, 10) for _ in range(10)]
y = [random.randint(0, 10) for _ in range(10)]
print(f'{x}\n{y}\n{list(set(x) & set(y))}')