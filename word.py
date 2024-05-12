import OpenGL.GLUT as GLUT
import OpenGL.GL as GL
import OpenGL.GLU as GLU
import glfw
import sys

# Define the size of the window
W, H = 1200, 800

# Define the dot matrix patterns for each character

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
Space = [
    "     ",
    "     ",
    "     ",
    "     ",
    "     "
]

Characters = {
  'A': CHAR_A,
  'B': CHAR_B,
  'C': CHAR_C,
  'D': CHAR_D,
  'E': CHAR_E,
  'F': CHAR_F,
  'G': CHAR_G,
  'H': CHAR_H,
  'I': CHAR_I,
  'J': CHAR_J,
  'K': CHAR_K,
  'L': CHAR_L,
  'M': CHAR_M,
  'N': CHAR_N,
  'O': CHAR_O,
  'P': CHAR_P,
  'Q': CHAR_Q,
  'R': CHAR_R,
  'S': CHAR_S,
  'T': CHAR_T,
  'U': CHAR_U,
  'V': CHAR_V,
  'W': CHAR_W,
  'X': CHAR_X,
  'Y': CHAR_Y,
  'Z': CHAR_Z,
  ' ': Space
  # ... and so on for all lowercase characters
}


def draw_dot(x, y):
    GL.glPointSize(5.0)
    GL.glBegin(GL.GL_POINTS)
    GL.glVertex2f(x, y)
    GL.glEnd()

def display_char(char_pattern, x_offset):
    for j, row in enumerate(reversed(char_pattern)):
        for i, dot in enumerate(row):
            if dot == "*":
                draw_dot(x_offset + i * 10, 50 + j * 10)

def display_word(word):
    x_offset = -500
    for char in word:
        if char in Characters:
            display_char(Characters[char], x_offset)
            x_offset += 70  # Increase x_offset for the next character

def display():
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    GL.glLoadIdentity()

    # Display the word "ANIK"
    display_word("NEW GAME")
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

    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    GLU.gluOrtho2D(-W / 2, W / 2, -H / 2, H / 2)
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GL.glLoadIdentity()

    while not glfw.window_should_close(Window):
        glfw.poll_events()
        display()

    glfw.terminate()

if __name__ == "__main__":
    main()
