class Horse:
    x_distance = 0
    sound = 'Frrr'

    def __init__(self):
        dx = 0

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self):
        dy = 0

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        Horse.run(self, dx)
        Eagle.fly(self, dy)

    def get_pos(self):
        pos = (self.x_distance, self.y_distance)
        return pos

    def voice(self):
        return print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()


p1 = Pegasus()

print(p1.get_pos())
