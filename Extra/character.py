from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL as GL
import glfw
import time
import sys
import math

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
