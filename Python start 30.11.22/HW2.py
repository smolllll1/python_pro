#1. Write a Python program to print the number entered by user only if the number entered is negative
a = int(input('enter negative number: '))
if a < 0:
    print('everything is correct!')
else:
    print('it is not a negative number')
#2. Write a Python program to check if the value a is less than 20 or not
a = int(input('enter a number: '))
if a < 20 and a < 0:
    print("This number is less 20!")
if a == 20:
    print("This number is 20!")
if a > 20:
    print("This number is greater than 20!")
#3. Write a Python program to check if a given number is Zero or Not
a = int(input('enter a number: '))
if a == 0:
    print('It is Zero!')
else:
    print("It's not Zero!")
#4. Write a Python program to check if a given number is Even or Odd.
a = int(input('enter a number: '))
if a % 2:
    print('is Even')
else:
    print('is Odd')
#5. Write a Python program to find largest number among three numbers entered by user
a = int(input('enter a number: '))
b = int(input('enter a number: '))
c = int(input('enter a number: '))
if a < b and b > c:
    print(str(b) + ': largest number')
if b < a and a > c:
    print(str(a) + ': largest number')
if c > a and c > b:
    print(str(c) + ': largest number')
else:
    print(': there are similar numbers')
