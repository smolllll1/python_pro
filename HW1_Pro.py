import Product_modul
import Customer_modul
import Cart_modul
class Incorrect_number(Exception):
    def __init__(self, msg, correct):
        self.msg = msg
        self.correct = correct
    def __str__(self):
        return f'{self.msg}, {self.correct}'

x_1 = Product_modul.Product('banana', 1)
x_2 = Product_modul.Product('apple', 25)
x_3 = Product_modul.Product('orange', 35)

customer_1 = Customer_modul.Customer('Ivanov', 'Ivan', '123456789')
customer_2 = Customer_modul.Customer('Ivanov', 'Petro', '123456799')

order_1 = Cart_modul.Cart(customer_1)
try:
    order_1.add_product(x_1)
    order_1.add_product(x_2, 2)
    order_1.add_product(x_3, 35)
except Incorrect_number as error:
    print(error)


order_2 = Cart_modul.Cart(customer_2)
try:
    order_2.add_product(x_2, 10)
    order_2.add_product(x_2, 2)
    order_2.add_product(x_3, 27)
    order_2.add_product(x_1)
except Incorrect_number as error:
    print(error)
print(order_2)
for i in order_2:
    print(i)
# print(order_2[2])