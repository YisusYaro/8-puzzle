import pygame
from Display import Display
from Controller import Controller
from Puzzle import Puzzle
import numpy as np


puzzle = Puzzle()
display = Display()
controller = Controller(puzzle)
print(puzzle.bfs())
display.runDisplay()

