import glfw
from OpenGL.GL import *
import sys
import time

W, H = 1200, 800
foodList = []
foodindex=0
Snake_direction = "down"
sizeofSnake=0
bonusDelay = 3
# Snake position
snake_x = 50.0
snake_y = 50.0
reverse_direction = False
paused = False

total_score  =0

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

def move_snake():
    global snake_y, snake_x, Snake_direction, reverse_direction

    if not paused:
        # Check if the snake reached the top, bottom, left, or right edge of the window
        if snake_y <= -H/2:
            snake_y = H/2
        elif snake_y >= H/2:
            snake_y = -H/2
        if snake_x <= -W/2:
            snake_x = W/2
        elif snake_x >= W/2:
            snake_x = -W/2

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

def check_food_consume(snake_x, snake_y, food_point):
    
    global foodList,sizeofSnake,foodindex,bonusDelay,total_score

    food_x, food_y = food_point
    
    tolerance = 10 
    if(foodindex%bonusDelay==bonusDelay-1):
       tolerance = 35   # Set point size
    else:
        glPointSize(5.0)


    if abs(snake_x - food_x) <= tolerance and abs(snake_y - food_y) <= tolerance:
      if(foodindex%bonusDelay==bonusDelay-1):
            total_score+= 50   #bonus
      else:
            total_score+=5


      print("totalscore: ",total_score)  
      sizeofSnake+=8
      foodindex+=1
      return True
    
    return False

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

from OpenGL.GLUT import *

def render_score():
    glPushMatrix()
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(-W/2, W/2, -H/2, H/2, -1, 1)
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(-W/2 + 10, H/2 - 30)
    for char in "Score: " + str(total_score):
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ctypes.c_int(ord(char)))
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()

def main():
    global paused , sizeofSnake,foodindex,bonusDelay

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
 
        point = foodList[foodindex%100]
        glColor3ub(255, 255, 255)  # White color for the points
        
        if(foodindex%bonusDelay==bonusDelay-1):
            glPointSize(30.0)  # Set point size
        else:
            glPointSize(5.0)


        glBegin(GL_POINTS)
        glVertex2f(point[0], point[1])
        glEnd()
        

        check_food_consume(snake_x,snake_y,point)
        render_score()  # Render the score on the screen
        draw_Snake(snake_x, snake_y)
        glfw.swap_buffers(Window)
        glfw.poll_events()

        # Pause for 0.1 seconds
        time.sleep(0.05)
        #sizeofSnake+=5
        # Move the snake
        move_snake()

    glfw.terminate()

main()
