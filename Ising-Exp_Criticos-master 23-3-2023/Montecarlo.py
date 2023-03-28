import random as rnd
import math
import numpy as np
from Medidas import *

def red_random(N):  # Función que crea la red cuadrada

    # Crea una red (matriz) de NxN elementos con valores -1 o +1

    red = np.random.choice([-1, -1], size=(N, N))   # Elige un número aleatorio entre los que estén entre corchetes
    return red



def mover(x, y, red, N, B, beta, vec_exp):  # Función que decide si cambiar o no el spin red[x][y]
    rnum = rnd.random()
    ssuma = SpinSuma(x, y, red, N)
    if red[x][y] == 1:
        prob_mover = vec_exp[int(ssuma/2 + 2)]
    elif red[x][y] == -1:
        prob_mover = vec_exp[int(ssuma/2 + 7)]
    if rnum <= prob_mover:
        return True
    else:
        return False


def Metropolis(red, N, B, beta, vec_exp, E_0):  # Escoge un elemento de la red aleatorio, evalúa la función mover, si es True realiza el cambio y calcula la variación de la energía

    RND_x = rnd.randint(0, N-1)
    RND_y = rnd.randint(0, N-1)

    if mover(RND_x, RND_y, red, N, B, beta, vec_exp) == True:
        red[RND_x][RND_y] = -1*red[RND_x][RND_y]
        List_E = energias(RND_x, RND_y, red, N, E_0, B)
        return List_E
    else:
        return None
    


    



