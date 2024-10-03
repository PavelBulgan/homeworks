class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = "Frrr"

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        pos = (self.x_distance, self.y_distance)
        return pos

    def voice(self):
        return print(self.sound)


p1 = Pegasus()

print(p1.get_pos())