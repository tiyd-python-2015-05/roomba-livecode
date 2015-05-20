__author__ = 'clinton'
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