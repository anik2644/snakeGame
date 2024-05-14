from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL as GL
import glfw
import time

# Importing functions from other files
from OuterBorderRectangle import draw_rectangle_outline 
from word import display_word, ddisplay_word  # Assuming this is a typo and correcting it
from Score import render_score
from DrawSnake import draw_Snake
from CheckFoodConsume import check_food_consume
from FoodList import getFood
from Initialization import initialize
from Movesnake import move_snake
from ProvideFood import draw_food_point

# Global variables
W, H = 1200, 800  # Window width and height
foodList = []     # List to store food positions
foodindex = 0     # Index to keep track of current food item
Snake_direction = "down"  # Initial direction of the snake
sizeofSnake = 0           # Initial size of the snake
bonusDelay = 3            # Delay for bonus points
snake_x = 50.0            # Initial x-coordinate of the snake
snake_y = 50.0            # Initial y-coordinate of the snake
reverse_direction = False  # Flag to reverse the direction of the snake
paused = False            # Flag to pause the game
total_score = 0           # Total score of the player
gameOver = 0              # Flag to indicate if the game is over

# Callback function for keyboard input
def key_callback(window, key, scancode, action, mods):
    global paused, Snake_direction

    # Toggle pause when spacebar is pressed
    if key == glfw.KEY_SPACE and action == glfw.PRESS:
        paused = not paused
    # Change snake direction based on arrow keys
    elif key == glfw.KEY_UP and action == glfw.PRESS:
        Snake_direction = "up"
    elif key == glfw.KEY_DOWN and action == glfw.PRESS:
        Snake_direction = "down"
    elif key == glfw.KEY_LEFT and action == glfw.PRESS:
        Snake_direction = "left"
    elif key == glfw.KEY_RIGHT and action == glfw.PRESS:
        Snake_direction = "right"



def main():
    global paused, sizeofSnake, foodindex, bonusDelay, total_score,Window,gameOver,snake_x,snake_y
    W, H = 1200, 800  # Height and Width of the window

    # Initialize GLFW window
    Window = initialize(W, H)
    if Window is None:
        return

    # Set up keyboard callback
    glfw.set_key_callback(Window, key_callback)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    GL.glLoadIdentity()

    # Display welcome message
    display_word(Window, "WELCOME", True)
    glfw.swap_buffers(Window)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)

    # Get food positions
    foodList = getFood()

    # Main game loop
    while not glfw.window_should_close(Window):
        glClear(GL_COLOR_BUFFER_BIT)


        # Draw the outer border of the game area
        draw_rectangle_outline(W, H, 4)

        # Draw the food point
        point = foodList[foodindex % 100]
        draw_food_point(point, foodindex, bonusDelay)

        # Check if food is consumed and update game state
        food_consumed, total_score, sizeofSnake, foodindex = check_food_consume(snake_x, snake_y, point, foodList, sizeofSnake, foodindex, bonusDelay, total_score)

        # Draw the snake
        draw_Snake(snake_x, snake_y, Snake_direction, sizeofSnake)

        # Render the score on the screen
        render_score(total_score)

        # Swap buffers and poll events
        glfw.swap_buffers(Window)
        glfw.poll_events()

        # Move the snake
        snake_x, snake_y, gameOver = move_snake(snake_x, snake_y, Snake_direction, reverse_direction, paused, W, H)

        # Check if game over
        if gameOver == 1:
            glClear(GL_COLOR_BUFFER_BIT)
            display_word(Window, "GAME OVER", True)
            glfw.swap_buffers(Window)
            break 

        # increase this time for slow the snake or decrease to speed up the snake
        time.sleep(0.05)

    # Display final score
    toshow = "YOUR SCORE:" + str(total_score)
    glfw.swap_buffers(Window)
    ddisplay_word(Window, toshow)
    time.sleep(2.5)

    # Terminate GLFW
    glfw.terminate()

# Run the main function
if __name__ == "__main__":
    main()