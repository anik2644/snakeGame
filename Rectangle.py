from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL as GL
import glfw
import time
import sys
import math



def draw_rectangle_outline(width, height, edge_width):
    half_width = width / 2
    half_height = height / 2
    
    glLineWidth(edge_width)
    glColor3ub(255, 0, 0)  # White color
    
    glBegin(GL_LINE_LOOP)
    glVertex2f(-half_width, -half_height)  # Bottom left corner
    glVertex2f(half_width, -half_height)   # Bottom right corner
    glVertex2f(half_width, half_height)    # Top right corner
    glVertex2f(-half_width, half_height)   # Top left corner
    glEnd()
    
    