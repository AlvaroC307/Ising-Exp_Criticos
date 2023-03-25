import matplotlib.pyplot as plt
import csv 
import numpy as np


def Representacion():

    csv_M = open('./Data/Magnetizacion.csv', 'r') # Abrir el fichero donde están los Inputs del programa
    Reader_M = csv.reader(csv_M) # Definir un objeto que lee el fichero
    csv_M2 = open('./Data/Magnetizacion2.csv', 'r') # Abrir el fichero donde están los Inputs del programa
    Reader_M2 = csv.reader(csv_M2) # Definir un objeto que lee el fichero

    M_vec=[]
    M2_vec=[]

    for row in Reader_M:
        M_vec.append(eval(row[0])) # Añadir cada elemento de cada fila del csv en una lista

    for row in Reader_M2:
        M2_vec.append(eval(row[0])) # Añadir cada elemento de cada fila del csv en una lista

    N_med=len(M_vec)

    csv_M.close() # Cerrar el fichero
    csv_M2.close() # Cerrar el fichero

    plt.plot( M_vec, "k", alpha = 0.3, lw = 3)
    plt.savefig('./Graphics/M_plot.png', bbox_inches = 'tight')
    plt.close()
    plt.plot( M2_vec, "k", alpha = 0.3, lw = 3)
    plt.savefig('./Graphics/M2_plot.png', bbox_inches = 'tight')
    plt.close()
