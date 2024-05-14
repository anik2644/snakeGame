from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL as GL
import glfw
import time
import sys
import math



from Rectangle import draw_rectangle_outline 
from word import display_word,ddisplay_word
from Score import render_score
from DrawSnake import draw_Snake
from CheckFoodConsume import check_food_consume
from FoodList import getFood
from Initialization import initialize
# from welcome import display_Welcome

W, H = 1200, 800
foodList = []
foodindex = 0
Snake_direction = "down"
sizeofSnake = 0
bonusDelay = 3
# Snake position
snake_x = 50.0
snake_y = 50.0
reverse_direction = False
paused = False
total_score = 0

gameOver = 0





def move_snake():
    global snake_y, snake_x, Snake_direction, reverse_direction,gameOver

    if not paused:
        # Check if the snake reached the top, bottom, left, or right edge of the window
        if snake_y <= -H/2:
            gameOver = 1
        elif snake_y >= H/2:
            gameOver = 1
        if snake_x <= -W/2:
            gameOver = 1
        elif snake_x >= W/2:
            gameOver = 1

        # Move the snake in the appropriate direction along the y-axis or x-axis
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




def key_callback(window, key, scancode, action, mods):
    global paused, Snake_direction

    if key == glfw.KEY_SPACE and action == glfw.PRESS:
        paused = not paused
    elif key == glfw.KEY_UP and action == glfw.PRESS:
        Snake_direction = "up"
    elif key == glfw.KEY_DOWN and action == glfw.PRESS:
        Snake_direction = "down"
    elif key == glfw.KEY_LEFT and action == glfw.PRESS:
        Snake_direction = "left"
    elif key == glfw.KEY_RIGHT and action == glfw.PRESS:
        Snake_direction = "right"






def main():
    global paused, sizeofSnake, foodindex, bonusDelay, total_score,Window,gameOver
    W, H = 1200, 800  
    
    Window = initialize(W, H)
    if Window is None:
        return




    glfw.set_key_callback(Window, key_callback)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    GL.glLoadIdentity()

    # Display the word "WELCOME" with animation

    # ddisplay_word(Window,"HELLO015")
    # time.sleep(2.5)



    display_word(Window,"WELCOME",True)
    glfw.swap_buffers(Window)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    

    foodList = getFood()

    while not glfw.window_should_close(Window):
        glClear(GL_COLOR_BUFFER_BIT)

        point = foodList[foodindex % 100]
        glColor3ub(255, 255, 255)  # White color for the points

        if (foodindex % bonusDelay == bonusDelay - 1):
            glPointSize(30.0)  # Set point size
        else:
            glPointSize(5.0)


        draw_rectangle_outline(W, H, 4)


        glBegin(GL_POINTS)
        glVertex2f(point[0], point[1])
        glEnd()

        
        food_consumed, total_score,sizeofSnake, foodindex  = check_food_consume(snake_x, snake_y, point,foodList, sizeofSnake, foodindex, bonusDelay, total_score)



        draw_Snake(snake_x, snake_y, Snake_direction, sizeofSnake)
        render_score(total_score)  # Render the score on the screen
        
        glfw.swap_buffers(Window)
        glfw.poll_events()
 
 
        if(gameOver==1):
            glClear(GL_COLOR_BUFFER_BIT)
            display_word(Window,"GAME OVER",True)
            glfw.swap_buffers(Window)
            break 
        # Pause for 0.1 seconds
        time.sleep(0.05)
        move_snake()


    
    toshow = "YOUR SCORE:"+ str(total_score)
    glfw.swap_buffers(Window)
    ddisplay_word(Window,toshow)
    time.sleep(2.5)



    glfw.terminate()

main()
