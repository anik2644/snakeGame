# initialize.py

# Import necessary libraries
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL as GL
import glfw

# This function initializes everything to run the OpenGL snake game 
def initialize(W, H):
    global Window

    # Initialize GLFW
    if not glfw.init():
        return None

    # Create a window
    Window = glfw.create_window(W, H, "Line and Points", None, None)
    
    # Check if window creation failed
    if not Window:
        glfw.terminate()
        return None

    # Make the window's context current
    glfw.make_context_current(Window)
    
    # Clear buffers and set up projection matrix
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-W / 2, W / 2, -H / 2, H / 2, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Return the window object
    return Window
