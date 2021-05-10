import numpy as np
import time

class Puzzle:
    def __init__(self, controller):
        self.controller = controller
        #self.estadoInicial = np.matrix([[0,1,2],[3,4,5],[6,7,8]])
        #self.estadoFinal = np.matrix([[3,1,2],[4,0,5],[6,7,8]])
        self.estadoInicial = np.matrix([[0,2,3],[1,4,5],[8,7,6]])
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

    def manhatan(self, estado):
        m=0
        for i in range(1,9):
            ei,ej = np.where(estado == i)
            fi,fj = np.where(self.estadoFinal == i)
            m = m + abs(ei-fi)
            m = m + abs(ej-fj)
        return m

    def malColocadas(self, estado):
        m=0
        for i in range(1,9):
            ei,ej = np.where(estado == i)
            fi,fj = np.where(self.estadoFinal == i)
            if((ei!=fi) or (ej!=fj)):
                m = m +1 
        return m

    def aestrella(self):
        visitados = []
        estado = self.estadoInicial
        visitados.append(estado)
        camino = []
        numeroVisitados = 0
        peso = 0
        bandera = True
        while True and bandera:
            camino.append(visitados[len(visitados)-1])
            #print("operador")
            #print(visitados[len(visitados)-1])

            if(np.array_equal(visitados[len(visitados)-1],self.estadoFinal)):
                break
            i=0
            for vecinoOperador in self.operadores(visitados[len(visitados)-1]).copy():
                if self.noEstaEnVisitados(vecinoOperador, visitados):
                    if(i==0):
                        visitados.append(vecinoOperador)
                        peso=peso+self.malColocadas(vecinoOperador)
                    else:
                        if( (peso + self.malColocadas(vecinoOperador)+ self.manhatan(vecinoOperador)) < ( peso + self.malColocadas(visitados[len(visitados)-1])+ self.manhatan(visitados[len(visitados)-1]))):
                            visitados.pop(len(visitados)-1)
                            visitados.append(vecinoOperador)
                            peso=peso+self.malColocadas(vecinoOperador)
                            
                    
                i = i+1
        return camino
                

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
        
        