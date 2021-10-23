import sys

import numpy as np
import matplotlib.pyplot as plt

from grafica import  Grafica
from inicioRed import inicializarMontana
from montanaOperaciones import operacionesMontana


sys.setrecursionlimit(5000)

def main():

    gr = Grafica()
    l = inicializarMontana(200,4)(False)
    print(l)
    op = operacionesMontana(200,4)
    montana = op(l,100)
    gr.graficaMontana(montana, f'final.png')


if __name__ == '__main__':
    main()
