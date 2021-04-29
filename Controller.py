from Puzzle import Puzzle
from Display import Display
from Animador import Animador

class Controller:

    def __init__(self):
        self.puzzle = Puzzle(self)
        self.animador = Animador()

    def init(self):
        self.animador.animar(self.puzzle.bfs())
        
