# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")

        self.colour = colour


# Implement your Circle class here
class Circle(Shape):  #need to have (shape) cause it inherits from shape
    """
    A circle with a radius, position, and colour.
    """

    def __init__(self, radius, position, colour= "red"):   #can just assign 'red' to colour as default value so we dont keep having to write it everytime
        super().__init__(position, colour)  #this means

        self.radius(radius)  # i did  '= radius' instead of '(radius)' 
        # self.position = position
        # self.colour = "red"
        

    def set_radius(self, radius):
        if not isinstance (radius, (int, float)):
            raise TypeError("radius must be a number")
        self.radius = radius


    def area(self):
        return math.pi * self.radius ** 2

        # if radius < 0:                  i did all this...
        #     raise ValueError("radius must be a positive number")
        # self.radius = radius

    def __str__(self):
        return f"Circle(colour={self.colour}, radius={self.radius}, at position={self.position})" 
   

        

# Make sure that it inherits properly from Shape!
