import random as rnd
from Medidas import *
import math

def Vector_Exponenciales(beta, B):
    s0 = -1
    vec_exp = np.zeros((2,5))
    for i in range (2):
        for j in range (5):
            vec_exp[i][j] = math.exp(-2 * beta * s0 * ((j-2)*2 + B) )
        s0 = -s0
    return vec_exp

def mover(x, y, red, N, vec_exp):  # Función que decide si cambiar o no el spin red[x][y]
    rnum = rnd.random()
    ssuma = SpinSuma(x, y, red, N)
    prob_mover = vec_exp[int((red[x][y]+1)/2), int(ssuma/2+2)]

    if rnum <= prob_mover:
        return True
    else:
        return False


def Metropolis(red, N, vec_exp):  # Escoge un elemento de la red aleatorio, evalúa la función mover, si es True realiza el cambio y calcula la variación de la energía

    RND_x = rnd.randint(0, N-1)
    RND_y = rnd.randint(0, N-1)

    if mover(RND_x, RND_y, red, N, vec_exp) == True:
        red[RND_x][RND_y] = -red[RND_x][RND_y]
