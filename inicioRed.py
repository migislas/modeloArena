
import numpy as np
import sys


class inicializarMontana():
    def __init__(self, tamano:int,
                         alturaCritica:int) -> None:
        self.tamnoRed = tamano
        self.alturaCritica = alturaCritica


    def todoCero(self)->np.ndarray:
        return np.zeros((self.tamnoRed, self.tamnoRed))


    def aleatorio(self)->np.ndarray:
        return np.random.randint(self.alturaCritica,
                                 size=(self.tamnoRed, self.tamnoRed))


    def __call__(self,random:bool)->np.ndarray:
        if random:
            red = self.aleatorio()
        else:
            red = self.todoCero()
        return red
