import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

A = np.matrix([[0,1,2],[3,4,5],[6,7,8]])
B = np.matrix([[1,0,2],[3,4,5],[6,7,8]])

fig = plt.figure()


plt.imshow(A)

for i in range(0,3):
    for j in range(0,3):
        if A[i,j] != 0:
            plt.text(j, i, A[i,j], size=20, va="center", ha="center", multialignment="left")


def animate(x):
    if(x==1):
        plt.cla()
        plt.imshow(B)
        for i in range(0,3):
            for j in range(0,3):
                if B[i,j] != 0:
                    plt.text(j, i, B[i,j], size=20, va="center", ha="center", multialignment="left")

    
    

ani = animation.FuncAnimation(fig, animate, frames=100, interval=500)

plt.show()


