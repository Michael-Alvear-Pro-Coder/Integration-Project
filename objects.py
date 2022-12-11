"""This file contains the physics object class code,
so far its only one object: Ball"""
__author__ = "Michael Alvear"

import pygame
import pygame.gfxdraw
import vectors as v


class Ball:
    """this is a ball physics object"""

    def __init__(self, pos, vel, mass, radius, color, surface):
        self.pos = v.Vector(pos)
        self.vel = v.Vector(vel)
        self.mass = mass
        self.radius = radius
        self.color = color
        self.surface = surface

    def apply_force(self, force):
        """applies a force to the object"""

        # using newtons second law here to calculate how force will affect
        # the object's acceleration
        # everybody knows: F = ma, therefore: F/m = a
        my_force = v.Vector(force)
        my_acceleration = v.Vector(my_force.get_quotient(self.mass))

        self.vel.add(my_acceleration)

    def gravitize(self, point, g_constant):
        """applies a gravity force pointing to the given point at the
        specified strength using newtons gravitational attraction formula"""

        # turning the given point into a vector for calculations
        my_point_vector = v.Vector(point)

        # using vector subtraction to determine the direction of the
        # gravitational force
        my_force = v.Vector(my_point_vector.get_difference(self.pos))

        # finding the distance between the ball and the attractor and
        # constraining it, so it never gets too big or too small
        distance = my_force.get_magnitude()

        if distance > 25:

            distance = 25

        elif distance < 18:

            distance = 18

        # normalizing the force and multiplying it by the strength
        my_force.normalize()

        strength = (g_constant * self.mass) / (distance ** 2)

        my_force.multiply(strength)

        # applying the gravitational force to the ball
        self.apply_force(my_force.get_value())

    def update(self):
        """updates the position of the ball"""

        self.pos.add(self.vel)

    def draw(self):
        """uses pygame to draw the ball on the surface"""
        pygame.gfxdraw.filled_circle(self.surface, int(self.pos.x),
                                     int(self.pos.y), self.radius, self.color)
