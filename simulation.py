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
        return (int(x), int(y)) in self.cleaned_squares

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
        self.steps = 0

    def step(self):
        """
        - check next roomba positions for collision
        - inform colliding roombas of collision
        - move all roombas
        - inform room of cleaned spaces
        - record clean times at 50, 90, 100%
        """
        for roomba in self.roombas:
            i = 0
            while not self.room.in_bounds(*roomba.next_position):
                roomba.collide()
                i += 1
                if i > 360:
                    raise Exception("Stuck roomba!")

            roomba.move()
            self.room.clean(*roomba.position)
        self.steps += 1

    def run(self):
        results = {0.5: None, 0.9: None, 1.0: None}
        while self.room.clean_percentage() < 1.0 and self.steps < self.room.area * 100:
            self.step()
            for percentage in results.keys():
                if self.room.clean_percentage() >= percentage and results[percentage] is None:
                    results[percentage] = self.steps
        return results
