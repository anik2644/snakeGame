import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys
import time

W, H = 1200, 800
current_number = 1  # Current number to display
display_duration = 0.1  # Duration to display each number (in seconds)
Window = None  # Global variable for the window


def draw_number(number):
    global Window  # Make Window accessible in the function
    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Set up orthographic projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-W/2, W/2, -H/2, H/2, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Set up color for the pixels
    glColor3ub(255, 255, 255)  # White color
    
    # Define pixel positions for each digit
    digits = {
       '0': [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (2, 2), (0, 3), (2, 3), (0, 4), (2, 4), (0, 5), (1, 5), (2, 5)],
        '1': [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5)],
        '2': [(0, 0), (1, 0), (2, 0), (2, 1), (0, 2), (1, 2), (2, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5)],
        '3': [(0, 0), (1, 0), (2, 0), (2, 1), (1, 2), (2, 2), (2, 3), (1, 4), (2, 4), (0, 5), (1, 5), (2, 5)],
        '4': [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5)],
        '5': [(0, 0), (1, 0), (2, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (0, 5), (1, 5), (2, 5)],
        '6': [(0, 0), (1, 0), (2, 0), (0, 1), (0, 2), (1, 2), (2, 2), (0, 3), (2, 3), (0, 4), (1, 4), (2, 4), (0, 5), (1, 5), (2, 5)],
        '7': [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5)],
        '8': [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2), (0, 3), (2, 3), (0, 4), (2, 4), (0, 5), (1, 5), (2, 5)],
        '9': [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (2, 5)]
    }
    
    # Get the digit positions for the current number
    number_str = str(number)
    digit_positions = [digits[digit] for digit in number_str]
    
    # Define spacing between digits
    digit_spacing = 5  # Adjust this value as needed
    
    # Draw pixels for each digit
    for i, digit_pos in enumerate(digit_positions):
        for px, py in digit_pos:
            glBegin(GL_POINTS)
            # Adjust x and y positions based on digit index and spacing
            glVertex2f(i * (len(digit_pos) + digit_spacing) + px - (len(number_str) * (len(digit_pos) + digit_spacing)) / 2, py)
            glEnd()
    
    # Swap buffers
    glfw.swap_buffers(Window)

def main():
    global Window, current_number
    
    if not glfw.init():
        return

    Window = glfw.create_window(W, H, "Display Numbers", None, None)
    if not Window:
        glfw.terminate()
        return

    glfw.make_context_current(Window)

    # Set up the main loop to display numbers
    while not glfw.window_should_close(Window) and current_number <= 100:
        draw_number(current_number)
        glfw.poll_events()
        
        # Pause for the specified duration
        time.sleep(display_duration)
        
        # Move to the next number
        current_number += 1

    glfw.terminate()

if __name__ == "__main__":
    main()
