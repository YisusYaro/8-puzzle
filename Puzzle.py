import numpy as np

class Puzzle:
    def __init__(self, controller):
        self.controller = controller
        self.estadoInicial = np.matrix([[0,1,2],[3,4,5],[6,7,8]])
        self.estadoFinal = np.matrix([[3,1,2],[4,0,5],[6,7,8]])
        #self.estadoInicial = np.matrix([[0,2,3],[1,4,5],[8,7,6]])
        #self.estadoFinal = np.matrix([[1,2,3],[8,0,4],[7,6,5]])

    def obtenerCamino(self, padres):
        camino = []
        finDelCamino = False

        estado = self.estadoFinal.tobytes()

        while not finDelCamino:
            camino.append(np.frombuffer(estado, dtype=int).reshape(3, 3))
            estado = padres[estado]
            if(self.estadoInicial.tobytes()==estado):
                finDelCamino = True

        camino.append(np.frombuffer(self.estadoInicial, dtype=int).reshape(3, 3))

        return camino[::-1]


    def operadores(self, estado):

        operadores = []

        i,j = np.where(estado == 0)

        # Mover hueco arriba
        if(i > 0):
            operador = estado.copy()
            operador[i,j] , operador[i-1,j] = operador[i-1,j] , operador[i,j]
            operadores.append(operador)
        
        # Mover hueco derecha
        if(j < 2):
            operador = estado.copy()
            operador[i,j] , operador[i,j+1] = operador[i,j+1] , operador[i,j]
            operadores.append(operador)
        
        # Mover hueco izquierda
        if(j > 0):
            operador = estado.copy()
            operador[i,j] , operador[i,j-1] = operador[i,j-1] , operador[i,j]
            operadores.append(operador)
        
        # Mover hueco abajo
        if(i < 2):
            operador = estado.copy()
            operador[i,j] , operador[i+1,j] = operador[i+1,j] , operador[i,j]
            operadores.append(operador)

        return operadores

        
    def noEstaEnVisitados(self, vecino, visitados):
        for visitado in visitados:
            if(vecino==visitado).all():
                return False
        return True

    def bfs(self):

        visitados = []
        cola = []
        
        padres = {}

        fin = False

        visitados.append(self.estadoInicial.copy())
        cola.append(self.estadoInicial.copy())

        while cola and not fin:
            estado = cola.pop(0)
            for neighbour in self.operadores(estado).copy():
                if self.noEstaEnVisitados(neighbour, visitados):
                    #print(neighbour)
                    visitados.append(neighbour)
                    cola.append(neighbour)
                    padres[neighbour.tobytes()] = estado.tobytes()
                    if(neighbour==self.estadoFinal).all():
                        fin = True
                        #print("ALERTA ROJAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaa")
                        break
                        
        return self.obtenerCamino(padres)
        
        