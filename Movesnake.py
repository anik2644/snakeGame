from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL as GL
import glfw

def move_snake(snake_x, snake_y, Snake_direction, reverse_direction, paused, W, H):
    if not paused:
        # Move the snake in the appropriate direction along the y-axis or x-axis based on keyboard input
        if Snake_direction == "up":
            if reverse_direction:
                snake_y -= 10
            else:
                snake_y += 10
        elif Snake_direction == "down":
            if reverse_direction:
                snake_y += 10
            else:
                snake_y -= 10
        elif Snake_direction == "left":
            if reverse_direction:
                snake_x += 10
            else:
                snake_x -= 10
        elif Snake_direction == "right":
            if reverse_direction:
                snake_x -= 10
            else:
                snake_x += 10

        # Check if the snake reached the top, bottom, left, or right edge of the window
        if snake_y <= -H/2 or snake_y >= H/2 or snake_x <= -W/2 or snake_x >= W/2:
            return None, None, 1  # Game over
        else:
            return snake_x, snake_y, 0  # Continue game
    else:
        return snake_x, snake_y, 0  # Continue game
