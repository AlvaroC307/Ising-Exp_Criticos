import numpy as np
from numba import jit

@jit(nopython=True)
def SpinSuma(i, j, red, N): # Función que calcula la suma de los spines vecinos al red[i][j]
    
    ssuma = red[(i+1)%N][j]+red[i-1][j]+red[i][(j+1)%N]+red[i][j-1]

    return ssuma

def energias(red, B):

    shifted_down = np.roll(red, 1, axis=0)
    shifted_right = np.roll(red, 1, axis=1)
    E = np.sum(-red * (shifted_down + shifted_right + B))

    return E

@jit(nopython=True)
def magnetizaciones(red): # Magnetizacion

    M=np.sum(red)
    m=M/red.size

    return m

@jit(nopython=True)
def promedios(N, beta, data):

    # Extract columns from data
    M_vec = data[:, 0]
    Mabs_vec = data[:, 1]
    M2_vec = data[:, 2]
    E_vec = data[:, 3]
    E2_vec = data[:, 4]
    
    # Calculate means
    prom_m = np.mean(M_vec)
    prom_mabs = np.mean(Mabs_vec)
    prom_m2 = np.mean(M2_vec)
    sus = beta * N**2 * (prom_m2 - prom_m**2)
    prom_E = np.mean(E_vec)
    prom_E2 = np.mean(E2_vec)
    cap_cal = (beta / N)**2 * (prom_E2 - prom_E**2)
    
    """ print("------------------------------------------------------------------")
    print("Promedio de la magnetización: ", prom_m, ".")
    print("Promedio de la magnetización absoluta: ", prom_mabs, ".")
    print("Promedio de la magnetización al cuadrado ", prom_m2, ".")
    print("Susceptibilidad: ", sus)
    print("Promedio de la energía: ", prom_E, ".")
    print("Promedio de la energía al cuadrado ", prom_E2, ".")
    print("Capacidad calorífica: ", cap_cal)
    print("<3") """

    return [prom_m, prom_mabs, prom_m2, sus, prom_E, prom_E2, cap_cal]



    
