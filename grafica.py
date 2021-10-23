import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

class Grafica():
    def graficaMontana(self,
            montana:np.ndarray,
            nombre="inicial.png")->None:
        cmap =ListedColormap(['white', 'orange', 'red', 'black'])
        plt.imshow(montana, cmap=cmap)
        plt.axis('off')
        plt.savefig(nombre, dpi=500)
