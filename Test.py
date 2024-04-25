import glfw
from OpenGL.GL import *
import sys
import time

W, H = 1000, 600
foodList = []

# Snake position
snake_x = 500.0
snake_y = 50.0
reverse_direction = False

def draw_line(x1, y1, x2, y2, color):
    # Set the line width
    glLineWidth(6.0)

    # Draw the line
    glBegin(GL_LINES)
    glColor3ub(*color)  # Set color
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

    # Draw the point (x1, y1) with a different color
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glColor3ub(255, 0, 0)  # Red color for the point
    glVertex2f(x1, y1)
    glEnd()

def draw_snake_head(x, y, direction):
    # Set the line width
    glLineWidth(8.0)

    # Draw the head based on the direction
    if direction == "right":
        glBegin(GL_LINES)
        glColor3ub(255, 0, 0)  # Red color for the head
        glVertex2f(x, y)
        glVertex2f(x + 6, y)  # Make the head slightly larger
        glEnd()
    elif direction == "left":
        glBegin(GL_LINES)
        glColor3ub(255, 0, 0)  # Red color for the head
        glVertex2f(x, y)
        glVertex2f(x - 6, y)  # Make the head slightly larger
        glEnd()

def draw_snake_body(x, y):
    # Set the line width
    glLineWidth(6.0)

    # Draw the body
    glBegin(GL_LINES)
    glColor3ub(0, 255, 0)  # Green color for the body
    glVertex2f(x, y)
    glVertex2f(x + 50, y)
    glEnd()

def move_snake():
    global snake_x
    global snake_y
    global reverse_direction

    # Check if the snake reached the edge of the window
    if snake_x <= -W/2 or snake_x >= W/2:
        reverse_direction = not reverse_direction

    # Move the snake in the appropriate direction
    if reverse_direction:
        snake_x -= 10
    else:
        snake_x += 10

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

        # Draw all points from the food list
        for point in foodList:
            glColor3ub(255, 255, 255)  # White color for the points
            glPointSize(3.0)  # Set point size
            glBegin(GL_POINTS)
            glVertex2f(point[0], point[1])
            glEnd()

        # Draw the snake's head at its current position
        if reverse_direction:
            draw_snake_head(snake_x, snake_y, "left")
        else:
            draw_snake_head(snake_x, snake_y, "right")

        # Draw the snake's body
        draw_snake_body(snake_x, snake_y)

        # Swap buffers
        glfw.swap_buffers(Window)
        glfw.poll_events()

        # Pause for 0.1 seconds
        time.sleep(0.1)

        # Move the snake
        move_snake()

    glfw.terminate()

main()
