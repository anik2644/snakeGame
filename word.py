from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL as GL
import glfw
import time
import sys
import math
# from character import Characters



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
    "*    ",
    "*    ",
    "*    ",
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

CHAR_0 = [
    " *** ",
    "*   *",
    "*   *",
    "*   *",
    " *** "
]

CHAR_1 = [
    "  *  ",
    " **  ",
    "  *  ",
    "  *  ",
    " *** "
]

CHAR_2 = [
    " *** ",
    "*   *",
    "   * ",
    "  *  ",
    "*****"
]

CHAR_3 = [
    " *** ",
    "    *",
    " *** ",
    "    *",
    " *** "
]
CHAR_4 = [
    "*  * ",
    "*  * ",
    "*****",
    "   * ",
    "   * "
]

CHAR_5 = [
    "*****",
    "*    ",
    "**** ",
    "    *",
    "**** "
]

CHAR_6 = [
    " *** ",
    "*    ",
    "**** ",
    "*   *",
    " *** "
]

CHAR_7 = [
    "*****",
    "    *",
    "   * ",
    "  *  ",
    " *   "
]

CHAR_8 = [
    " *** ",
    "*   *",
    " *** ",
    "*   *",
    " *** "
]

CHAR_9 = [
    " *** ",
    "*   *",
    " ****",
    "    *",
    " ****"
]
Semicolon = [
    "  *  ",
    "  *  ",
    "     ",
    "  *  ",
    "  *  "
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
  ' ': Space,
  '0': CHAR_0,
  '1': CHAR_1,
  '2': CHAR_2,
  '3': CHAR_3,
  '4': CHAR_4,
  '5': CHAR_5,
  '6': CHAR_6,
  '7': CHAR_7,
  '8': CHAR_8,
  '9': CHAR_9,
  ':': Semicolon
  # ... and so on for all lowercase characters
}



# Rainbow colors
def rainbow_color(index, total):
    # Calculate the color using sine function to create a rainbow effect
    r = math.sin(index / total * math.pi * 2 + 0) * 0.5 + 0.5
    g = math.sin(index / total * math.pi * 2 + 2) * 0.5 + 0.5
    b = math.sin(index / total * math.pi * 2 + 4) * 0.5 + 0.5
    return r, g, b

def draw_dot(x, y, color):
    GL.glPointSize(5.0)
    GL.glColor3f(*color)
    GL.glBegin(GL.GL_POINTS)
    GL.glVertex2f(x, y)
    GL.glEnd()

def display_char(char_pattern, x_offset, color):
    for j, row in enumerate(reversed(char_pattern)):
        for i, dot in enumerate(row):
            if dot == "*":
                draw_dot(x_offset + i * 10, 50 + j * 10, color)
                
                
    


def ddisplay_word(Window, word):
    word_width = sum(len(Characters[char][0]) * 10 for char in word)
    x_offset = -word_width / 2  # Center the word

    GL.glClear(GL.GL_COLOR_BUFFER_BIT)

    for i, char in enumerate(word):
        if char in Characters:
            color = (1.0, 1.0, 1.0)  # Set color to white
            display_char(Characters[char], x_offset, color)
            x_offset += len(Characters[char][0]) * 10 + 10  # Increase x_offset for the next character

    glfw.swap_buffers(Window)



                
def display_word(Window,word, animate):
    word_width = sum(len(Characters[char][0]) * 10 for char in word)
    x_offset = -word_width / 2  # Center the word
    
    if animate:
        for i, char in enumerate(word):
            if char in Characters:
                color = rainbow_color(i, len(word))
                display_char(Characters[char], x_offset, color)
                glfw.swap_buffers(Window)  # Swap buffers to display the character
                time.sleep(0.4)  # Add delay for animation
                x_offset += len(Characters[char][0]) * 10 + 10  # Increase x_offset for the next character
               
    else:
        for i, char in enumerate(word):
            if char in Characters:
                color = (1.0, 1.0, 1.0)  # Set color to white (no animation)
                glfw.swap_buffers(Window)
                display_char(Characters[char], x_offset, color)
                x_offset += len(Characters[char][0]) * 10 + 10  # Increase x_offset for the next character
            time.sleep(.4)

    GL.glClear(GL.GL_COLOR_BUFFER_BIT)