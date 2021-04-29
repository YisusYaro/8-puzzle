import pygame
import numpy as np

from Pieza import Pieza

class Tablero:
    def __init__(self, screen ,myfont):
        self.screen = screen
        self.myfont = myfont


    def setEstado(self, estado):
        self.estado = estado

        self.piezas = {}
        
        self.piezas[0,0] = Pieza(self.screen, self.myfont, 0, 0, self.estado[0,0])
        self.piezas[0,1] = Pieza(self.screen, self.myfont, 100, 0, self.estado[0,1])
        self.piezas[0,2] = Pieza(self.screen, self.myfont, 200, 0, self.estado[0,2])
        self.piezas[1,0] = Pieza(self.screen, self.myfont, 0, 100, self.estado[1,0])
        self.piezas[1,1] = Pieza(self.screen, self.myfont, 100, 100, self.estado[1,1])
        self.piezas[1,2] = Pieza(self.screen, self.myfont, 200, 100, self.estado[1,2])
        self.piezas[2,0] = Pieza(self.screen, self.myfont, 0, 200, self.estado[2,0])
        self.piezas[2,1] = Pieza(self.screen, self.myfont, 100, 200, self.estado[2,1])
        self.piezas[2,2] = Pieza(self.screen, self.myfont, 200, 200, self.estado[2,2])


    def animar(self, i1, j1, i2, j2 ):
        print(i1,j1,i2,j2)

    def dibujar(self):
        for pieza in self.piezas:
            self.piezas[pieza].dibujar()
        