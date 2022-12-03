#1. Construct an integer from the string "123"
a = int('123')
#2. Construct a float from the integer 123
a = float(int(123))
#3. Construct an integer from the float 12.345
a = int(12.342)
#4. Write a Python-script that detects the last 4 digits of a credit card
a, b, c, d = input('Введіть номер карточки як на зразку (0000-0000-0000-0000): ').split('-')
print('Останні чотири цифри: ' + d)
#5. Write a Python-script that calculates the sum of the digits of a three-digit number
a = int(input('Введіть тризначне число: '))
print((a//100)+(a//10%10)+(a%10))
#6. Write a program that calculates and displays the area of a triangle if its sides are known
a, b, c = input('Введіть три сторони через прибіл: ').split(' ')
p = (int(a) + int(b) + int(c)) / 2
s = (p*(p-int(a))*(p-int(b))*(p-int(c)))**0.5
print('площа трикутника: ', s)
#7.Write a Python-script that calculates the sum of the digits of a number
a = int(input('Введіть число: '))
sum = 0
while a != 0:
    sum = sum + a % 10
    a = a // 10
print("Сума цифр числа рівна: ", sum)
#8.Determine the number of digits in a number
a = int(input('Введіть число: '))
s = 0
while a:
    s += 1
    a //= 10
print('Кількість цифр в числі: ', s)
#9.Print the digits in reverse order
a = int(input('Введіть число: '))
b = 0
while a > 0:
    c = a % 10
    a //= 10
    b *= 10
    b += c
print(b)








