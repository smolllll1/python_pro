#1. Є дев'ятиповерховий будинок, в якому 4 під'їзди. Номер під'їзду починається з одиниці.
# На одному поверсі - 4 квартири. Напишіть програму, яка від користувача отримує номер квартири
# та виводить для заданої квартири номер під'їзду, поверху та номер на поверсі.
# Якщо такої квартира немає в цьому будинку, то необхідно повідомити користувача про це.
a = int(input('Введіть номер квартири: '))
b = 144
p = 36
f = 9
t = 4
if a <= 0 or a > 144:
    print('Такої квартира немає у цьому будинку!')
else:
    print('Підїзд: '+f'{-((b-a)//p)+t}''\nПоверх: '+f'{-(((b-a)//t)%f)+f}''\nКвартира: '+str(a))

#2.Написати програму, яка буде повертати для заданого року кількість днів.
# Рік є високосним, якщо він кратний 4, але не кратний 100, а також якщо він кратний 400
a = int(input('введіть рік:'))
if a%4 and a%400 and  a%100 != 0:
    print ('365 днів')
else:
    print('366 днів. Висикосний!')

#.3  Трикутник існує лише тоді, коли сума будь-яких двох сторін більше третьої.
# Дано: A, B, C - сторони трикутника. Напишіть програму, яка вказує чи існує такий трикутник.

a = int(input('сторона а:'))
b = int(input('сторона b:'))
c = int(input('сторона c:'))
if a > b + c or b > a + c or c > a + b:
    print('такий трикутник існує!')
else:
    print(('такого трикутника неіснує'))


