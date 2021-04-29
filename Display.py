import pygame
import time
import numpy as np

from Tablero import Tablero

class Display:



    def __init__(self, controller):
        pygame.init()
        self.width = 400
        self.height = 300
        self.screen = pygame.display.set_mode([self.height, self.width])
        self.screen.fill((25, 25, 25))
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.cursorPositionDetector = False

        self.controller =  controller

        self.tablero = Tablero(self.screen ,self.myfont)

        self.inicial = True
        self.estadoInicial()
        self.final = False
        self.estadoFinal()

        self.animando = False


        self.tablero.setEstado(self.controller.puzzle.estadoInicial)

        

        

    def estadoInicial(self):
        print("hola")

    def estadoFinal(self):
        self.controller.puzzle.estadoFinal

    def botonIniciar(self):
        textsurface = self.myfont.render("Fuego", False, (255, 255, 255))
        self.screen.blit(textsurface,(120,370))
        pygame.draw.rect(self.screen, (0, 100, 255), (100, 350, 100, 50), 1)
                
    
    def eventos(self):
        if(self.cursorPositionDetector):
            pos = pygame.mouse.get_pos()
            print(pos)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.cursorPositionDetector = True
            if event.type == pygame.MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()
                #evento boton iniciar
                if(x>100 and x<200 and y>350 and y<400):
                    self.inicial = False
                    self.animando = True
                    self.self.camino = self.controller.puzzle.bfs()
                self.cursorPositionDetector = False
            if event.type == pygame.QUIT:
                self.running = False

    def cambiaEstados(self, camino):
        print(camino)
        for i in range(0, len(camino)):
            if(i<len(camino)-1):
                self.animar(camino[i], camino[i+1])
                i+=1
        self.animando = False
    
    def animar(self, estado1, estado2):

        i1,j1 = np.where(estado1 == 0)
        i2,j2 = np.where(estado2 == 0)


        if (i2>i1):
            print("mover 0 abajo")#restar y
            self.tablero.piezas[int(i1),int(j1)].moverAbajo()
            self.tablero.setEstado(estado2)
            time.sleep(1)

        if (i2<i1):
            print("mover 0 arriba")#sumar y
            self.tablero.piezas[int(i1),int(j1)].moverArriba()
            self.tablero.setEstado(estado2)
            time.sleep(1)

        if (j2>j1):
            print("mover 0 a la derecha")# restar x
            self.tablero.piezas[int(i1),int(j1)].moverDerecha()
            self.tablero.setEstado(estado2)
            time.sleep(1)

        if (j2<j1):
            print("mover 0 a la izquierda")
            self.tablero.piezas[int(i1),int(j1)].moverIzquierda()
            self.tablero.setEstado(estado2)
            time.sleep(1)
        
        
            

    def runDisplay(self):
        self.running = True
        while self.running:

            # code here

            self.screen.fill((25, 25, 25)) #Limpiamos pantalla

            self.botonIniciar()


            self.tablero.dibujar()
            


            self.eventos()

            
            pygame.display.flip()

            time.sleep(0.01)
        pygame.quit()
