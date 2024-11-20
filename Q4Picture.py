# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import pygame

from pygame import Color, Rect
from pygame import draw
from pygame import display

SCREEN_SIZE = (500, 500)

# initialize pygame modules
pygame.init()

# get a surface for graphics display
gameDisplay = display.set_mode(SCREEN_SIZE)

# background - color of the ocean
gameDisplay.fill(Color('blue'))

# draw back fin of the fish
draw.polygon(gameDisplay, Color('black'), [(100, 300), (400, 300), (250, 200)])


# draw ocean floor
draw.rect(gameDisplay, Color('yellow'), Rect(0, 400, 500, 100))

# draw seaweed
draw.rect(gameDisplay, Color('green'), Rect(10, 400, 10, 100))

# draw the fish's head
draw.circle(gameDisplay, Color('pink'), (250, 105), 100)

# show the graphics on the screen
display.flip()

# Wait for user input before closing the window
input("Press enter to exit")
