from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL as GL
import glfw
import time
import sys
import math


# Define 7 segments position
segment_positions = [
    [(-520, 340), (-480, 340)],    # Top
    [(-480, 340), (-480, 290)],    # Right top
    [(-480, 290), (-480, 240)],    # Right bottom
    [(-520, 240), (-480, 240)],    # Bottom
    [(-520, 290), (-520, 240)],    # Left bottom
    [(-520, 340), (-520, 290)],    # Left top
    [(-520, 290), (-480, 290)]     # Middle
]



# Define segments for all the digits 
segments = {
    0: [1, 1, 1, 1, 1, 1, 0],
    1: [0, 1, 1, 0, 0, 0, 0],
    2: [1, 1, 0, 1, 1, 0, 1],
    3: [1, 1, 1, 1, 0, 0, 1],
    4: [0, 1, 1, 0, 0, 1, 1],
    5: [1, 0, 1, 1, 0, 1, 1],
    6: [1, 0, 1, 1, 1, 1, 1],
    7: [1, 1, 1, 0, 0, 0, 0],
    8: [1, 1, 1, 1, 1, 1, 1],
    9: [1, 1, 1, 1, 0, 1, 1]
}



# Function to draw a segment
def draw_segment(x1, y1, x2, y2):
    glLineWidth(4.0)
    glBegin(GL_LINES)
    glColor3ub(0, 255, 0)  # Green color for the body
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

# Function to draw a number
def draw_number(number):
    glColor3f(1.0, 1.0, 1.0)

    # Draw the first digit for three-digit numbers
    if number >= 100:
        for i, segment in enumerate(segments[number // 100]):
            if segment:
                x1 = segment_positions[i][0][0]  # Shift position for the second digit
                y1 = segment_positions[i][0][1]
                x2 = segment_positions[i][1][0]
                y2 = segment_positions[i][1][1]
                draw_segment(x1, y1, x2, y2)

    # Draw the second digit
    for i, segment in enumerate(segments[(number % 100) // 10]):
        if segment:
            x1 = segment_positions[i][0][0] + 80
            y1 = segment_positions[i][0][1]
            x2 = segment_positions[i][1][0] + 80
            y2 = segment_positions[i][1][1]
            draw_segment(x1, y1, x2, y2)

    # Draw the third digit
    for i, segment in enumerate(segments[number % 10]):
        if segment:
            x1 = segment_positions[i][0][0] + 160
            y1 = segment_positions[i][0][1]
            x2 = segment_positions[i][1][0] + 160
            y2 = segment_positions[i][1][1]
            draw_segment(x1, y1, x2, y2)

# Function to display the score
def display_score(number):
    glColor3ub(255, 255, 255)  # White color for the border
    glLineWidth(2.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-550, 230)     # Bottom left corner
    glVertex2f(-550, 350)     # Top left corner
    glVertex2f(-250, 350)     # Top right corner
    glVertex2f(-250, 230)     # Bottom right corner
    glEnd()

    draw_number(number)  # Draw the digits

# Function to render the score
def render_score(total_score):
    display_score(total_score)  # Render the score

# Note: The OpenGL context setup and main loop are assumed to be elsewhere in the code.
