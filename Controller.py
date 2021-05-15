from Puzzle import Puzzle
from Animador import Animador

class Controller:

    def __init__(self):
        self.puzzle = Puzzle(self)
        self.animador = Animador(self)


        
