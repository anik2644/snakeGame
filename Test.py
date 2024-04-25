import glfw
from OpenGL.GL import *
import sys

W, H = 1000, 600
foodList = []
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

    # print("Food List:", foodList)

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

    # Define the endpoints of the line
    x1, y1 = -100.0, 50.0
    x2, y2 = 100.0, 50.0

    # Set the color to white
    glColor3ub(255, 255, 255)

    # Draw the line
    draw_line(x1, y1, x2, y2)

    # Draw all points from the food list
    for point in foodList:
        # Set the color to white
        glColor3ub(255, 255, 255)
        glPointSize(3.0) 
        # Draw a point at each coordinate
        glBegin(GL_POINTS)
        glVertex2f(point[0], point[1])
        glEnd()

    glfw.swap_buffers(Window)
    glfw.poll_events()

    while not glfw.window_should_close(Window):
        if glfw.get_key(Window, glfw.KEY_ESCAPE) == glfw.PRESS:
            break
        glfw.wait_events()

    glfw.terminate()

main()

