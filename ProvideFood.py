from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL as GL
import glfw
import time
import sys
import math

# this function is responsible to show the current feed of the snake
def draw_food_point(point, foodindex, bonusDelay):
    glColor3ub(255, 255, 255)  # White color for the points
    
    if (foodindex % bonusDelay == bonusDelay - 1):
        glPointSize(30.0)  # Set point size for bonus
    else:
        glPointSize(5.0)   # Set regular point size

    glBegin(GL_POINTS)
    glVertex2f(point[0], point[1])  # Draw the food point
    glEnd()