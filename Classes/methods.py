"""
    What is a method?
        - a procedural attribute
        - a function that only works for this specific class.
"""

class Coordinate(object):

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def distance(self, other):
        """
            other is another instance of a coordinate object
        """
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self):
        """
            other __method__ methods ( dunder )
                - __add__  +
                - __sub__  -
                - __eq__   ==
                - __lt__   <
                - __len__  len(self)
        """
        return f"({self.x},{self.y})"

c = Coordinate(3,4)
origin = Coordinate(0,0)
print ("Distance of c to the origin: ", c.distance(origin))
print ("Different process of taking distance of c to the origin: ", Coordinate.distance(c, origin))
print ("Origin and c: ", origin, c)
print ("Checking if something is an instance: ", isinstance(c, Coordinate))

class Clock(object):

    def __init__(self, time):
        self.time = time

    def print_time(self):
        time = '6:30'
        print(self.time)

clock = Clock('5:30')
clock.print_time()

class Clock(object):

    def __init__(self, time):
        self.time = time

    def print_time(self):
        print(self.time)

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()
