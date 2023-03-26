import random as rnd
import math
from Medidas import *
import numpy as np

def red_random(N):  # Función que crea la red cuadrada

    # Crea una red (matriz) de NxN elementos con valores -1 o +1

    red = np.random.choice([+1, +1], size=(N, N))   # Elige un número aleatorio entre los que estén entre corchetes
    return red

def SpinSuma(i, j, red, N): # Función que calcula la suma de los spines vecinos al red[i][j]
    if i == (N-1):
        if j == (N-1):
            ssuma = red[0][j]+red[i-1][j]+red[i][0]+red[i][j-1]
        else:
            ssuma = red[0][j]+red[i-1][j]+red[i][j+1]+red[i][j-1]
   
    else:
        if j == (N-1):
            ssuma = red[i+1][j]+red[i-1][j]+red[i][0]+red[i][j-1]
        else:
            ssuma = red[i+1][j]+red[i-1][j]+red[i][j+1]+red[i][j-1]
    return ssuma

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

def energias(i, j, red, N, E_0, B): # Calcula la variación de energía al cambiar el spin [i][j]

    Delta_E = 2 * red[i][j] * (SpinSuma(i, j, red, N) + B)  # Ecuación 3.10 del Newman

    E = (E_0 + Delta_E)/(N**2)
    E2 = E**2
    return [E, E2]

def Metropolis(red, N, B, beta, vec_exp, E_0):  # Escoge un elemento de la red aleatorio, evalúa la función mover, si es True realiza el cambio y calcula la variación de la energía

    RND_x = rnd.randint(0, N-1)
    RND_y = rnd.randint(0, N-1)

    if mover(RND_x, RND_y, red, N, B, beta, vec_exp) == True:
        red[RND_x][RND_y] = -1*red[RND_x][RND_y]
        List_E = energias(RND_x, RND_y, red, N, E_0, B)
        return List_E
    else:
        return None
    


    



