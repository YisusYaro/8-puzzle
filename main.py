import pygame
from Display import Display
from Controller import Controller
from Puzzle import Puzzle


puzzle = Puzzle()
display = Display()
controller = Controller(puzzle)

display.runDisplay()

