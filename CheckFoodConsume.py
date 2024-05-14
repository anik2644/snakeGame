
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL as GL
import glfw
import time
import sys
import math

def check_food_consume(snake_x, snake_y, food_point, foodList, sizeofSnake, foodindex, bonusDelay, total_score):
    # global foodList, sizeofSnake, foodindex, bonusDelay, total_score

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
        return True, total_score,sizeofSnake, foodindex  # Return True along with total_score if food is consumed

    return False, total_score,sizeofSnake, foodindex  # Return False along with total_score if food is not consumed
