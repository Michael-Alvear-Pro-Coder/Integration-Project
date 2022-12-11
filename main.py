"""this is the main file"""
__author__ = "Michael Alvear"

import pygame
import pygame.gfxdraw
import sys
import random
import objects


def explanation_prompt():
    """explanation of how the program works"""

    input("\n\nHello, this program is a little demonstration of forces and "
          "vectors in pygame, inspired by Daniel Shiffman's"
          " fantastic book: 'The Nature of Code'.\n\n"
          ""
          "This program lets you place an 'attractor' around the "
          "screen by left-clicking where you want to place it.\n\n"
          ""
          "You can then spawn in balls which are attracted"
          " to the attractor by pressing right-click.\n\n"
          ""
          "If you create too many balls "
          "you can middle click to clear the screen.\n\n"
          ""
          "Press enter to start, have fun!")


def main_loop():
    """this is the main loop function"""
    FPS = 60
    WIDTH, HEIGHT = 1000, 1000
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    CENTER = (WIDTH / 2, HEIGHT / 2)
    BACKGROUND_COLOR = (0, 0, 0)

    ball_list = []
    ball_radius = 25
    ball_mass = 10

    attractor_location = CENTER
    gravitational_constant = 150
    attractor_radius = 37
    attractor_color = (255, 0, 0)

    my_attractor = objects.Ball(attractor_location, (0, 0), 1,
                                attractor_radius, attractor_color, WIN)

    while (True):

        # this line limits the FPS
        pygame.time.Clock().tick(FPS)

        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and \
                    pygame.mouse.get_pressed()[2] and len(ball_list) <= 50:

                mouse_x, mouse_y = pygame.mouse.get_pos()

                ball_list.append(objects.Ball(
                    (mouse_x, mouse_y),
                    (0, 0), ball_mass, ball_radius, (random.randint(0, 255),
                                                     random.randint(0, 255),
                                                     random.randint(0, 255)),
                    WIN))

                print("new ball")

            elif event.type == pygame.MOUSEBUTTONDOWN and \
                    pygame.mouse.get_pressed()[0]:

                mouse_x, mouse_y = pygame.mouse.get_pos()

                attractor_location = (mouse_x, mouse_y)

                my_attractor = objects.Ball(attractor_location, (0, 0),
                                            1,
                                            attractor_radius, attractor_color,
                                            WIN)

                print("moved attractor")

            elif event.type == pygame.MOUSEBUTTONDOWN and \
                    pygame.mouse.get_pressed()[1]:

                ball_list = []

                print("balls erased")

        # logic area

        for ball in ball_list:
            ball.gravitize(attractor_location, gravitational_constant)
            ball.update()

        # Drawing area
        WIN.fill(BACKGROUND_COLOR)

        my_attractor.draw()

        for ball in ball_list:
            ball.draw()

        pygame.display.update()


# execution
if __name__ == "__main__":
    explanation_prompt()
    main_loop()
