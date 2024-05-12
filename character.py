from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw
import sys
import time

# Define the size of the window
W, H = 1200, 800

# Define the dot matrix pattern for character 'A'
# CHAR_A = [
#         " ****",
#         "*    ",
#         "*    ",
#         "*    ",
#         " ****"
# ]

CHAR_A = [
    "  *  ",
    " * * ",
    "*****",
    "*   *",
    "*   *"
]

CHAR_B = [
    "**** ",
    "*   *",
    "**** ",
    "*   *",
    "**** "
]

CHAR_C = [
    " *** ",
    "*   *",
    "*    ",
    "*   *",
    " *** "
]

CHAR_D = [
    "**** ",
    "*   *",
    "*   *",
    "*   *",
    "**** "
]

CHAR_E = [
    "*****",
    "*    ",
    "***  ",
    "*    ",
    "*****"
]

CHAR_F = [
    "*****",
    "*    ",
    "***  ",
    "*    ",
    "*    "
]

CHAR_G = [
    " *** ",
    "*    ",
    "*  **",
    "*   *",
    " *** "
]

CHAR_H = [
    "*   *",
    "*   *",
    "*****",
    "*   *",
    "*   *"
]

CHAR_I = [
    " *** ",
    "  *  ",
    "  *  ",
    "  *  ",
    " *** "
]

CHAR_J = [
    "   **",
    "   * ",
    "   * ",
    "*  * ",
    " **  "
]

CHAR_K = [
    "*   *",
    "*  * ",
    "***  ",
    "*  * ",
    "*   *"
]

CHAR_L = [
    "*    ",
    "*    ",
    "*    ",
    "*    ",
    "*****"
]

CHAR_M = [
    "*   *",
    "** **",
    "* * *",
    "*   *",
    "*   *"
]

CHAR_N = [
    "*   *",
    "**  *",
    "* * *",
    "*  **",
    "*   *"
]

CHAR_O = [
    " *** ",
    "*   *",
    "*   *",
    "*   *",
    " *** "
]

CHAR_P = [
    "**** ",
    "*   *",
    "**** ",
    "*    ",
    "*    "
]


CHAR_P = [
    "**** ",
    "*   *",
    "**** ",
    "*    ",
    "*    "
]

CHAR_Q = [
    " *** ",
    "*   *",
    "*   *",
    "*  **",
    " *** "
]

CHAR_R = [
    "**** ",
    "*   *",
    "**** ",
    "*  * ",
    "*   *"
]

CHAR_S = [
    " *** ",
    "*    ",
    " *** ",
    "    *",
    " *** "
]

CHAR_T = [
    "*****",
    "  *  ",
    "  *  ",
    "  *  ",
    "  *  "
]

CHAR_U = [
    "*   *",
    "*   *",
    "*   *",
    "*   *",
    " *** "
]

CHAR_V = [
    "*   *",
    "*   *",
    " * * ",
    " * * ",
    "  *  "
]

CHAR_W = [
    "*   *",
    "*   *",
    "* * *",
    "** **",
    "*   *"
]

CHAR_X = [
    "*   *",
    " * * ",
    "  *  ",
    " * * ",
    "*   *"
]

CHAR_Y = [
    "*   *",
    " * * ",
    "  *  ",
    "  *  ",
    "  *  "
]

CHAR_Z = [
    "*****",
    "   * ",
    "  *  ",
    " *   ",
    "*****"
]

Characters = [
    CHAR_A,
    CHAR_B,
    CHAR_C,
    CHAR_D,
    CHAR_E,
    CHAR_F,
    CHAR_G,
    CHAR_H,
    CHAR_I,
    CHAR_J,
    CHAR_K,
    CHAR_L,
    CHAR_M,
    CHAR_N,
    CHAR_O,
    CHAR_P,
    CHAR_Q,
    CHAR_R,
    CHAR_S,
    CHAR_T,
    CHAR_U,
    CHAR_V,
    CHAR_W,
    CHAR_X,
    CHAR_Y,
    CHAR_Z
]


def draw_dot(x, y):
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def display_char(char_pattern):
    for j, row in enumerate(reversed(char_pattern)):
        for i, dot in enumerate((row)):
            if dot == "*":
                draw_dot(50 + i * 10, 50 + j * 10)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Draw the character 'A' using the dot matrix
    for char in Characters:
        glClear(GL_COLOR_BUFFER_BIT)
        display_char(char)
        glfw.swap_buffers(Window)
        time.sleep(1)  # Pause for 1 second between characters
        # glfw.wait_events_timeout(1) 
        

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
