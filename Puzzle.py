import numpy as np

class Puzzle:
    def __init__(self, controller):
        self.controller = controller
        #self.estadoInicial = np.matrix([[0,1,2],[3,4,5],[6,7,8]])
        #self.estadoFinal = np.matrix([[3,1,2],[4,0,5],[6,7,8]])
        #self.estadoInicial = np.matrix([[0,2,3],[1,4,5],[8,7,6]])
        #self.estadoFinal = np.matrix([[1,2,3],[8,0,4],[7,6,5]])
        self.estadoInicial = np.matrix([[4,8,1],[3,0,2],[7,6,5]])
        self.estadoFinal = np.matrix([[1,2,3],[8,0,4],[7,6,5]])

    def cambiarFichaEstadoInicial(self,ni,nj,USER_INP):
        if(USER_INP=='' or USER_INP==' '):
            USER_INP='0'
        if(USER_INP=='0' or USER_INP=='1' or USER_INP=='2' or USER_INP=='3' or USER_INP=='4' or USER_INP=='5' or USER_INP=='6' or USER_INP=='7' or USER_INP=='8'):
            vi,vj = np.where(self.estadoInicial == int(USER_INP))
            cambio = self.estadoInicial[ni,nj]
            self.estadoInicial[ni,nj] = USER_INP
            self.estadoInicial[vi,vj] = cambio

    def cambiarFichaEstadoFinal(self,ni,nj,USER_INP):
        if(USER_INP=='' or USER_INP==' '):
            USER_INP='0'
        if(USER_INP=='0' or USER_INP=='1' or USER_INP=='2' or USER_INP=='3' or USER_INP=='4' or USER_INP=='5' or USER_INP=='6' or USER_INP=='7' or USER_INP=='8'):
            vi,vj = np.where(self.estadoFinal == int(USER_INP))
            cambio = self.estadoFinal[ni,nj]
            self.estadoFinal[ni,nj] = USER_INP
            self.estadoFinal[vi,vj] = cambio
         

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

    def manhattan(self, estado):
        m=0
        for i in range(1,9):
            ei,ej = np.where(estado == i)
            fi,fj = np.where(self.estadoFinal == i)
            m = m + abs(ei-fi)
            m = m + abs(ej-fj)
        return int(m)

    def malColocadas(self, estado):
        m=0
        for i in range(1,9):
            ei,ej = np.where(estado == i)
            fi,fj = np.where(self.estadoFinal == i)
            if((ei!=fi) or (ej!=fj)):
                m = m +1 
        return int(m)

    def aestrella(self):
        peso = 0
        ultimoPeso = 0
        visitados = []
        visitados.append(self.estadoInicial)
        while True:
            auxiliar = True
            if(visitados[-1]==self.estadoFinal).all():
                break
            for vecinoOperador in self.operadores(visitados[-1]):
                if self.noEstaEnVisitados(vecinoOperador, visitados):
                    if(auxiliar):
                        visitados.append(vecinoOperador)
                        auxiliar=False
                        ultimoPeso = self.malColocadas(vecinoOperador)
                        peso = peso + self.malColocadas(vecinoOperador)
                    else:
                        if( (peso + self.malColocadas(vecinoOperador) + self.manhattan(vecinoOperador)) < ( peso + self.malColocadas(vecinoOperador) + self.manhattan(visitados[-1])) ):
                            visitados.pop()
                            visitados.append(vecinoOperador)
                            peso = peso - self.malColocadas(visitados[-1])
                            peso = peso + self.malColocadas(vecinoOperador)
                            ultimoPeso = self.malColocadas(vecinoOperador)
        return visitados
                

    def bfs(self):

        visitados = []
        cola = []
        
        padres = {}

        fin = False

        visitados.append(self.estadoInicial.copy())
        cola.append(self.estadoInicial.copy())

        while cola and not fin:
            estado = cola.pop(0)
            for vecinoOperador in self.operadores(estado).copy():
                if self.noEstaEnVisitados(vecinoOperador, visitados):
                    visitados.append(vecinoOperador)
                    cola.append(vecinoOperador)
                    padres[vecinoOperador.tobytes()] = estado.tobytes()
                    if(vecinoOperador==self.estadoFinal).all():
                        fin = True
                        break
                        
        return self.obtenerCamino(padres)
        
        