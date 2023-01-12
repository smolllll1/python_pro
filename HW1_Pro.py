# 1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару,
# опису товару, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
# 2. Створіть клас "Покупець". У якості атрибутів можна використовувати прізвище, ім'я, по батькові, мобільний телефон тощо.

# 3. Створіть клас "Замовлення". Замовлення може містити декілька товарів певної кількості.
# Замовлення має містити дані про користувача, який його здійснив. Реалізуйте метод обчислення сумарної вартості замовлення.
# Визначте метод str() для коректного виведення інформації про це замовлення.
class Goods:
    def __init__(self, price, product, dimensions):
        self.price = price
        self.product = product
        self.dimensions = dimensions
    def __str__(self):
        return f'{self.product} - {self.price}$   {self.dimensions}'
class Shopper:
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone
    def __str__(self):
        return f'{self.surname}.{self.name[0]}   tel: {self.phone}'
class Order:
    def __init__(self, shoper, product):
        self.shoper = shoper
        self.product = product
        self.suma = {}
    def suma1(self, prace):
        self.prace = prace.price
        self.tovar = prace.product
        if self.tovar in self.suma:
            self.suma[self.tovar] = self.suma.get(self.tovar) + int(self.prace)
        else:
            self.suma[self.tovar] = int(self.prace)


    def __str__(self):
        return  f'\n{"*"*40}\n{self.shoper}\nCумарнa вартості замовлення: {sum(self.suma.values())} $\n{"*"*40}'


x1 = Goods('120', 'хімія', '20*30')
x2 = Goods('100', 'кулінарія', '50*60')
x3 = Goods('600', 'кондитер', '80*90')

shoper_1 = Shopper('Іван', 'Іванов', '099-999-99-99')
shoper_2 = Shopper('Іван1', 'Іванов1', '088-888-88-88')
shoper_3 = Shopper('Іван2', 'Іванов2', '077-777-77-77')

order = Order(shoper_1, x1)
order.suma1(x1)
order.suma1(x2)
order.suma1(x1)
order.suma1(x3)
print(order)
