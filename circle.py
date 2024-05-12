from OpenGL.GL import *
from OpenGL.GLU import *
import glfw
import sys
import time
from math import pi, cos, sin

# Circle parameters
circle_radius = 0.5
circle_slices = 50

# Time variables
current_time = 0
change_color_time = 1  # Change color every 5 seconds

# Colors
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]  # Red, Green, Blue
color_index = 0
circle_color = colors[color_index]

# Function to draw circle
def draw_circle(radius, slices):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    for i in range(slices + 1):
        theta = i * (2 * pi / slices)
        x = radius * cos(theta)
        y = radius * sin(theta)
        glVertex2f(x, y)
    glEnd()

# Function to draw scene
def draw():
    global window
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Draw circle
    glColor3f(*circle_color)
    draw_circle(circle_radius, circle_slices)

    glfw.swap_buffers(window)

# Function to update
import time

# Function to update
def update():
    global current_time, color_index, circle_color

    # Get current time
    new_time = time.time()

    # Calculate time elapsed since last color change
    time_elapsed = new_time - current_time

    # Change color every 5 seconds
    if time_elapsed >= change_color_time:
        current_time = new_time
        color_index = (color_index + 1) % len(colors)
        circle_color = colors[color_index]


# Initialize OpenGL window
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

# Main function
def main():
    global window
    # Initialize GLFW
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 600, "Changing Color Circle", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Draw
        draw()
        # Update
        update()
        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
