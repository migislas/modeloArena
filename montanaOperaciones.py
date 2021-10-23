import numpy as np
from typing import List
class operacionesMontana():


    def __init__(self,
                 tamno:int,
                 altura:int)->None:

        self.tamno = tamno
        self.mitad = (self.tamno)//2
        self.altura = altura
        print(self.mitad)


    def agregarGranosCentro(self,
                            montana:np.ndarray):
        montana[self.mitad, self.mitad] += 1


    def repartirGranosVecinos(self,
                              montana:np.ndarray,
                              punto:List):
        x = punto[0]
        y = punto[1]
        montana[x - 1, y] += 1
        montana[x + 1, y] += 1
        montana[x, y + 1] += 1
        montana[x, y - 1] += 1
        montana[x, y] -= self.altura
        return 1

    def repartirPuntos(self,
                       montana:np.ndarray,
                       vecinos:int)->int:
        x, y = np.where(montana >= self.altura)
        listaPuntos = [[x[valor], y[valor]]
                           for valor in range(len(x))]
        if listaPuntos:
            listaSitios = list(map(lambda p:
                    self.repartirGranosVecinos(montana, p),
                    listaPuntos)
                    )
            vecinos += sum(listaSitios)
            montana[0] = montana[-1] = 0
            montana[:, 0] = montana[:, -1] = 0
            return self.repartirPuntos(montana, vecinos)
        else:
            return vecinos


    def __call__(self,
                 montana:np.ndarray,
                 numeroIteraciones:int)->np.ndarray:

        for i in range(numeroIteraciones):
            vecinos = 0
            self.agregarGranosCentro(montana)
            vecinos = self.repartirPuntos(montana, vecinos)
        return montana
