class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'product.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        text = file.read()
        file.close()
        return text

    def add(self, *products):
        for product in products:
            check = Shop.get_products(self)
            if (product.name not in check):
                text = f'{product.name}, {product.weight}, {product.category}\n'
                file = open(self.__file_name, 'a')
                file.write(text)
                file.close()
            elif f'{product.weight}' not in check:
                text = f'{product.name}, {product.weight}, {product.category}\n'
                file = open(self.__file_name, 'a')
                file.write(text)
                file.close()
            if (product.name in check):
                print(f'Продукт {product.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())