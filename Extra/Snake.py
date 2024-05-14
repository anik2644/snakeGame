from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw
import sys
import time

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


segment_positions = [
    [(-520, 340), (-480, 340)],    # Top
    [(-480, 340), (-480, 290)],    # Right top
    [(-480, 290), (-480, 240)],    # Right bottom
    [(-520, 240), (-480, 240)],    # Bottom
    [(-520, 290), (-520, 240)],    # Left bottom
    [(-520, 340), (-520, 290)],    # Left top
    [(-520, 290), (-480, 290)]     # Middle
]

def draw_segment(x1, y1, x2, y2):
    glLineWidth(4.0)
    glBegin(GL_LINES)
    glColor3ub(0, 255, 0)  # Green color for the body
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def draw_number(number):
    
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



def display_score(number):
     
   # glClear(GL_COLOR_BUFFER_BIT)
   # glLoadIdentity()
    
    # Draw the rectangle border
    glColor3ub(255, 255, 255)  # White color for the border
    glLineWidth(2.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-550, 230)     # Bottom left corner
    glVertex2f(-550, 350)    # Top left cornerprojet
    glVertex2f(-250, 350)   # Top right corner
    glVertex2f(-250, 230)    # Bottom right corner
    glEnd()

    # Draw the digits
    draw_number(number)
    
    # glfw.swap_buffers(Window)
    # time.sleep(0.1)
    # number = (number + 1) % 1000  # Cycle through numbers 0 to 999



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
    glVertex2f(x1, y1)
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
    global foodList, sizeofSnake, foodindex, bonusDelay, total_score

    food_x, food_y = food_point

    tolerance = 10
    if (foodindex % bonusDelay == bonusDelay - 1):
        tolerance = 35  # Set point size
    else:
        glPointSize(5.0)

    if abs(snake_x - food_x) <= tolerance and abs(snake_y - food_y) <= tolerance:
        if (foodindex % bonusDelay == bonusDelay - 1):
            total_score += 50  # bonus
        else:
            total_score += 5

        print("Total Score: ", total_score)
        sizeofSnake += 8
        foodindex += 1
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

def render_score():
    global total_score
    display_score(total_score)
   

def main():
    global paused, sizeofSnake, foodindex, bonusDelay, total_score,Window

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
    glOrtho(-W / 2, W / 2, -H / 2, H / 2, -1, 1)
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

        point = foodList[foodindex % 100]
        glColor3ub(255, 255, 255)  # White color for the points

        if (foodindex % bonusDelay == bonusDelay - 1):
            glPointSize(30.0)  # Set point size
        else:
            glPointSize(5.0)

        glBegin(GL_POINTS)
        glVertex2f(point[0], point[1])
        glEnd()

        check_food_consume(snake_x, snake_y, point)
        draw_Snake(snake_x, snake_y)
        render_score()  # Render the score on the screen
        
        glfw.swap_buffers(Window)
        glfw.poll_events()

        # Pause for 0.1 seconds
        time.sleep(0.05)
        move_snake()

    glfw.terminate()

main()

