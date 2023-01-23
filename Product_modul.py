class Product:

    def __init__(self, title: str, price: int | float):
        if price <= 0:
            raise ValueError('Price must be positive number')
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price} UAH'

