import glfw
from OpenGL.GL import *
import sys
import time

W, H = 1000, 600
foodList = []

# Snake position
snake_x = 500.0
snake_y = 50.0

def draw_line(x1, y1, x2, y2):
    # Set the line width
    glLineWidth(6.0)

    # Draw the line
    glBegin(GL_LINES)
    glColor3ub(0, 255, 0)  # Green color for the line
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

    # Draw the point (x1, y1) with a different color
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glColor3ub(255, 0, 0)  # Red color for the point
    glVertex2f(x1, y1)
    glEnd()

def move_snake():
    global snake_x
    # Increment the snake's x-coordinate
    snake_x -= 10

def main():
    # Read the food list from the file
    with open('foods.txt', 'r') as file:
        content = file.read()
        lines = content.split('\n')
        foodList = []
        for line in lines:
            if line:
                pair = line.split(', ')
                foodList.append((int(pair[0]), int(pair[1])))

    if not glfw.init():
        return

    Window = glfw.create_window(W, H, "Line and Points", None, None)
    if not Window:
        glfw.terminate()
        return

    glfw.make_context_current(Window)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-W/2, W/2, -H/2, H/2, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    while not glfw.window_should_close(Window):
        glClear(GL_COLOR_BUFFER_BIT)

        # Draw the line
      #  draw_line(-100.0, 50.0, -50.0, 50.0)
        
        # Draw all points from the food list
        for point in foodList:
            glColor3ub(255, 255, 255)  # White color for the points
            glPointSize(3.0)  # Set point size
            glBegin(GL_POINTS)
            glVertex2f(point[0], point[1])
            glEnd()

        # Draw the snake at its current position
        draw_line(snake_x, snake_y, snake_x + 50, snake_y)

        # Swap buffers
        glfw.swap_buffers(Window)
        glfw.poll_events()

        # Pause for 0.5 seconds
        time.sleep(0.1)

        # Move the snake
        move_snake()

    glfw.terminate()

main()
