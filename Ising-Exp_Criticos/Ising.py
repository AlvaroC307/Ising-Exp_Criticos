import numpy as np
from concurrent.futures import *
import csv
import time

from Plot import *
from Medidas import *
from Montecarlo import *
from Representacion import *


def main():

    start=time.time()
    

    csv_Input = open('./Input/Input.csv', 'r') # Abrir el fichero donde están los Inputs del programa
    Reader_Input = csv.reader(csv_Input) # Definir un objeto que lee el fichero

    list_Input = [] 
    for row in Reader_Input:
        list_Input.append(row[1]) # Añadir cada segundo elemento de cada fila del csv en una lista
    csv_Input.close() # Cerrar el fichero

    N = eval(list_Input[0]) # Número de puntos de la red
    N_mover=eval(list_Input[1])
    N_med=eval(list_Input[2])
    N_calentar=eval(list_Input[3])
    B = eval(list_Input[4]) # Campo externo (B=\mu H)
    beta = eval(list_Input[5]) # Inversa de la temperatura, hemos tomado k=1

    s0 = 1
    vec_exp = []
    for i in range (2):
        for j in range (5):
            vec_exp.append(math.exp(-2 * beta * ( s0*((j-2)*2) + B * s0)))
        s0 = s0*(-1)


    # E_inicial=E_0(red, N, B)

    M_file=open('./Data/Magnetizacion.csv', "w", newline="")
    M_csv=csv.writer(M_file)
    M2_file=open('./Data/Magnetizacion2.csv', "w", newline="")
    M2_csv=csv.writer(M2_file)


    red = red_random(N)
    pintar(red, N, "inicial")

    medida = magnetizaciones(red, N)
    M = medida[0]
    M2 = medida[1]

    M_csv.writerow([M])
    M2_csv.writerow([M2])


    for j in range(N_calentar):
        Metropolis(red, N, B, beta, vec_exp)
    

    for i in range(N_med):
        for j in range(N_mover):
            Metropolis(red, N, B, beta, vec_exp)
    
        #nombre="medida"
        #pintar(red, N, nombre)
        medida = magnetizaciones(red, N)
        M = medida[0]
        M2 = medida[1]

        M_csv.writerow([M])
        M2_csv.writerow([M2])
        #if (100*i)/N_med % 
        print("Progreso", (100*i)/N_med, "%")

    M_file.close()
    M2_file.close()

    pintar(red, N, "final")

    Representacion()

    promedios(N, beta)

    print(time.time()-start, "segundos")

    

if __name__ == '__main__':
    main()

