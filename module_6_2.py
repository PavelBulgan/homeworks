class Vehicle:
    __COLOR_VARIANTS: list = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, __model: str, __color: str, __engine_power: int):
        self.new_color = None
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        self.change = None

    def get_model(self):
        print('Модель: ', self.__model)

    def get_horsepower(self):
        print('Мощность: ', self.__engine_power)

    def get_color(self):
        print('Цвет: ', self.__color)

    def print_info(self):
        print('Модель: ', self.__model)
        print('Мощность: ', self.__engine_power)
        print('Цвет: ', self.__color)
        print('Владелец: ', self.owner)

    def set_color(self, new_color: str):
        self.new_color = new_color
        self.change = True
        for color in Vehicle.__COLOR_VARIANTS:
            if color.lower() == new_color.lower():
                self.__color = new_color
                self.change = False

        if self.change:
            print('Нельзя сменить цвет на', self.new_color)


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.get_model()
vehicle1.get_color()
vehicle1.set_color('green')
vehicle1.get_color()
vehicle1.set_color('orange')
vehicle1.get_color()




