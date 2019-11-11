"""
Objects have types.
    - objects are a data abstraction that has an internal representation
    - you can create new instances of new instances
    - [1,2,3,4] is a type of list
    - a list is an object which has methods
"""

class Coordinate(object):
    """
    object is a superclass of the Coordinate
    Coordinate is the subclass of the object
    <define attributes below>
    """

    def __init__(self, x, y):
        """
        this is the initialization of the object
        """
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

c = Coordinate(3,4)
origin = Coordinate(0,0)
print ('c.x',  c.x)
print ('c.y',  c.y)
print ('c',  c)
print ('origin',  origin)
