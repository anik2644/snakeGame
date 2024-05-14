
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL as GL
import glfw
import time
import sys
import math




# Function to calculate the new position of the snake's body
def SnakeSize(x, y, Snake_direction, sizeofSnake):
    # Calculate the tail position based on the direction and size of the snake
    if Snake_direction == "left":
        return x + 30 + sizeofSnake, y
    elif Snake_direction == "right":
        return x - 30 - sizeofSnake, y
    elif Snake_direction == "up":
        return x, y - 30 - sizeofSnake
    elif Snake_direction == "down":
        return x, y + 30 + sizeofSnake

# Function to draw the snake on the screen
def draw_Snake(x,y, Snake_direction, sizeofSnake):

    x1, y1 = SnakeSize(x, y, Snake_direction, sizeofSnake) # determine the tail of the snake


    # Set width of the snake
    glLineWidth(4.0)
    # Draw the body
    glBegin(GL_LINES)
    glColor3ub(0, 255, 0)  # Green color for the body
    glVertex2f(x, y)
    glVertex2f(x1, y1)
    glEnd()

    # Draw the point (x1, y1) with a different color to mention head
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glColor3ub(255, 0, 0)  # Red color for the Head
    glVertex2f(x, y)
    glEnd()