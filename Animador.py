import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
from tkinter import simpledialog

class Animador:
    
    def __init__(self, controller):
        self.controller = controller

        root = Tk.Tk()

        fig, axarr = plt.subplots(1,2)

        fig.suptitle("8-Puzzle", fontsize=16)

        
        axarr[0].axes.get_xaxis().set_visible(False)
        axarr[0].axes.get_yaxis().set_visible(False)
        

        axarr[1].axes.get_xaxis().set_visible(False)
        axarr[1].axes.get_yaxis().set_visible(False)
        

        def animate(x):
            axarr[0].cla()
            axarr[1].cla()

            axarr[0].set_title('Estado Inicial')
            axarr[0].imshow(self.controller.puzzle.estadoInicial)
            for i in range(0,3):
                for j in range(0,3):
                    if self.controller.puzzle.estadoInicial[i,j] != 0:
                        axarr[0].text(j, i, self.controller.puzzle.estadoInicial[i,j], size=20, va="center", ha="center", multialignment="left")
            
            axarr[1].set_title('Estado Final')
            axarr[1].imshow(self.controller.puzzle.estadoFinal)
            for i in range(0,3):
                for j in range(0,3):
                    if self.controller.puzzle.estadoFinal[i,j] != 0:
                        axarr[1].text(j, i, self.controller.puzzle.estadoFinal[i,j], size=20, va="center", ha="center", multialignment="left")

        def getxy(event):    
            print(event.x, event.y)
            if(event.x>80 and event.x<305 and event.y>130 and event.y<355):
                USER_INP = simpledialog.askstring(title="Editar", prompt="Escribe el nuevo valor:")
                if(event.x>80 and event.x<155 and event.y>130 and event.y<205):
                    self.controller.puzzle.cambiarFichaEstadoInicial(0,0,USER_INP)
                if(event.x>155 and event.x<230 and event.y>130 and event.y<205):
                    self.controller.puzzle.cambiarFichaEstadoInicial(0,1,USER_INP)
                if(event.x>230 and event.x<305 and event.y>130 and event.y<205):
                    self.controller.puzzle.cambiarFichaEstadoInicial(0,2,USER_INP)
                
                if(event.x>80 and event.x<155 and event.y>205 and event.y<280):
                    self.controller.puzzle.cambiarFichaEstadoInicial(1,0,USER_INP)
                if(event.x>155 and event.x<230 and event.y>205 and event.y<280):
                    self.controller.puzzle.cambiarFichaEstadoInicial(1,1,USER_INP)
                if(event.x>230 and event.x<305 and event.y>205 and event.y<280):
                    self.controller.puzzle.cambiarFichaEstadoInicial(1,2,USER_INP)

                if(event.x>80 and event.x<155 and event.y>280 and event.y<355):
                    self.controller.puzzle.cambiarFichaEstadoInicial(2,0,USER_INP)
                if(event.x>155 and event.x<230 and event.y>280 and event.y<355):
                    self.controller.puzzle.cambiarFichaEstadoInicial(2,1,USER_INP)
                if(event.x>230 and event.x<305 and event.y>280 and event.y<355):
                    self.controller.puzzle.cambiarFichaEstadoInicial(2,2,USER_INP)

            if(event.x>350 and event.x<575 and event.y>130 and event.y<355):
                USER_INP = simpledialog.askstring(title="Editar", prompt="Escribe el nuevo valor:")
                if(event.x>350 and event.x<425 and event.y>130 and event.y<205):
                    self.controller.puzzle.cambiarFichaEstadoFinal(0,0,USER_INP)
                if(event.x>425 and event.x<500 and event.y>130 and event.y<205):
                    self.controller.puzzle.cambiarFichaEstadoFinal(0,1,USER_INP)
                if(event.x>500 and event.x<575 and event.y>130 and event.y<205):
                    self.controller.puzzle.cambiarFichaEstadoFinal(0,2,USER_INP)
            
                if(event.x>350 and event.x<425 and event.y>205 and event.y<280):
                    self.controller.puzzle.cambiarFichaEstadoFinal(1,0,USER_INP)
                if(event.x>425 and event.x<500 and event.y>205 and event.y<280):
                    self.controller.puzzle.cambiarFichaEstadoFinal(1,1,USER_INP)
                if(event.x>500 and event.x<575 and event.y>205 and event.y<280):
                    self.controller.puzzle.cambiarFichaEstadoFinal(1,2,USER_INP)
             
                if(event.x>350 and event.x<425 and event.y>280 and event.y<355):
                    self.controller.puzzle.cambiarFichaEstadoFinal(2,0,USER_INP)
                if(event.x>425 and event.x<500 and event.y>280 and event.y<355):
                    self.controller.puzzle.cambiarFichaEstadoFinal(2,1,USER_INP)
                if(event.x>500 and event.x<575 and event.y>280 and event.y<355):
                    self.controller.puzzle.cambiarFichaEstadoFinal(2,2,USER_INP)

                
        root.bind('<Button-1>', getxy)

        canvas = FigureCanvasTkAgg(fig, master=root)
        
        canvas.get_tk_widget().pack()

        Tk.Button(root, text="Resolver por BFS", command = self.setCaminoBFS).pack()

        Tk.Button(root, text="Resolver por A*", command = self.setCaminoAestrella ).pack()

        ani = animation.FuncAnimation(fig, animate, 1000, interval=100, repeat=True)

        Tk.mainloop()

    def setCaminoBFS(self):
        self.animar(self.controller.puzzle.bfs(),"BFS")

    def setCaminoAestrella(self):
        self.animar(self.controller.puzzle.aestrella(), "A*")
    
    def animar(self,camino,metodo):



        fig, axarr = plt.subplots(1,2)

        fig.suptitle(metodo, fontsize=16)

        axarr[1].imshow(self.controller.puzzle.estadoFinal)
        for i in range(0,3):
            for j in range(0,3):
                if self.controller.puzzle.estadoFinal[i,j] != 0:
                    axarr[1].text(j, i, self.controller.puzzle.estadoFinal[i,j], size=20, va="center", ha="center", multialignment="left")
        

        axarr[0].axes.get_xaxis().set_visible(False)
        axarr[0].axes.get_yaxis().set_visible(False)

        axarr[1].axes.get_xaxis().set_visible(False)
        axarr[1].axes.get_yaxis().set_visible(False)
        axarr[1].set_title('Estado Final')


        def animate(x):

            axarr[0].cla()
            axarr[0].imshow(camino[x])
            if(x==0):
                axarr[0].set_title("Estado Inicial")
            if(x==(len(camino)-1)):
                axarr[0].set_title("Estado Final")
            for i in range(0,3):
                for j in range(0,3):
                    if camino[x][i,j] != 0:
                        axarr[0].text(j, i, camino[x][i,j], size=20, va="center", ha="center", multialignment="left")
            


        root = Tk.Tk()


        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().grid(column=0,row=1)


        ani = animation.FuncAnimation(fig, animate, frames=len(camino), interval=700, repeat=False)

        Tk.mainloop()



