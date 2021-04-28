import numpy as np

class Puzzle:
    def __init__(self):
        self.estadoInicial = np.matrix([[0,1,2],[3,4,5],[6,7,8]])
        self.estadoFinal = np.matrix([[3,1,2],[4,0,5],[6,7,8]])


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

        bandera = True

        for visitado in visitados:
            if(vecino==visitado).all():
                return False
        return bandera


    def bfs(self):

        visitados = []
        cola = []
        

        fin = False

        visitados.append(self.estadoInicial.copy())
        cola.append(self.estadoInicial.copy())

        print(self.estadoInicial)

        while cola and not fin:
            estado = cola.pop(0)
            for neighbour in self.operadores(estado).copy():
                if self.noEstaEnVisitados(neighbour, visitados):
                    print(neighbour)
                    visitados.append(neighbour)
                    cola.append(neighbour)
                    if(neighbour==self.estadoFinal).all():
                        fin = True
                        break
                        #print("ALERTA ROJAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaa")
        
        