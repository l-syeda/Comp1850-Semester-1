# Week 1.5, Session 1: Task 3

import math

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x, y):
            """
            Creates a Point, given x & y coordinates.
            """
            self.x = x
            self.y = y


    # Add distance() method here
    def distance(self):
        """
        Returns the distance of this point from the origin (0, 0).
        """
        return math.hypot(self.x, self.y)

    # Add distance_to() method here
    def distance_to(self, point):
        """
        Returns the distance from this point to the specified point.
        """
        return math.hypot(self.x - point.x, self.y - point.y)

#for distance() method
p = Point(3,4)
print(p.x,p.y)
print(p.distance())

#for distance_to() method
p = Point(3,2)
q = Point(7,8)
print(p.distance_to(q))

    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
