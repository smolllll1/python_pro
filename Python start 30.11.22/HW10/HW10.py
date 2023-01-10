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
c = amounts_product(names())
y = amounts_product(product())
b = amounts_operation(names())
a = input("ВВедіть ім'я: ")
print(f'Потратив: {c[a]} $. Зробив(ла): {b[a]} покупок')

print('\nЗагальна сума витрат по кожній категорії: ')
for i in y:
    print(f'{i}: {y[i]}')

print('\nKожен член родини витратив: ')
for i in c:
    print(f'{i}: {c[i]}')
f.close()

