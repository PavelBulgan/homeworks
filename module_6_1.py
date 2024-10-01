
class Animal:
    alive = True  # живое
    fed = False  # голодный

    def __init__(self, name: str):
        self.name = name


class Plant:
    edible = False  # не съедобный

    def __init__(self, name: str):
        self.name = name


class Mammal(Animal):
    food = Plant

    def eat(self, food: Plant):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            Animal.alive = False
        else:
            print(f'{self.name} не стал есть {food.name}')
            Animal.fed = True


class Predator(Animal):
    food = Plant

    def eat(self, food: Plant):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            Animal.alive = False
        else:
            print(f'{self.name} не стал есть {food.name}')
            Animal.fed = True


class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.