import csv 
import numpy as np

""" def Delta_E(i, j, red, N, B): # Cálculo la variación de la energía al cambiar un spin 

    if i == (N-1):
        if j == (N-1):
            Delta_E = - red[i][j]*(red[0][j]+red[i-1][j]+red[i][0]+red[i][j-1]) -B*red[i][j]
        else:
            Delta_E = - red[i][j]*(red[0][j]+red[i-1][j]+red[i][j+1]+red[i][j-1]) -B*red[i][j]
   
    else:
        if j == (N-1):
            Delta_E = - red[i][j]*(red[i+1][j]+red[i-1][j]+red[i][0]+red[i][j-1]) -B*red[i][j]
        else:
            Delta_E = - red[i][j]*(red[i+1][j]+red[i-1][j]+red[i][j+1]+red[i][j-1]) -B*red[i][j]

    return (-2*Delta_E) """


def E_0(red, N, B):#Calculo de la energía inicial

    E_0=0

    for i in range (N):
        for j in range (N):

            if i == N-1:
                if j == N-1:
                    E_0 += - red[i][j]*(red[0][j]+red[i-1][j]+red[i][0]+red[i][j-1]) -B*red[i][j]
                else:
                    E_0 += - red[i][j]*(red[0][j]+red[i-1][j]+red[i][j+1]+red[i][j-1]) -B*red[i][j]
   
            else:
                if j == N-1:
                    E_0 += - red[i][j]*(red[i+1][j]+red[i-1][j]+red[i][0]+red[i][j-1]) -B*red[i][j]
                else:
                    E_0 += - red[i][j]*(red[i+1][j]+red[i-1][j]+red[i][j+1]+red[i][j-1]) -B*red[i][j]

    return E_0


def magnetizaciones(red, N): # Magnetizacion
    m = 0
    m2 = 0
    for i in range (N):
        for j in range(N):
            m += red[i][j]/N**2
    m2 = m**2
    return [m, m2]

def promedios(N, beta):
    
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

    prom_m = np.sum(M_vec)/N_med
    prom_m2 =np.sum(M2_vec)/N_med
    sus = beta * N**2 * (prom_m2 - prom_m**2)
    
    print("Buenas tardes, usuario.")
    print("El promedio de la magnetización o prom es ", prom_m, ".")
    print("El promedio de la magnetización al cuadrado o promm es ", prom_m2, ".")
    print("Kinda sus= ", sus)
    print("Muchas gracias por utilizar nuestro programa. Un cordial saludo.")
    print("<3")
    print(":D")
    print("8===D")

    return [prom_m, prom_m2, sus]





            
