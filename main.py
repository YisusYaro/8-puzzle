import pygame
from Display import Display
from Controller import Controller
from Puzzle import Puzzle
import numpy as np


puzzle = Puzzle()
#display = Display()
#controller = Controller(puzzle)
#print(puzzle.operadores(np.matrix([[1,0,2],[3,4,5],[6,7,8]])))
puzzle.bfs()
#display.runDisplay()

