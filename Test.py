import glfw
from OpenGL.GL import *
import sys
import time

W, H = 1000, 600
foodList = []

Snake_direction = "down"
sizeofSnake=0
# Snake position
snake_x = 50.0
snake_y = 50.0
reverse_direction = False
paused = False

def SnakeSize(x, y):
    global Snake_direction, sizeofSnake
    
    if Snake_direction == "left":
        return x + 30 + sizeofSnake, y
    elif Snake_direction == "right":
        return x - 30 - sizeofSnake, y
    elif Snake_direction == "up":
        return x, y - 30 - sizeofSnake
    elif Snake_direction == "down":
        return x, y + 30 + sizeofSnake



def draw_Snake(x,y):
    # Set the line width
    x1, y1 = SnakeSize(x, y)
    glLineWidth(4.0)
    # Draw the body
    glBegin(GL_LINES)
    glColor3ub(0, 255, 0)  # Green color for the body
    glVertex2f(x, y)
    glVertex2f(x1 , y1)
    glEnd()

    # Draw the point (x1, y1) with a different color
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glColor3ub(255, 0, 0)  # Red color for the point
    glVertex2f(x, y)
    glEnd()


def draw_snake_head(x, y, direction):
    # Set the line width
    glLineWidth(8.0)

    # Draw the head based on the direction
    if direction == "right":
        glPointSize(10.0)
        glBegin(GL_POINTS)
        glColor3ub(255, 0, 0)  # Red color for the point
        glVertex2f(x, y)
        glEnd()
    elif direction == "left":
        glPointSize(10.0)
        glBegin(GL_POINTS)
        glColor3ub(255, 0, 0)  # Red color for the point
        glVertex2f(x, y)
        glEnd()

def draw_snake_body(x, y):
    # Set the line width
    glLineWidth(6.0)

    # Draw the body
    glBegin(GL_LINES)
    glColor3ub(0, 255, 0)  # Green color for the body
    glVertex2f(x, y)
    glVertex2f(x , y-50)
    glEnd()

def move_snake():
    global snake_y
    global reverse_direction

    if not paused:
        # Check if the snake reached the top or bottom edge of the window
        if snake_y <= -H/2:
            snake_y = H/2
        elif snake_y >= H/2:
            snake_y = -H/2

        # Move the snake in the appropriate direction along the y-axis
        if reverse_direction:
            snake_y -= 10
        else:
            snake_y += 10

def key_callback(window, key, scancode, action, mods):
    global paused

    if key == glfw.KEY_SPACE and action == glfw.PRESS:
        paused = not paused

def main():
    global paused

    if not glfw.init():
        return

    Window = glfw.create_window(W, H, "Line and Points", None, None)
    if not Window:
        glfw.terminate()
        return

    # Set up the keyboard callback
    glfw.set_key_callback(Window, key_callback)
    glfw.make_context_current(Window)


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-W/2, W/2, -H/2, H/2, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


    # Read the food list from the file
    with open('foods.txt', 'r') as file:
        content = file.read()
        lines = content.split('\n')
        foodList = []
        for line in lines:
            if line:
                pair = line.split(', ')
                foodList.append((int(pair[0]), int(pair[1])))


    while not glfw.window_should_close(Window):
        glClear(GL_COLOR_BUFFER_BIT)

        # Draw all points from the food list
        for point in foodList:
            glColor3ub(255, 255, 255)  # White color for the points
            glPointSize(3.0)  # Set point size
            glBegin(GL_POINTS)
            glVertex2f(point[0], point[1])
            glEnd()

        draw_Snake(snake_x, snake_y)
        # Draw the snake's head at its current position
        # Draw the snake's body

        # draw_snake_body(snake_x, snake_y)

        # if reverse_direction:
        #     draw_snake_head(snake_x, snake_y, "left")
        # else:
        #     draw_snake_head(snake_x, snake_y, "right")

        # Swap buffers
        glfw.swap_buffers(Window)
        glfw.poll_events()

        # Pause for 0.1 seconds
        time.sleep(0.1)

        # Move the snake
        move_snake()

    glfw.terminate()

main()
