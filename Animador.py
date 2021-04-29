import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Animador:
    
    def animar(self, camino):

        fig = plt.figure()
        plt.gca().axes.get_xaxis().set_visible(False)
        plt.gca().axes.get_yaxis().set_visible(False)

        def animate(x):

            plt.cla()
            plt.imshow(camino[x])
            if(x==0):
                plt.title("Estado Inicial")
            if(x==(len(camino)-1)):
                plt.title("Estado Final")
            for i in range(0,3):
                for j in range(0,3):
                    if camino[x][i,j] != 0:
                        plt.text(j, i, camino[x][i,j], size=20, va="center", ha="center", multialignment="left")


        ani = animation.FuncAnimation(fig, animate, frames=len(camino), interval=700, repeat=False)

        plt.show()


