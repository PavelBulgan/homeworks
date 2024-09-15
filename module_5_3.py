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

    def __add__(self, other):
        if isinstance(other, int):
            return House(self.name, self.floors + other)
        else:return (f'   !ошибка при вводе этажа!')

    def __iadd__(self, other):
        if isinstance(other, int):
            return House(self.name, self.floors + other)
        else:return (f'   !ошибка при вводе этажа!')

    def __radd__(self, other):
        if isinstance(other, int):
            return House(self.name, self.floors + other)
        else:return (f'   !ошибка при вводе этажа!')

    def __eq__(self, other):
        return self.floors == other.floors

    def __lt__(self, other):
        return self.floors < other.floors

    def __le__(self, other):
        return self.floors <= other.floors

    def __gt__(self, other):
        return self.floors > other.floors

    def __ge__(self, other):
        return self.floors >= other.floors

    def __ne__(self, other):
        return self.floors != other.floors


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(f'{h1}   - НАЧАЛЬНОЕ ЗНАЧЕНИЕ h1')
print(f'{h2}    - НАЧАЛЬНОЕ ЗНАЧЕНИЕ h2')

print(f'{h1 == h2}                                     - ПРОВЕРКА НА РАВЕНСТВО МЕТОДОМ "__eq__"') # __eq__

h1 = h1 + 10
print(f'{h1}   - ИЗМЕНЕНИЕ ЭТАЖНОСТИ МЕТОДОМ "__add__"')
print(f'{h1 == h2}                                      - ПРОВЕРКА НА РАВЕНСТВО ПОСЛЕ ИЗМЕНЕНИЯ')

h1 += 10
print(f'{h1}   - ДОБАВЛЕНИЕ ЭТАЖЕЙ МЕТОДОМ "__iadd__"')

h2 = 10 + h2
print(f'{h2}    - ДОБАВЛЕНИЕ ЭТАЖЕЙ МЕТОДОМ "__radd__"')

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__