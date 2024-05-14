 
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL as GL
import glfw
import time
import sys
import math 


def getFood() ->list:
   with open('foods.txt', 'r') as file:
           content = file.read()
           lines = content.split('\n')
           foodList = []
           for line in lines:
               if line:
                   pair = line.split(', ')
                   foodList.append((int(pair[0]), int(pair[1])))

   return foodList
   
