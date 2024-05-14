import OpenGL.GLUT as GLUT
import OpenGL.GL as GL
import OpenGL.GLU as GLU
import glfw
import sys
from Initialization import initialize
from word import Characters
from OpenGL.GLUT import glutInit

# Define the size of the window
W, H = 1200, 800


# Function to draw a dot at given coordinates
def draw_dot(x, y):
    GL.glPointSize(5.0)
    GL.glBegin(GL.GL_POINTS)
    GL.glVertex2f(x, y)
    GL.glEnd()

# Function to display a character at given offset
def display_char(char_pattern, x_offset, y_offset):
    for j, row in enumerate(reversed(char_pattern)):
        for i, dot in enumerate(row):
            if dot == "*":
                draw_dot(x_offset + i * 10, y_offset + j * 10)

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

# Function to display everything
def display():
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    GL.glLoadIdentity()

    # Display the word "NEW GAME"
    display_word("NEW GAME", -250, 200)

    # Display buttons for "LEVEL ONE" and "LEVEL TWO"
    display_button("LEVEL ONE", -250, 100)
    display_button("LEVEL TWO", -10, 100)

    glfw.swap_buffers(Window)

# Main function
def main():

  
    global Window
    if not glfw.init():
        return

    Window = glfw.create_window(W, H, "Dot Matrix Display", None, None)
    # GLUT.glutInit()  # Initialize GLUT here
    glutInit()


    if not Window:
        glfw.terminate()
        return
    
 

    glfw.make_context_current(Window)

    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    GLU.gluOrtho2D(-W / 2, W / 2, -H / 2, H / 2)
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GL.glLoadIdentity()


    while not glfw.window_should_close(Window):
        glfw.poll_events()
        display()

    glfw.terminate()

if __name__ == "__main__":
    main()
    glfw.swap_buffers(Window)
