from typing import List

from zoo.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self,Product):
        self.products.append(Product)

    def find(self,product_name):
        return next((p for p in self.products if p.name == product_name),None)

    def remove(self,product_name):
        product = self.find(product_name)
        if product:
            self.products.remove(product)


    def __repr__(self):
        return '\n'.join([f'{p.name}: {p.quantity}' for p in self.products])