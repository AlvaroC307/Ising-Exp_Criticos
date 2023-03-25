import random as rnd
import math
from Medidas import *
import numpy as np

def red_random(N):

    # Crea una red (matriz) de NxN elementos con valores -1 o +1

    red = np.random.choice([+1, +1], size=(N, N))
    return red



def Metropolis(red, N, B, beta, vec_exp):

    RND_x = rnd.randint(0, N-1)
    RND_y = rnd.randint(0, N-1)

    if mover(RND_x, RND_y, red, N, B, beta, vec_exp) == True:
        red[RND_x][RND_y] = -1*red[RND_x][RND_y]

def SpinSuma(i, j, red, N):
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
    


def mover(x, y, red, N, B, beta, vec_exp):
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
