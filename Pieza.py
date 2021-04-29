import pygame
import numpy as np

class Pieza:
    def __init__(self, screen ,myfont, x, y, number):

        self.screen = screen
        self.myfont = myfont

        self.initX = x
        self.initY = y

        self.x = x
        self.y = y

        self.number = number

        self.contador = 0


    def moverDerecha(self):
        if(self.x-self.initX < 100):
            print(self.x-self.initX)
            self.x = self.x + 1
            return True
        else:
            return False

    def moverIzquierda(self):
        if(self.initX-self.x < 100):
            print(self.initX-self.x)
            self.x = self.x - 1
            return True
        else:
            return False
    
    def moverArriba(self):
        if(self.initY-self.y < 100):
            print(self.initY-self.y)
            self.y = self.y - 1
            return True
        else:
            return False

    def moverAbajo(self):
        if(self.y-self.initY < 100):
            print(self.y-self.initY)
            self.y = self.y + 1
            return True
        else:
            return False

    def dibujar(self):
        if self.number != 0:
            textsurface = self.myfont.render(str(self.number), False, (255, 255, 255))
            self.screen.blit(textsurface,(self.x+45,self.y+45))
            pygame.draw.rect(self.screen, (0, 100, 255), (self.x, self.y, 100, 100), 1)