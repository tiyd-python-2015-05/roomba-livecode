from math import sin, cos, radians

class Room:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.cleaned_squares = set()

    @property
    def area(self):
        return self.length * self.width

    def clean_percentage(self):
        return len(self.cleaned_squares) / self.area

    def clean(self, x, y):
        """Clean the 1x1 square that contains x & y."""
        self.cleaned_squares.add((int(x), int(y)))

    def is_clean(self, x, y):
        """See if square has been cleaned."""
        return (x, y) in self.cleaned_squares

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.length


class Roomba:
    def __init__(self, x=0, y=0, angle=0):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 1

    @property
    def position(self):
        return (self.x, self.y)

    @position.setter
    def position(self, pos):
        self.x, self.y = pos

    @property
    def next_position(self):
        x_move = sin(radians(self.angle)) * self.speed
        y_move = cos(radians(self.angle)) * self.speed
        return (self.x + x_move, self.y + y_move)

    def collide(self):
        self.angle += 45
        self.angle %= 360

    def move(self):
        self.position = self.next_position

    def place(self, x, y):
        self.position = (x, y)


class Simulation:
    def __init__(self, room, roombas):
        self.room = room
        self.roombas = roombas