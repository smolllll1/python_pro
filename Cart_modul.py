import Customer_modul
import Product_modul

class GroupIterator:
    def __init__(self, products):
        self.products = products
        self.index = 0
    def __next__(self):
        if self.index < len(self.products):
            self.index += 1
            return self.products[self.index - 1]
        raise StopIteration


class Cart:

    MAX_LIMIT = 40

    def __init__(self, customer: Customer_modul):
        self.customer = customer
        self.__products = []
        self.__quantities = []
        self.res = []
    def __iter__(self):
        return GroupIterator(self.__products)
    def __getitem__(self, item):
        if isinstance(item, int):
            if item < len(self.__products):
                return self.__products[item]
            raise IndexError()

    def __len__(self):
        return len(self.__products)

    def get_weight(self):
        return sum(self.__quantities)

    def add_product(self, product: Product_modul, quantity: int | float = 1):
        if self.get_weight() + quantity <= Cart.MAX_LIMIT:
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