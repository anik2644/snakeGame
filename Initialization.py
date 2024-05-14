# initialize.py

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL as GL
import glfw

def initialize(W, H):
    global Window

    if not glfw.init():
        return None

    Window = glfw.create_window(W, H, "Line and Points", None, None)
    
    if not Window:
        glfw.terminate()
        return None

    # Set up the keyboard callback
   
    glfw.make_context_current(Window)
    

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-W / 2, W / 2, -H / 2, H / 2, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    return Window
