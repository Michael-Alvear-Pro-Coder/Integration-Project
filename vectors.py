"""This file contains classes and functions relevant to vectors for use in
simple physics applications. Coordinates are expected to be tuples with 2
elements and are in cartesian or polar format."""
__author__ = "Michael Alvear"

import math


def cart_to_pol(coords):
    """takes in a cartesian coordinate tuple and returns a
     polar coordinate tuple"""

    x_coord = coords[0]
    y_coord = coords[1]

    # performs necessary trigonometry to convert from cartesian to
    # polar coordinates

    radius = (x_coord ** 2 + y_coord ** 2) ** (1 / 2)

    # I am manipulating theta in a way such that radius can always be positive.
    if x_coord > 0:

        theta = math.atan(y_coord / x_coord)

    elif x_coord < 0:

        theta = math.atan(y_coord / x_coord) + math.pi

    elif x_coord == 0 and y_coord > 0:

        theta = math.pi / 2

    elif x_coord == 0 and y_coord < 0:
        theta = (3 * math.pi) / 2

    else:

        theta = 0

    return (radius, theta)


def pol_to_cart(coords):
    """takes in a polar coordinate tuple and returns a
    cartesian coordinate tuple"""

    radius = coords[0]
    theta = coords[1]

    # performs necessary trigonometry to convert from polar to
    # cartesian coordinates
    x_coord = math.cos(theta) * radius
    y_coord = math.sin(theta) * radius

    return (x_coord, y_coord)


class Vector:
    """This is the main vector class, it expects cartesian coordinates as
    a tuple"""

    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def add(self, other_vector):
        """adds the value of another vector to the instance of the vector on
        which this method is called"""

        self.x += other_vector.x
        self.y += other_vector.y

    def get_sum(self, other_vector):
        """similar to add but simply returns the value of the sum vector
        instead of changing the vector instance"""

        return (self.x + other_vector.x, self.y + other_vector.y)

    def subtract(self, other_vector):
        """subtracts the value of another vector from the instance of the
        vector on which this method is called"""

        self.x -= other_vector.x
        self.y -= other_vector.y

    def get_difference(self, other_vector):
        """similar to subtract but simply returns the value of the
        difference vector instead of changing the vector instance"""

        return (self.x - other_vector.x, self.y - other_vector.y)

    def multiply(self, scalar):
        """multiplies vector instance by given scalar"""

        self.x *= scalar
        self.y *= scalar

    def get_product(self, scalar):
        """returns tuple of the product of multiplying the vector instance
        by the given scalar"""

        return (self.x * scalar, self.y * scalar)

    def divide(self, scalar):
        """divides vector instance by given scalar"""

        self.x /= scalar
        self.y /= scalar

    def get_quotient(self, scalar):
        """returns tuple of the quotient of dividing the vector instance
        by the given scalar"""

        return (self.x / scalar, self.y / scalar)

    def get_magnitude(self):
        """returns the magnitude of the vector instance this method is
        called on"""

        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def normalize(self):
        """normalizes the vector, turning it into its unit vector"""

        # in this case im converting the vector into a polar coordinate with a
        # radius of one and then turning it back into a cartesian coordinate
        unit_vector = pol_to_cart((1, cart_to_pol((self.x, self.y))[1]))

        self.x = unit_vector[0]
        self.y = unit_vector[1]

    def get_unit_vector(self):
        """similar to normalize but simply returns the value of the unit
        vector"""

        return pol_to_cart((1, cart_to_pol((self.x, self.y))[1]))

    def get_value(self):
        """return a tuple of the x and y coordinates of the vector"""
        return (self.x, self.y)
