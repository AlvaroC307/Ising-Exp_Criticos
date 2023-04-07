from Medidas import *
import random as rnd
from numba import jit

@jit(nopython=True)
def Vector_Exponenciales(beta, B):
    s0 = np.array([-1, 1])
    j = np.arange(5)
    vec_exp = np.exp(-2 * beta * np.outer(s0, (j-2)*2 + B))
    # np.outer(a,b) hace el producto exterior de dos vectores que es una matriz c tal que:
    # c_{ij} = a_i*b_j (No me acordaba de lo que era el producto exterior)
    return vec_exp

@jit(nopython=True)
def mover(x, y, red, N, vec_exp):  # Función que decide si cambiar o no el spin red[x][y]
    rnum = rnd.random()
    ssuma = SpinSuma(x, y, red, N)
    prob_mover = vec_exp[int((red[x][y]+1)/2), int(ssuma/2+2)]

    if rnum <= prob_mover:
        return True
    else:
        return False

@jit(nopython=True)
def Metropolis(red, N, vec_exp):  # Escoge un elemento de la red aleatorio, evalúa la función mover, si es True realiza el cambio y calcula la variación de la energía

    RND_x = rnd.randint(0, N-1)
    RND_y = rnd.randint(0, N-1)

    if mover(RND_x, RND_y, red, N, vec_exp) == True:
        red[RND_x][RND_y] *= -1