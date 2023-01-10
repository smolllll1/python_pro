#Необхідно підготувати звіт про витрати членів родини на новорічні свята.
#Звіт повинен включати наступне:
#1. Яка загальна сума витрат по кожній категорії товарів?
#2. Скільки грошей витратив кожен член родини?
#2. Яку кількість покупок та на яку загальну суму зробив введений користувачем через input член родини?

def spliting(x: str)->list:
    return [line.strip().replace('.(0, 99)$ ', ' ').split() for line in x]

def product()->list:
    tovar = []
    for i in no_cents:
        tovar.append([i[-1]]+[i[-2]])
    return tovar

def names()->list:
    name = []
    for i in no_cents:
        if i[2].isalpha():
            name.append([i[1]+' '+i[2]]+[i[-2]])
        else:
            name.append([i[1]]+[i[-2]])
    return name

def amounts_product(x: list)->dict:
    dictionary_product = dict(x)

    for i in x:
       dictionary_product[i[0]] = 0
    for i in x:
        dictionary_product[i[0]] = round((float(dictionary_product.get(i[0])) + float(i[1])) + float(0.99), 2)
    return dictionary_product

def amounts_operation(x: list)->dict:
    dictionary_amounts = {}

    for i in x:
       dictionary_amounts[i[0]] = 0
    for i in x:
        dictionary_amounts[i[0]] = dictionary_amounts[i[0]] + 1
    return dictionary_amounts

f = open('test.txt', 'r')

no_cents = spliting(f)
many = amounts_product(names())
category = amounts_product(product())
number = amounts_operation(names())
value = input("ВВедіть ім'я: ")
print(f'Потратив(ла): {many[value]} $. Зробив(ла): {number[value]} покупок')

print('\nЗагальна сума витрат по кожній категорії: ')
for i in category:
    print(f'{i}: {category[i]}')


print('\nKожен член родини витратив: ')
for i in many:
    print(f'{i}: {many[i]}')
f.close()

