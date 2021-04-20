import pygame
import time

class Display:



    def __init__(self):
        pygame.init()
        self.width = 400
        self.height = 300
        self.screen = pygame.display.set_mode([self.height, self.width])
        self.screen.fill((25, 25, 25))
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.cursorPositionDetector = False
    
    def piece(self, number, x, y):
        textsurface = self.myfont.render(number, False, (255, 255, 255))
        self.screen.blit(textsurface,(x+45,y+45))
        pygame.draw.rect(self.screen, (0, 100, 255), (x, y, 100, 100), 1)



        

    def runDisplay(self):
        running = True
        while running:

            # code here

            self.screen.fill((25, 25, 25)) #Limpiamos pantalla


            self.piece("1",0,0)
            self.piece("2",100,0)
            self.piece("3",200,0)
            self.piece("4",0,100)
            self.piece("5",100,100)
            self.piece("6",200,100)
            self.piece("7",0,200)
            self.piece("8",100,200)
        

            if(self.cursorPositionDetector):
                pos = pygame.mouse.get_pos()
                print(pos)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.cursorPositionDetector = True
                if event.type == pygame.MOUSEBUTTONUP:
                    self.cursorPositionDetector = False
                if event.type == pygame.QUIT:
                    running = False

            
            pygame.display.flip()

            time.sleep(0.1)
        pygame.quit()
