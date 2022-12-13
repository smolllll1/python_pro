#1. Дано число (чотиризначне). Перевірити, чи воно є «щасливим квитком».
#Примітка: щасливим квитком називається число, у якому, при парній кількості цифр, сума цифр його лівої
#половини дорівнює сумі цифр його правої половини.
#Наприклад, 1322 є щасливим квитком, тому що 1 + 3 = 2 + 2.

x = list(input("Введи свій щасливий квиток: "))
print(x)
for i in range(len(x)):
    x[i]=int(x[i])
if not len(x)%2 and sum(x[:(int(len(x)/2))]) == sum(x[-(int(len(x)/2)):]):
    print('Ваш квиток щасливий!')
else:
    print('Пощастить іншим разом')

#2. З клавіатури вводиться число (шестизначне). Перевірити, чи воно є паліндромом.
# Примітка: Паліндром називається число, слово або текст, які однаково читаються зліва направо і справа наліво.
# Наприклад, це числа 143341, 5555, 7117 і т.д.

y = []
x =list(input("Введи число або слово: "))
print(x)
for i in reversed(x):
    y.append(i)
print(y)
if x == y:
    print('Паліндром!')
else:
    print('Не паліндром!')

#3. Дано коло з центром на початку координат та радіусом 4.
# Користувач вводить з клавіатури координати точки x та y.
# Написати програму, яка визначить, лежить ця точка всередині кола чи ні.
x = int(input('Введіть координату Х: '))
y = int(input('Введіть координату Y: '))
R = 4
if x**2 + y**2 <= R**2:
    print('точка належить трикутнику!')
else:
    print('точка не належить трикутнику!')