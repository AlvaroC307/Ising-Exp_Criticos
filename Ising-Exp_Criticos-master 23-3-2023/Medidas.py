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

def SpinSuma(i, j, red, N): # Función que calcula la suma de los spines vecinos al red[i][j]
    
    ssuma = red[(i+1)%N][j]+red[i-1][j]+red[i][(j+1)%N]+red[i][j-1]

    return ssuma


def E_0(red, N, B):#Calculo de la energía inicial

    E_0=0

    for i in range (N):
        for j in range (N):
            E_0 += - red[i][j]*(red[(i+1)%N][j]+red[i-1][j]+red[i][(j+1)%N]+red[i][j-1]) -B*red[i][j]      

    return E_0


def energias(i, j, red, N, E_0, B): # Calcula la variación de energía al cambiar el spin [i][j]

    Delta_E = 2 * red[i][j] * (SpinSuma(i, j, red, N) + B)  # Ecuación 3.10 del Newman

    E = E_0 + Delta_E
    e = E/(N**2)
    e2 = e**2
    lista = [e, e2, E]
    return lista

def magnetizaciones(red, N): # Magnetizacion
    m = 0
    m2 = 0
    M=0

    M=np.sum(red)
    m=M/N**2
    m2 = m**2
    return [m, m2]

def promedios(N, beta):
    
    csv_M = open('./Data/Magnetizacion.csv', 'r') # Abrir el fichero donde están los datos de la magnetización por spin
    Reader_M = csv.reader(csv_M) # Definir un objeto que lee el fichero
    csv_M2 = open('./Data/Magnetizacion2.csv', 'r') # Abrir el fichero donde están los datos de la magnetización por spin al cuadrado
    Reader_M2 = csv.reader(csv_M2) # Definir un objeto que lee el fichero
    csv_E = open('./Data/energia_promedio.csv', 'r') # Abrir el fichero donde están los datos de la energía
    Reader_E = csv.reader(csv_E) # Definir un objeto que lee el fichero
    csv_E2 = open('./Data/energia2_promedio.csv', 'r') # Abrir el fichero donde están los datos de la energía al cuadrado
    Reader_E2 = csv.reader(csv_E2) # Definir un objeto que lee el fichero

    #   Definimos los vectores donde guardaremos los datos de cada variable
    M_vec=[]
    M2_vec=[]
    E_vec=[]
    E2_vec=[]

    #   Leemos los ficheros y los metemos en los vectores
    for row in Reader_M:
        M_vec.append(eval(row[0])) # Añadir cada elemento de cada fila del csv en una lista

    for row in Reader_M2:
        M2_vec.append(eval(row[0])) # Añadir cada elemento de cada fila del csv en una lista

    for row in Reader_E:
        E_vec.append(eval(row[0])) # Añadir cada elemento de cada fila del csv en una lista

    for row in Reader_E2:
        E2_vec.append(eval(row[0])) # Añadir cada elemento de cada fila del csv en una lista

    #   Miramos las longitudes
    N_med=len(M_vec)
    N_mover=len(E_vec)

    #   Cerramos los ficheros
    csv_M.close() 
    csv_M2.close() 
    csv_E.close() 
    csv_E2.close() 

    #   Hallamos los promedios
    prom_m = np.sum(M_vec)/N_med
    prom_m2 =np.sum(M2_vec)/N_med
    sus = beta * N**2 * (prom_m2 - prom_m**2)

    prom_E = np.sum(E_vec)/N_mover
    prom_E2 =np.sum(E2_vec)/N_mover
    cap_cal = (beta / N)**2 * (prom_E2 - prom_E**2)
    
    print("------------------------------------------------------------------")
    # print("Buenas tardes, usuario.")
    print("Promedio de la magnetización: ", prom_m, ".")
    print("Promedio de la magnetización al cuadrado ", prom_m2, ".")
    print("Susceptibilidad: ", sus)
    print("Promedio de la energía: ", prom_E, ".")
    print("Promedio de la energía al cuadrado ", prom_E2, ".")
    print("Capacidad calorífica: ", cap_cal)
    # print("Muchas gracias por utilizar nuestro programa. Un cordial saludo.")
    print("<3")
    # print(":D")

    return [prom_m, prom_m2, sus]






            
