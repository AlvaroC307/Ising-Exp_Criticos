import numpy as np
from concurrent.futures import *
import csv

from Plot import *
from Medidas import *
from Montecarlo import *


def main():
    

    csv_Input = open('./Input/Input.csv', 'r') # Abrir el fichero donde están los Inputs del programa
    Reader_Input = csv.reader(csv_Input) # Definir un objeto que lee el fichero

    list_Input = [] 
    for row in Reader_Input:
        list_Input.append(row[1]) # Añadir cada segundo elemento de cada fila del csv en una lista
    csv_Input.close() # Cerrar el fichero

    N = eval(list_Input[0]) # Número de puntos de la red
    N_mover=eval(list_Input[1])
    N_med=eval(list_Input[2])
    J = eval(list_Input[3]) # Energía de interacción entre spines
    B = eval(list_Input[4]) # Campo externo (B=\mu H)
    beta = eval(list_Input[5]) # Inversa de la temperatura, hemos tomado k=1

    red = red_random(N)
    pintar(red, N, "inicial")

    E_inicial=E_0(red, N, J, B)

    for i in range(N_med):
        for j in range(N_mover):
            Metropolis(red, N, J, B, beta)
    
        nombre="medida " + str(i)
        pintar(red, N, nombre)

    

    

if __name__ == '__main__':
    main()

