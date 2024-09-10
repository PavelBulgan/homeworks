class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        for i in range(1, self.new_floor + 1):
            if new_floor >= 1 and new_floor <= self.number_of_floors:
                print(f'{self.name}: этаж {i}')
            else:
                print(f'Такого этажа в "{self.name}" не существует')
                break

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)