# Import necessary libraries
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL as GL
import glfw
import time
import sys
import math

# Function to read food coordinates from the Food basket and store those in a python list
def getFood() -> list:
    # Open the basket containing food coordinates
    with open('foods.txt', 'r') as file:
        # Read the content of the file
        content = file.read()
        # Split the content into lines
        lines = content.split('\n')
        # Create an empty list to store food coordinates
        foodList = []
        # Iterate through each line in the file
        for line in lines:
            # Check if the line is not empty
            if line:
                # Split the line into x and y coordinates
                pair = line.split(', ')
                # Convert coordinates to integers and add them to the foodList
                foodList.append((int(pair[0]), int(pair[1])))

    # Return the list of food coordinates
    return foodList
