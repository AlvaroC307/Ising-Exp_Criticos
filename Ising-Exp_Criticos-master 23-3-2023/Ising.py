import numpy as np
from concurrent.futures import *
import csv
import time
from tqdm import tqdm

from Medidas import *
from Montecarlo import *
from Representacion import *


def main():

    start=time.time()   # Comienza a contar el tiempo de ejecución
    

    csv_Input = open('./Input/Input.csv', 'r') # Abrir el fichero donde están los Inputs del programa
    Reader_Input = csv.reader(csv_Input) # Definir un objeto que lee el fichero

    list_Input = [] # Vector donde guardaremos los inputs
    for row in Reader_Input:
        list_Input.append(row[1]) # Añadir cada segundo elemento de cada fila del csv en una lista
    csv_Input.close() # Cerrar el fichero

    N = eval(list_Input[0]) # Número de puntos de la red
    N_mover=eval(list_Input[1]) # Número de veces que movemos antes de medir
    N_med=eval(list_Input[2])   # Número de veces que medimos
    N_calentar=eval(list_Input[3])  # Número de movimientos de calentamiento
    B = eval(list_Input[4]) # Campo externo (B=\mu H)
    beta = eval(list_Input[5]) # Inversa de la temperatura, hemos tomado k=1
    pintar_intermedios = eval(list_Input[6])    # Variable que nos dice si pintar los pasos intermedios o no


    # Creamos un vector, llamada vec_exp, que guarda los posibles valores de e^(\beta * H)
    s0 = 1
    vec_exp = []
    for i in range (2):
        for j in range (5):
            vec_exp.append(math.exp(-2 * beta * ( s0*((j-2)*2) + B * s0)))
        s0 = s0*(-1)
    
    # Abrimos los archivos donde guardaremos las medidas
    M_file=open('./Data/Magnetizacion.csv', "w", newline="")
    M_csv=csv.writer(M_file)
    M2_file=open('./Data/Magnetizacion2.csv', "w", newline="")
    M2_csv=csv.writer(M2_file)
    e_file=open('./Data/energia_promedio.csv', "w", newline="")
    e_csv=csv.writer(e_file)
    e2_file=open('./Data/energia2_promedio.csv', "w", newline="")
    e2_csv=csv.writer(e2_file)
    E_file=open('./Data/Energia.csv', "w", newline="")
    E_csv=csv.writer(E_file)

    #   Creamos la red inicial y la pintamos
    red = red_random(N)
    pintar(red, N, "inicial")

    #   Hallamos la magnetización y magnetización al cuadrado inciales y las guardamos en los respectivos ficheros
    medida = magnetizaciones(red, N)
    M = medida[0]
    M2 = medida[1]

    #   Cerramos los archivos 
    M_csv.writerow([M])
    M2_csv.writerow([M2])

    #   Inicializamos el valor de la energía
    e_i = 0
    e2 = 0
    E_i = 0

    print("Calentamiento: ")
    #     Hacemos movimientos de calentamiento
    for j in tqdm(range(N_calentar)):
        Metropolis(red, N, B, beta, vec_exp, e_i)

    #   Caculamos la energía inicial
    E_i=E_0(red, N, B)
    E_csv.writerow([E_i])


    print("Montecarlo: ")
    #   Ejecutamos el algortimo de metropolis. Movemos N_mover entre cada medida. Medimo N_med veces
    for i in tqdm(range(N_med)):
        for j in range(N_mover):
            Lista = Metropolis(red, N, B, beta, vec_exp, E_i)
            if Lista != None:
                e_i = Lista[0]
                e2 = Lista[1]
                E_i = Lista[2]
                

        # Cada vez que midamos pintamos el estado de la red, si así lo hemos decidido antes
        if pintar_intermedios == True:
            nombre="Pasos_intermedios"
            pintar(red, N, nombre)

        #   Ejecutamos la función de magnetizaciones, que nos da un valor de la magnetización o otro de la magnetización al cuadrado.
        #   Guardamos las salidas y luego las escribimos en un archivo
        medida = magnetizaciones(red, N)    
        M = medida[0]
        M2 = medida[1]
        M_csv.writerow([M])
        M2_csv.writerow([M2])
        e_csv.writerow([e_i])
        e2_csv.writerow([e2])
        E_csv.writerow([E_i])
     
 
        # print("Progreso", (100*i)/N_med, "%", end = "\r")

    #   Cerramos los archivos en lo que hemos escrito
    M_file.close()
    M2_file.close()
    e_file.close()
    e2_file.close()
    E_file.close()

    #   Pintamos la red al final del proceso
    pintar(red, N, "final")
    #   Generamos los gráficos 
    Representacion()
    #   Llamamos a la función que calcula los promedios de las cantidades necesarias
    promedios(N, beta)

    print("------------------------------------------------------------------")
    print("Duración de la simulación: ", time.time()-start, "segundos")
    print("------------------------------------------------------------------")
    print("MAGNETO")
    print("""⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣶⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⡿⢛⣿⣿⣿⣿⣿⣿⣿⣿⡛⢿⣦⡀⠀⠀⠀
⠀⠀⣰⣿⡟⠀⠀⣿⣿⠿⠛⠛⠿⣿⣿⠀⠀⢻⣿⣆⠀⠀
⠀⣰⣿⣿⣿⡀⠀⠹⣿⠀⠀⠀⠀⣿⠏⠀⢀⣿⣿⣿⣧⠀
⢠⣿⣿⣿⣿⣿⣦⣤⣘⣇⠀⠀⣸⣁⣤⣴⣿⣿⣿⣿⣿⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⠟⠛⠛⠻⣿⣿⣿⣿⠟⡛⠛⠻⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣇⠀⠚⠛⠓⠈⠛⠛⠁⠚⠛⠓⠀⣹⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣷⣤⣤⣄⠀⠀⠀⠀⣠⣤⣤⣾⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠘⠻⠿⣿⣿⣿⣿⣿⣿⠛⠛⠛⠛⣿⣿⣿⣿⣿⣿⠿⠟⠃
⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠉⠋⠉⠉⠀⠀⠀⠀⠀""")

    

if __name__ == '__main__':
    main()

