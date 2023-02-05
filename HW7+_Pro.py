#1. Create a class that performs statistical processing of a text file - counting characters, words, sentences, etc.
# Determine the required attributes-data and attributes-methods in class for working with the text file.

class Text():
    def __init__(self, x):
        self.x = x
        self.y = []



    def spliting(self) -> list:
        for i in self:
            yield i.strip().replace(',', ' ')

    def __len__(self):
        return self.x

    def __str__(self):
        return f'{self.x}'

f = open('test.txt')
y = Text.spliting(f)
print(len(y))

#2. Pizzeria offers pizza-of-the-day for business lunch. The type of pizza-of-the-day depends on the day of week.
# Having a pizza-of-the-day simplifies ordering for customers. They don't have to be experts on specific types of pizza.
# Also, customers can add extra ingredients to the pizza-of-the-day. Write a program that will form orders from customers.

from datetime import date

class Pizza:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title} - {self.price}'

class Ingradient:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title} - {self.price}'

class Cart:
    def __init__(self):
        self.ingradient = []


    def add_pizza(self, pizza, ingradient):
        self.ingradient.append(ingradient)

    def __str__(self):
        rec = ''
        for i in self.ingradient:
            rec += f' + {i}'
        return f'{pizza[date.today().isocalendar()[2]]}{rec}'

pizza_1 = Pizza('Cheese Pizza', '12.6$')
pizza_2 = Pizza('Mit Pizza', '15.4$')
pizza_3 = Pizza('Little Pizza', '10.6$')
pizza_4 = Pizza('Big Pizza', '18.5$')
pizza_5 = Pizza('Mediym Pizza', '14.4$')
pizza_6 = Pizza('Pizza Pizza', '18.3$')
pizza_7 = Pizza('XXXL Pizza', '20.9$')

pizza = {1: pizza_1, 2: pizza_2, 3: pizza_3, 4: pizza_4, 5: pizza_5, 6: pizza_6, 7: pizza_7}

ingradient_1 = Ingradient('olives', '0.5$')
ingradient_2 = Ingradient('cheese', '0.7$')
ingradient_3 = Ingradient('sausage', '0.8$')

order = Cart()
order.add_pizza(pizza, ingradient_1)
order.add_pizza(pizza, ingradient_2)
order.add_pizza(pizza, ingradient_3)

print(order)

