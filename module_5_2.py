class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        for i in range(1, self.new_floor + 1):
            if new_floor >= 1 and new_floor <= self.floors:
                print(f'{self.name}: этаж {i}')
            else:
                print(f'Такого этажа в "{self.name}" не существует')
                break

    def __len__(self):
        return self.floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(len(h1))
print(len(h2))

