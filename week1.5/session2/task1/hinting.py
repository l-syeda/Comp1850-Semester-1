# Week 1.5, Session 2: Task 1

# Add type hints to the Point class

import math


class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x: float, y:float):
        """
        Creates a Point, given x & y coordinates.
        """

        # if not isinstance(x, (int,float)):                   dont need these...
        #     raise TypeError ("x must be a number")

        # if not isinstance(y, (int,float)):
        #     raise TypeError ("y must be a number")

        self.x = x
        self.y = y

    def distance(self) -> float:
        """
        Returns distance of this Point from the origin.
        """
        
        # if not isinstance(self.distance, (int,float)):
        #     raise TypeError("distance must be a number")

        return math.hypot(self.x, self.y)

    def distance_to(self, p: Point) -> float:
        """
        Returns distance of this Point from the specified Point.
        """

        # if not isinstance(p, (int,float)):
        #             raise TypeError("distance to must be a number")
        
        return math.hypot(self.x - p.x, self.y - p.y)


# Test program

# p = Point("two", "one")    this will give an error
p = Point(2, 1)             #this works tho
print(p.distance())
