#!/usr/bin/python3
"""Square module"""


class square:
    """Square class."""

    def __init__(self, width=0, height=0):
        """ Initialize the square. """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square. """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Perimeter of the square. """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation of the square """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
