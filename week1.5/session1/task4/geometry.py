# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

# Copy Point class definition here
import math

class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
            """
            Creates a Point, given x & y coordinates.
            """
            self.x = x
            self.y = y


    def distance(self):
        """
        Returns the distance of this point from the origin (0, 0).
        """
        return math.hypot(self.x, self.y)


    def distance_to(self, point):
        """
        Returns the distance from this point to the specified point.
        """
        return math.hypot(self.x - point.x, self.y - point.y)

p = Point(3,4)
print(p.x,p.y)
print(p.distance())

p = Point(3,2)
q = Point(7,8)
print(p.distance_to(q))


# Add a definition for a Circle class here, giving it
class Circle:
    """
    A Circle in 2D space.
    """

    def __init__(self, center, radius = Point(0,0)):  #dont need to include =Point(0,0) it just means to set the coordinates to 0,0 if they aren't specified anywhere
        """
        Creates a Circle object, given the center and a radius.

        Centre coordinates default to (0, 0) if not specified.
        """
        self.center = center
        self.radius = radius
    
#  - A constructor that creates fields to represent the centre & radius of a circle (assume centre is represented as a Point object)

    def area(self):
         """
         Returns area of a circle
         """
         return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Returns perimeter (circumference) of a circle
        """
        return 2 * math.pi * self.radius

#  - A method area(), returning the area of the circle
a = Circle(Point(0,0), 5)
print(a.area())

#  - A method perimeter(), returning the perimeter of the circle
p = Circle(Point(0,0), 5)
print(p.perimeter())

# Don't add any testing code to this file!
