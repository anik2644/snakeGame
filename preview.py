from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL as GL
import glfw
import time
import sys
import math


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




# Define the dot matrix patterns for each character

CHAR_A = [
    "  *  ",
    " * * ",
    "*****",
    "*   *",
    "*   *"
]

CHAR_B = [
    "**** ",
    "*   *",
    "**** ",
    "*   *",
    "**** "
]

CHAR_C = [
    " *** ",
    "*    ",
    "*    ",
    "*    ",
    " *** "
]

CHAR_D = [
    "**** ",
    "*   *",
    "*   *",
    "*   *",
    "**** "
]

CHAR_E = [
    "*****",
    "*    ",
    "***  ",
    "*    ",
    "*****"
]

CHAR_F = [
    "*****",
    "*    ",
    "***  ",
    "*    ",
    "*    "
]

CHAR_G = [
    " *** ",
    "*    ",
    "*  **",
    "*   *",
    " *** "
]

CHAR_H = [
    "*   *",
    "*   *",
    "*****",
    "*   *",
    "*   *"
]

CHAR_I = [
    " *** ",
    "  *  ",
    "  *  ",
    "  *  ",
    " *** "
]

CHAR_J = [
    "   **",
    "   * ",
    "   * ",
    "*  * ",
    " **  "
]

CHAR_K = [
    "*   *",
    "*  * ",
    "***  ",
    "*  * ",
    "*   *"
]

CHAR_L = [
    "*    ",
    "*    ",
    "*    ",
    "*    ",
    "*****"
]

CHAR_M = [
    "*   *",
    "** **",
    "* * *",
    "*   *",
    "*   *"
]

CHAR_N = [
    "*   *",
    "**  *",
    "* * *",
    "*  **",
    "*   *"
]

CHAR_O = [
    " *** ",
    "*   *",
    "*   *",
    "*   *",
    " *** "
]

CHAR_P = [
    "**** ",
    "*   *",
    "**** ",
    "*    ",
    "*    "
]


CHAR_P = [
    "**** ",
    "*   *",
    "**** ",
    "*    ",
    "*    "
]

CHAR_Q = [
    " *** ",
    "*   *",
    "*   *",
    "*  **",
    " *** "
]

CHAR_R = [
    "**** ",
    "*   *",
    "**** ",
    "*  * ",
    "*   *"
]

CHAR_S = [
    " *** ",
    "*    ",
    " *** ",
    "    *",
    " *** "
]

CHAR_T = [
    "*****",
    "  *  ",
    "  *  ",
    "  *  ",
    "  *  "
]

CHAR_U = [
    "*   *",
    "*   *",
    "*   *",
    "*   *",
    " *** "
]

CHAR_V = [
    "*   *",
    "*   *",
    " * * ",
    " * * ",
    "  *  "
]

CHAR_W = [
    "*   *",
    "*   *",
    "* * *",
    "** **",
    "*   *"
]

CHAR_X = [
    "*   *",
    " * * ",
    "  *  ",
    " * * ",
    "*   *"
]

CHAR_Y = [
    "*   *",
    " * * ",
    "  *  ",
    "  *  ",
    "  *  "
]

CHAR_Z = [
    "*****",
    "   * ",
    "  *  ",
    " *   ",
    "*****"
]
Space = [
    "     ",
    "     ",
    "     ",
    "     ",
    "     "
]

Characters = {
  'A': CHAR_A,
  'B': CHAR_B,
  'C': CHAR_C,
  'D': CHAR_D,
  'E': CHAR_E,
  'F': CHAR_F,
  'G': CHAR_G,
  'H': CHAR_H,
  'I': CHAR_I,
  'J': CHAR_J,
  'K': CHAR_K,
  'L': CHAR_L,
  'M': CHAR_M,
  'N': CHAR_N,
  'O': CHAR_O,
  'P': CHAR_P,
  'Q': CHAR_Q,
  'R': CHAR_R,
  'S': CHAR_S,
  'T': CHAR_T,
  'U': CHAR_U,
  'V': CHAR_V,
  'W': CHAR_W,
  'X': CHAR_X,
  'Y': CHAR_Y,
  'Z': CHAR_Z,
  ' ': Space
  # ... and so on for all lowercase characters
}


# Rainbow colors
def rainbow_color(index, total):
    # Calculate the color using sine function to create a rainbow effect
    r = math.sin(index / total * math.pi * 2 + 0) * 0.5 + 0.5
    g = math.sin(index / total * math.pi * 2 + 2) * 0.5 + 0.5
    b = math.sin(index / total * math.pi * 2 + 4) * 0.5 + 0.5
    return r, g, b

def draw_dot(x, y, color):
    GL.glPointSize(5.0)
    GL.glColor3f(*color)
    GL.glBegin(GL.GL_POINTS)
    GL.glVertex2f(x, y)
    GL.glEnd()

def display_char(char_pattern, x_offset, color):
    for j, row in enumerate(reversed(char_pattern)):
        for i, dot in enumerate(row):
            if dot == "*":
                draw_dot(x_offset + i * 10, 50 + j * 10, color)
                
                
    

# Function to display a word
def display_word(word, x_offset, y_offset):
    for char in word:
        if char in Characters:
            display_char(Characters[char], x_offset, y_offset)
            x_offset += 70  # Increase x_offset for the next character

# Function to display buttons
def display_button(label, x, y):
    GL.glColor3f(0.5, 0.5, 0.5)  # Gray color for the button
    GL.glBegin(GL.GL_QUADS)
    GL.glVertex2f(x, y)
    GL.glVertex2f(x + 200, y)
    GL.glVertex2f(x + 200, y + 50)
    GL.glVertex2f(x, y + 50)
    GL.glEnd()

    GL.glColor3f(1.0, 1.0, 1.0)  # White color for the text
    GL.glRasterPos2f(x + 10, y + 20)
    GLUT.glutBitmapString(GLUT.GLUT_BITMAP_HELVETICA_18, label.encode())        
                
                
                
                
                
def display_word(word, animate=True):
    word_width = sum(len(Characters[char][0]) * 10 for char in word)
    x_offset = -word_width / 2  # Center the word
    
    if animate:
        for i, char in enumerate(word):
            if char in Characters:
                color = rainbow_color(i, len(word))
                display_char(Characters[char], x_offset, color)
                glfw.swap_buffers(Window)  # Swap buffers to display the character
                time.sleep(0.4)  # Add delay for animation
                x_offset += len(Characters[char][0]) * 10 + 10  # Increase x_offset for the next character
               
    else:
        for i, char in enumerate(word):
            if char in Characters:
                color = (1.0, 1.0, 1.0)  # Set color to white (no animation)
                display_char(Characters[char], x_offset, color)
                x_offset += len(Characters[char][0]) * 10 + 10  # Increase x_offset for the next character

    GL.glClear(GL.GL_COLOR_BUFFER_BIT)

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
    glVertex2f(-550, 350)    # Top left corner
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
   


def draw_rectangle(W, H, width):
    # Calculate half width for convenience
    half_width = width / 2
    
    # Set the color to red
    glColor3ub(255, 0, 0)  # Red color
    
    # Adjust vertices to add width to the rectangle
    glBegin(GL_QUADS)
    # Bottom edge
    glVertex2f(-W / 2 - half_width, -H / 2 - half_width)  # Bottom left corner
    glVertex2f(W / 2 + half_width, -H / 2 - half_width)   # Bottom right corner
    glVertex2f(W / 2 + half_width, -H / 2 + half_width)   # Top right corner
    glVertex2f(-W / 2 - half_width, -H / 2 + half_width)  # Top left corner
    
    # Top edge
    glVertex2f(-W / 2 - half_width, H / 2 - half_width)   # Bottom left corner
    glVertex2f(W / 2 + half_width, H / 2 - half_width)    # Bottom right corner
    glVertex2f(W / 2 + half_width, H / 2 + half_width)    # Top right corner
    glVertex2f(-W / 2 - half_width, H / 2 + half_width)   # Top left corner
    
    # Left edge
    glVertex2f(-W / 2 - half_width, -H / 2 - half_width)  # Bottom left corner
    glVertex2f(-W / 2 + half_width, -H / 2 - half_width)  # Bottom right corner
    glVertex2f(-W / 2 + half_width, H / 2 + half_width)   # Top right corner
    glVertex2f(-W / 2 - half_width, H / 2 + half_width)   # Top left corner
    
    # Right edge
    glVertex2f(W / 2 - half_width, -H / 2 - half_width)   # Bottom left corner
    glVertex2f(W / 2 + half_width, -H / 2 - half_width)   # Bottom right corner
    glVertex2f(W / 2 + half_width, H / 2 + half_width)    # Top right corner
    glVertex2f(W / 2 - half_width, H / 2 + half_width)    # Top left corner
    
    glEnd()

def draw_rectangle_outline(width, height, edge_width):
    half_width = width / 2
    half_height = height / 2
    
    glLineWidth(edge_width)
    glColor3ub(255, 0, 0)  # White color
    
    glBegin(GL_LINE_LOOP)
    glVertex2f(-half_width, -half_height)  # Bottom left corner
    glVertex2f(half_width, -half_height)   # Bottom right corner
    glVertex2f(half_width, half_height)    # Top right corner
    glVertex2f(-half_width, half_height)   # Top left corner
    glEnd()
    
    

def main():
    global paused, sizeofSnake, foodindex, bonusDelay, total_score,Window,gameOver

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
    
    
    # display_Welcome(Window)




    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    GL.glLoadIdentity()

    # Display the word "WELCOME" with animation
    display_word("WELCOME")
    glfw.swap_buffers(Window)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    
    
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


        draw_rectangle_outline(W, H, 4)


        glBegin(GL_POINTS)
        glVertex2f(point[0], point[1])
        glEnd()

        check_food_consume(snake_x, snake_y, point)
        draw_Snake(snake_x, snake_y)
        render_score()  # Render the score on the screen
        
        glfw.swap_buffers(Window)
        glfw.poll_events()
 
 
        if(gameOver==1):
            display_word("GAME OVER")
            # glfw.swap_buffers(Window)
            return 
        # Pause for 0.1 seconds
        time.sleep(0.05)
        move_snake()

    glfw.terminate()

main()

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL as GL
import glfw
import time
import sys
import math


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




# Define the dot matrix patterns for each character

CHAR_A = [
    "  *  ",
    " * * ",
    "*****",
    "*   *",
    "*   *"
]

CHAR_B = [
    "**** ",
    "*   *",
    "**** ",
    "*   *",
    "**** "
]

CHAR_C = [
    " *** ",
    "*    ",
    "*    ",
    "*    ",
    " *** "
]

CHAR_D = [
    "**** ",
    "*   *",
    "*   *",
    "*   *",
    "**** "
]

CHAR_E = [
    "*****",
    "*    ",
    "***  ",
    "*    ",
    "*****"
]

CHAR_F = [
    "*****",
    "*    ",
    "***  ",
    "*    ",
    "*    "
]

CHAR_G = [
    " *** ",
    "*    ",
    "*  **",
    "*   *",
    " *** "
]

CHAR_H = [
    "*   *",
    "*   *",
    "*****",
    "*   *",
    "*   *"
]

CHAR_I = [
    " *** ",
    "  *  ",
    "  *  ",
    "  *  ",
    " *** "
]

CHAR_J = [
    "   **",
    "   * ",
    "   * ",
    "*  * ",
    " **  "
]

CHAR_K = [
    "*   *",
    "*  * ",
    "***  ",
    "*  * ",
    "*   *"
]

CHAR_L = [
    "*    ",
    "*    ",
    "*    ",
    "*    ",
    "*****"
]

CHAR_M = [
    "*   *",
    "** **",
    "* * *",
    "*   *",
    "*   *"
]

CHAR_N = [
    "*   *",
    "**  *",
    "* * *",
    "*  **",
    "*   *"
]

CHAR_O = [
    " *** ",
    "*   *",
    "*   *",
    "*   *",
    " *** "
]

CHAR_P = [
    "**** ",
    "*   *",
    "**** ",
    "*    ",
    "*    "
]


CHAR_P = [
    "**** ",
    "*   *",
    "**** ",
    "*    ",
    "*    "
]

CHAR_Q = [
    " *** ",
    "*   *",
    "*   *",
    "*  **",
    " *** "
]

CHAR_R = [
    "**** ",
    "*   *",
    "**** ",
    "*  * ",
    "*   *"
]

CHAR_S = [
    " *** ",
    "*    ",
    " *** ",
    "    *",
    " *** "
]

CHAR_T = [
    "*****",
    "  *  ",
    "  *  ",
    "  *  ",
    "  *  "
]

CHAR_U = [
    "*   *",
    "*   *",
    "*   *",
    "*   *",
    " *** "
]

CHAR_V = [
    "*   *",
    "*   *",
    " * * ",
    " * * ",
    "  *  "
]

CHAR_W = [
    "*   *",
    "*   *",
    "* * *",
    "** **",
    "*   *"
]

CHAR_X = [
    "*   *",
    " * * ",
    "  *  ",
    " * * ",
    "*   *"
]

CHAR_Y = [
    "*   *",
    " * * ",
    "  *  ",
    "  *  ",
    "  *  "
]

CHAR_Z = [
    "*****",
    "   * ",
    "  *  ",
    " *   ",
    "*****"
]
Space = [
    "     ",
    "     ",
    "     ",
    "     ",
    "     "
]

Characters = {
  'A': CHAR_A,
  'B': CHAR_B,
  'C': CHAR_C,
  'D': CHAR_D,
  'E': CHAR_E,
  'F': CHAR_F,
  'G': CHAR_G,
  'H': CHAR_H,
  'I': CHAR_I,
  'J': CHAR_J,
  'K': CHAR_K,
  'L': CHAR_L,
  'M': CHAR_M,
  'N': CHAR_N,
  'O': CHAR_O,
  'P': CHAR_P,
  'Q': CHAR_Q,
  'R': CHAR_R,
  'S': CHAR_S,
  'T': CHAR_T,
  'U': CHAR_U,
  'V': CHAR_V,
  'W': CHAR_W,
  'X': CHAR_X,
  'Y': CHAR_Y,
  'Z': CHAR_Z,
  ' ': Space
  # ... and so on for all lowercase characters
}


# Rainbow colors
def rainbow_color(index, total):
    # Calculate the color using sine function to create a rainbow effect
    r = math.sin(index / total * math.pi * 2 + 0) * 0.5 + 0.5
    g = math.sin(index / total * math.pi * 2 + 2) * 0.5 + 0.5
    b = math.sin(index / total * math.pi * 2 + 4) * 0.5 + 0.5
    return r, g, b

def draw_dot(x, y, color):
    GL.glPointSize(5.0)
    GL.glColor3f(*color)
    GL.glBegin(GL.GL_POINTS)
    GL.glVertex2f(x, y)
    GL.glEnd()

def display_char(char_pattern, x_offset, color):
    for j, row in enumerate(reversed(char_pattern)):
        for i, dot in enumerate(row):
            if dot == "*":
                draw_dot(x_offset + i * 10, 50 + j * 10, color)
                
                
    

# Function to display a word
def display_word(word, x_offset, y_offset):
    for char in word:
        if char in Characters:
            display_char(Characters[char], x_offset, y_offset)
            x_offset += 70  # Increase x_offset for the next character

# Function to display buttons
def display_button(label, x, y):
    GL.glColor3f(0.5, 0.5, 0.5)  # Gray color for the button
    GL.glBegin(GL.GL_QUADS)
    GL.glVertex2f(x, y)
    GL.glVertex2f(x + 200, y)
    GL.glVertex2f(x + 200, y + 50)
    GL.glVertex2f(x, y + 50)
    GL.glEnd()

    GL.glColor3f(1.0, 1.0, 1.0)  # White color for the text
    GL.glRasterPos2f(x + 10, y + 20)
    GLUT.glutBitmapString(GLUT.GLUT_BITMAP_HELVETICA_18, label.encode())        
                
                
                
                
                
def display_word(word, animate=True):
    word_width = sum(len(Characters[char][0]) * 10 for char in word)
    x_offset = -word_width / 2  # Center the word
    
    if animate:
        for i, char in enumerate(word):
            if char in Characters:
                color = rainbow_color(i, len(word))
                display_char(Characters[char], x_offset, color)
                glfw.swap_buffers(Window)  # Swap buffers to display the character
                time.sleep(0.4)  # Add delay for animation
                x_offset += len(Characters[char][0]) * 10 + 10  # Increase x_offset for the next character
               
    else:
        for i, char in enumerate(word):
            if char in Characters:
                color = (1.0, 1.0, 1.0)  # Set color to white (no animation)
                display_char(Characters[char], x_offset, color)
                x_offset += len(Characters[char][0]) * 10 + 10  # Increase x_offset for the next character

    GL.glClear(GL.GL_COLOR_BUFFER_BIT)

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
    glVertex2f(-550, 350)    # Top left corner
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
   


def draw_rectangle(W, H, width):
    # Calculate half width for convenience
    half_width = width / 2
    
    # Set the color to red
    glColor3ub(255, 0, 0)  # Red color
    
    # Adjust vertices to add width to the rectangle
    glBegin(GL_QUADS)
    # Bottom edge
    glVertex2f(-W / 2 - half_width, -H / 2 - half_width)  # Bottom left corner
    glVertex2f(W / 2 + half_width, -H / 2 - half_width)   # Bottom right corner
    glVertex2f(W / 2 + half_width, -H / 2 + half_width)   # Top right corner
    glVertex2f(-W / 2 - half_width, -H / 2 + half_width)  # Top left corner
    
    # Top edge
    glVertex2f(-W / 2 - half_width, H / 2 - half_width)   # Bottom left corner
    glVertex2f(W / 2 + half_width, H / 2 - half_width)    # Bottom right corner
    glVertex2f(W / 2 + half_width, H / 2 + half_width)    # Top right corner
    glVertex2f(-W / 2 - half_width, H / 2 + half_width)   # Top left corner
    
    # Left edge
    glVertex2f(-W / 2 - half_width, -H / 2 - half_width)  # Bottom left corner
    glVertex2f(-W / 2 + half_width, -H / 2 - half_width)  # Bottom right corner
    glVertex2f(-W / 2 + half_width, H / 2 + half_width)   # Top right corner
    glVertex2f(-W / 2 - half_width, H / 2 + half_width)   # Top left corner
    
    # Right edge
    glVertex2f(W / 2 - half_width, -H / 2 - half_width)   # Bottom left corner
    glVertex2f(W / 2 + half_width, -H / 2 - half_width)   # Bottom right corner
    glVertex2f(W / 2 + half_width, H / 2 + half_width)    # Top right corner
    glVertex2f(W / 2 - half_width, H / 2 + half_width)    # Top left corner
    
    glEnd()

def draw_rectangle_outline(width, height, edge_width):
    half_width = width / 2
    half_height = height / 2
    
    glLineWidth(edge_width)
    glColor3ub(255, 0, 0)  # White color
    
    glBegin(GL_LINE_LOOP)
    glVertex2f(-half_width, -half_height)  # Bottom left corner
    glVertex2f(half_width, -half_height)   # Bottom right corner
    glVertex2f(half_width, half_height)    # Top right corner
    glVertex2f(-half_width, half_height)   # Top left corner
    glEnd()
    
    

def main():
    global paused, sizeofSnake, foodindex, bonusDelay, total_score,Window,gameOver

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
    
    
    # display_Welcome(Window)




    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    GL.glLoadIdentity()

    # Display the word "WELCOME" with animation
    display_word("WELCOME")
    glfw.swap_buffers(Window)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    
    
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


        draw_rectangle_outline(W, H, 4)


        glBegin(GL_POINTS)
        glVertex2f(point[0], point[1])
        glEnd()

        check_food_consume(snake_x, snake_y, point)
        draw_Snake(snake_x, snake_y)
        render_score()  # Render the score on the screen
        
        glfw.swap_buffers(Window)
        glfw.poll_events()
     
        scr = str(total_score)
        scr = "Total Score"
 
        if(gameOver==1):
            display_word("GAME OVER")
            # glfw.swap_buffers(Window)
            return 
        # Pause for 0.1 seconds
        time.sleep(0.05)
        move_snake()

    glfw.terminate()

main()