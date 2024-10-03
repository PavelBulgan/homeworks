class Animal:
    alive = True  # живое
    fed = False  # голодный

    def __init__(self, name: str):
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            Animal.alive = False
        else:
            print(f'{self.name} не стал есть {food.name}')
            Animal.fed = True


class Plant:
    edible = False  # не съедобный

    def __init__(self, name: str):
        self.name = name


class Mammal(Animal):
    food = Plant


class Predator(Animal):
    food = Plant


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True
