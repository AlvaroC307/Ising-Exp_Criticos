""" import numpy as np
import matplotlib.pyplot as plt

def red_random(N):

    # Crea una red (matriz) de NxN elementos con valores -1 o +1

    red = np.random.choice([-1, +1], size = (N, N))
    return red

def Energia(i, j, red, N, J, B, E): # Función que actualiza la energía

    if i == N:
        if j == N:
            E = E - J*red[i][j]*(red[0][j]+red[i-1][j]+red[i][0]+red[i][j-1]) -B*red[i][j]
        elif j == 0:
            E = E - J*red[i][j]*(red[0][j]+red[i-1][j]+red[i][j+1]+red[i][N]) -B*red[i][j]
        else:
            E = E - J*red[i][j]*(red[0][j]+red[i-1][j]+red[i][j+1]+red[i][j-1]) -B*red[i][j]
   
    elif i == 0:
        if j == N:
            E = E - J*red[i][j]*(red[i+1][j]+red[N][j]+red[i][0]+red[i][j-1]) -B*red[i][j]
        elif j == 0:
            E = E - J*red[i][j]*(red[i+1][j]+red[N][j]+red[i][j+1]+red[i][N]) -B*red[i][j]
        else:
            E = E - J*red[i][j]*(red[i+1][j]+red[N][j]+red[i][j+1]+red[i][j-1]) -B*red[i][j]

    else:
        if j == N:
            E = E - J*red[i][j]*(red[i+1][j]+red[i-1][j]+red[i][0]+red[i][j-1]) -B*red[i][j]
        elif j == 0:
            E = E - J*red[i][j]*(red[i+1][j]+red[i-1][j]+red[i][j+1]+red[i][N]) -B*red[i][j]
        else:
            E = E - J*red[i][j]*(red[i+1][j]+red[i-1][j]+red[i][j+1]+red[i][j-1]) -B*red[i][j]
  
    return E """