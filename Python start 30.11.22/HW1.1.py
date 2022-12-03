#1.Write a Python-script that displays the message “Hello world”
print('Hello world')
#2.Rewrite the first script to display three any messages.
print('Hello world!\n'*3)
#3.Write a Python-script to reads values for the length and width of a rectangle and returns the area of the rectangle
a = int(input('Введіть ширину прямокутника: '))
b = int(input('Введіть висоту прямокутника: '))
c = a * b
print('Площа прямокутника: ', c)

#4.Write a program that requests the user to enter two numbers and prints the sum, product, difference and quotient of the two numbers
a = int(input('Перше число: '))
d = int(input('Друге число: '))
print('сума = '+str(a+d), 'різниця = '+str(a-d), 'добуток = '+str(a*d), 'частка = '+str(a/d), sep='\n')

#5. Write a program that reads in the radius of a circle and prints the circle’s diameter, circumference and area. Use the constant value 3.14159 for π. Do these calculations in output statements.
r = int(input('Введіть радіус кола: '))
d = r*2
c = d*3.14159
s = 3.14159*(r**2)
print('діаметр: ' + str(d), 'окружність: ' + str(c), 'площа: ' + str(s), sep='\n')
