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
        Vehicle.get_model(self)
        Vehicle.get_horsepower(self)
        Vehicle.get_color(self)
        print('Владелец: ', self.owner)


    def set_color(self, new_color: str):
        self.new_color = new_color
        self.change = True
        for color in self.__COLOR_VARIANTS:
            if new_color.lower() == color.lower():
                self.__color = new_color
                self.change = False

        if self.change:
            print('Нельзя сменить цвет на', self.new_color)
