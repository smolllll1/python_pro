# 1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару,
# опису товару, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
# 2. Створіть клас "Покупець". У якості атрибутів можна використовувати прізвище, ім'я, по батькові, мобільний телефон тощо.

# 3. Створіть клас "Замовлення". Замовлення може містити декілька товарів певної кількості.
# Замовлення має містити дані про користувача, який його здійснив. Реалізуйте метод обчислення сумарної вартості замовлення.
# Визначте метод str() для коректного виведення інформації про це замовлення.

# HW3 . Модифікуйте Перше домашнє завдання так, щоб при спробі встановити від'ємну або нульову вартість товару викликалася виняткова ситуація
# (тип виняткової ситуації треба самостійно реалізувати).

class Incorrect_number(Exception):
    def __init__(self, msg, correct):
        self.msg = msg
        self.correct = correct

    def __str__(self):
        return f'{self.msg}, {self.correct}'

class Product:

    def __init__(self, title: str, price: int | float):

        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price} UAH'


class Customer:

    def __init__(self, surname, name, phone):
        self.surname = surname
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'\n{self.surname} {self.name[0]}. tel:  {self.phone}\n{"*"*35}'


class Cart:

    MAX_LIMIT = 40

    def __init__(self, customer: Customer):
        self.customer = customer
        self.__products = []
        self.__quantities = []

    def get_weight(self):
        return sum(self.__quantities)

    def add_product(self, product: Product, quantity: int | float = 1):
        if self.get_weight() + quantity <= Cart.MAX_LIMIT:
            if product.price <= 0:
                raise Incorrect_number(f'{product.title}!!!   Incorrect prise', 'mast be > 0')
            self.__products.append(product)
            self.__quantities.append(quantity)

    def total(self):
        result = 0
        for product, quantity in zip(self.__products, self.__quantities):
            result += product.price * quantity

        return result

    def __str__(self):
        result = f'{self.customer}\n'
        result += '\n'.join(map(lambda item: f'{item[0]} x {item[1]} = {item[0].price * item[1]} UAH',
                      zip(self.__products, self.__quantities)))
        result += f'\nTotal: {self.total()} UAH'
        return result


x_1 = Product('banana', 1)
x_2 = Product('apple', 25)
x_3 = Product('orange', -35)

customer_1 = Customer('Ivanov', 'Ivan', '123456789')
customer_2 = Customer('Ivanov', 'Petro', '123456799')

order_1 = Cart(customer_1)
try:
    order_1.add_product(x_1)
    order_1.add_product(x_2, 2)
    order_1.add_product(x_3, 35)
except Incorrect_number as error:
    print(error)

print(order_1)


order_2 = Cart(customer_2)
try:
    order_2.add_product(x_2, 10)
except Incorrect_number as error:
    print(error)
print(order_2)
