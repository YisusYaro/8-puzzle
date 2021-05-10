import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk

class Animador:
    
    def __init__(self, controller):
        self.controller = controller
        self.fig = plt.figure()
        plt.gca().axes.get_xaxis().set_visible(False)
        plt.gca().axes.get_yaxis().set_visible(False)

        root = Tk.Tk()

        label = Tk.Label(root,text="8-puzzle").grid(column=0, row=0)


        Tk.Button(root, text="BFS", command = self.setCaminoBFS).grid(column=0, row=2)

        Tk.Button(root, text="A*", command = self.setCaminoAestrella ).grid(column=2, row=2 )

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

        #Tk.Button(root, text="A*", command = self.setCaminoAestrella ).grid(column=2, row=2)

        Tk.mainloop()

        #plt.show()


