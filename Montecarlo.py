import random as rnd
import matplotlib.pyplot as plt
import math
from Medidas import *
import numpy as np

def red_random(N):

    # Crea una red (matriz) de NxN elementos con valores -1 o +1

    red = np.random.choice([-1, +1], size=(N, N))
    return red


def Metropolis(red, N, J, B, beta):

    RND_x = rnd.randint(0, N-1)
    RND_y = rnd.randint(0, N-1)

    if mover(RND_x, RND_y, red, N, J, B, beta):
        red[RND_x][RND_y] = -1*red[RND_x][RND_y]


def mover(x, y, red, N, J, B, beta):
    if Delta_E(x, y, red, N, J, B) <= 0:
        mover = True
    else:
        rnum = rnd.random()
        if rnum <= math.exp(-beta*Delta_E(x, y, red, N, J, B)):
            mover = True
        else:
            mover = False

    return mover
