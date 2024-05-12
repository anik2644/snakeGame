from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw

# Define the size of the window
W, H = 500, 500

# Define the dot matrix pattern for character 'A'
CHAR_A = [
    "  *  ",
    " * * ",
    "*   *",
    "*****",
    "*   *",
    "*   *"
]

def draw_dot(x, y):
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def display_char(char_pattern):
    for j, row in enumerate(reversed(char_pattern)):
        for i, dot in enumerate(reversed(row)):
            if dot == "*":
                draw_dot(50 + i * 10, 50 + j * 10)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Draw the character 'A' using the dot matrix
    display_char(CHAR_A)

    glfw.swap_buffers(Window)

def main():
    global Window
    if not glfw.init():
        return

    Window = glfw.create_window(W, H, "Dot Matrix Display", None, None)
    if not Window:
        glfw.terminate()
        return

    glfw.make_context_current(Window)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-W / 2, W / 2, -H / 2, H / 2, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    while not glfw.window_should_close(Window):
        glfw.poll_events()
        display()

    glfw.terminate()

if __name__ == "__main__":
    main()
