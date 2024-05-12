from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw
import sys
import time

W, H = 1200, 800
number = 88

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


characters = {
    'A': [1, 1, 1, 0, 1, 1, 1],
    'B': [1, 1, 1, 1, 1, 1, 0],
    'C': [1, 0, 0, 1, 1, 1, 1],
    'D': [1, 1, 1, 1, 1, 0, 1],
    'E': [1, 0, 0, 1, 1, 1, 1],
    'F': [1, 0, 0, 0, 1, 1, 1],
    'G': [1, 0, 1, 1, 1, 1, 1],
    'H': [0, 1, 1, 0, 1, 1, 0],
    'I': [1, 1, 0, 0, 1, 1, 0],
    'J': [0, 1, 1, 0, 1, 1, 1],
    'K': [0, 1, 1, 0, 1, 0, 0],
    'L': [0, 0, 0, 1, 1, 1, 1],
    'M': [1, 1, 1, 0, 1, 1, 0],
    'N': [1, 1, 1, 0, 1, 1, 0],
    'O': [1, 1, 1, 1, 1, 1, 1],
    'P': [1, 1, 0, 0, 1, 1, 1],
    'Q': [1, 1, 1, 1, 1, 1, 0],
    'R': [1, 1, 0, 0, 1, 1, 0],
    'S': [1, 0, 1, 1, 0, 1, 1],
    'T': [1, 1, 0, 0, 1, 0, 0],
    'U': [0, 1, 1, 1, 1, 1, 1],
    'V': [0, 1, 1, 1, 1, 1, 1],
    'W': [1, 1, 1, 1, 1, 1, 1],
    'X': [0, 1, 1, 0, 1, 1, 0],
    'Y': [0, 1, 1, 0, 1, 0, 1],
    'Z': [1, 0, 1, 1, 1, 0, 1]
}


# Define segment positions relative to the center of the window
# segment_positions = [
#     [(10, 700), (110, 700)],  # Top
#     [(300, 700), (300, 650)],  # Right top
#     [(300, 650), (300, 600)],  # Right bottom
#     [(10, 300), (110, 300)],  # Bottom
#     [(100, 650), (100, 600)],  # Left bottom
#     [(100, 700), (100, 650)],  # Left top
#     [(10, 500), (110, 500)]   # Middle
# ]

segment_positions = [
    [(20, 725), (60, 725)],    # Top
    [(60, 725), (60, 675)],    # Right top
    [(60, 675), (60, 625)],    # Right bottom
    [(20, 625), (60, 625)],    # Bottom
    [(20, 675), (20, 625)],    # Left bottom
    [(20, 725), (20, 675)],    # Left top
    [(20, 675), (60, 675)]     # Middle
]


def draw_segment(x1, y1, x2, y2):
    glLineWidth(4.0)
    glBegin(GL_LINES)
    glColor3ub(0, 255, 0)  # Green color for the body
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def draw_number():
    global number
    glColor3f(1.0, 1.0, 1.0)

    # For three-digit numbers, draw the first digit
    if number >= 100:
        for i, segment in enumerate(segments[number // 100]):
            if segment:
                x1 = segment_positions[i][0][0]  # Shift the position for the second digit
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


def display():
    global number
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    # Draw the rectangle border
    glColor3ub(255, 255, 255)  # White color for the border
    glLineWidth(2.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(10, 600)     # Bottom left corner
    glVertex2f(10, 750)    # Top left corner
    glVertex2f(300, 750)   # Top right corner
    glVertex2f(300, 600)    # Bottom right corner
    glEnd()
    
    # Draw the digits
    draw_number()
    
    glfw.swap_buffers(Window)
    time.sleep(0.1)
    number = (number + 1) % 1000  # Cycle through numbers 0 to 999




def key_callback(window, key, scancode, action, mods):
    global number
    if action == glfw.PRESS:
        if key == glfw.KEY_0:
            number = 0
        elif key == glfw.KEY_1:
            number = 1
        elif key == glfw.KEY_2:
            number = 2
        elif key == glfw.KEY_3:
            number = 3
        elif key == glfw.KEY_4:
            number = 4
        elif key == glfw.KEY_5:
            number = 5
        elif key == glfw.KEY_6:
            number = 6
        elif key == glfw.KEY_7:
            number = 7
        elif key == glfw.KEY_8:
            number = 8
        elif key == glfw.KEY_9:
            number = 9

        while not glfw.window_should_close(Window):
            display()

        # Print the number in the console
        print("Number:", number)


def main():
    global Window
    if not glfw.init():
        return

    Window = glfw.create_window(W, H, "Number Display", None, None)
    if not Window:
        glfw.terminate()
        return

    glfw.make_context_current(Window)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, W, 0, H, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glfw.set_key_callback(Window, key_callback)

    while not glfw.window_should_close(Window):
        display()
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
