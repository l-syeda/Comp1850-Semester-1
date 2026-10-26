# A bad class implementation

# What does the runtime error mean?
# How do we fix the code?

class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):   #should have two underscores before and after init
                                                      # the  self.  is very important, dont NEED it but lowk do. its always the first parameter in the list, it refers to 'the object itself', basically the object we're creating
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate


p = Point(1.5, 2.0)
print(p.x)
print(p.y)
