class Horse:
    x_distance = 0
    sound = 'Frrr'

    def __init__(self, dx, dy):
        super().__init__(dy)
        self.dx = dx

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self, dy):
        self.dy = dy

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):


    def move(self, dx, dy):
        Horse.run(self, dx)
        Eagle.fly(self, dy)

    def get_pos(self):
        pos = (self.x_distance, self.y_distance)
        return pos

    def voice(self):
        return self.sound


p1 = Pegasus()

print(p1.get_pos())
