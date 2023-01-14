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
    def __init__(self, shoper):
        self.shoper = shoper
        self.suma = {}
    def total_price(self, goods):
        self.prace = goods.price
        self.tovar = goods.product
        if self.tovar in self.suma:
            self.suma[self.tovar] = self.suma.get(self.tovar) + int(self.prace)
        else:
            self.suma[self.tovar] = int(self.prace)
    def __str__(self):
        return  f'\n{"*"*40}\n{self.shoper}\nThe total cost of the order: {sum(self.suma.values())} $\n{"*"*40}'

x1 = Goods('120', 'chemistry', '20*30')
x2 = Goods('100', 'cooking', '50*60')
x3 = Goods('600', 'confectioner', '80*90')

shoper_1 = Shopper('Ivan', 'Ivanov', '099-999-99-99')
shoper_2 = Shopper('Ivan1', 'Ivanov1', '088-888-88-88')
shoper_3 = Shopper('Ivan2', 'Ivanov2', '077-777-77-77')

order = Order(shoper_1)
order.total_price(x1)
order.total_price(x2)
order.total_price(x1)
order.total_price(x3)
print(order)
