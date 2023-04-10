from concurrent.futures import *
import time
from tqdm import tqdm

from Medidas import *
from Montecarlo import *
from Representacion import *
from Red import *

def One_Temp(N, N_calentar, N_med, N_mover, T_inicial, B, pintar_intermedios):

    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------RED INICIAL-------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------

    #   Creamos la red inicial y la pintamos
    red = red_random(N)
    pintar(red, N, "inicial")

    beta=1/T_inicial
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------VECTOR DE EXPONENCIALES-------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------

    vec_exp = Vector_Exponenciales(beta, B)

    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------CALENTAMIENTO-------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------

    print("Calentamiento: ")

    for j in tqdm(range(N_calentar)):
        Metropolis(red, N, vec_exp)

    m = np.zeros(N_med)
    e = np.zeros(N_med)

    #print("Montecarlo: ")
    #   Ejecutamos el algortimo de metropolis. Movemos N_mover entre cada medida. Medimo N_med veces
    print("Medidas de Montecarlo: ")

    velocidad_pasos_intermedios = 3 # Cuanto mayor, menos pasos intermedios se representan
    for i in tqdm(range(N_med)):
        for j in range(N_mover):
            Metropolis(red, N, vec_exp)

        # Cada vez que midamos pintamos el estado de la red, si así lo hemos decidido antes
        if pintar_intermedios == True and i % velocidad_pasos_intermedios == 0: # La segunda condición es porque si no las imágenes salen muy rápido y parece que causa un error
            nombre="Pasos_intermedios"
            pintar(red, N, nombre)

        #---------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------------------------------------
        #----------------------------------------------ESCRIBIR MEDIDAS-------------------------------------------------------
        #---------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------------------------------------

        #   Ejecutamos la función de magnetizaciones, que nos da un valor de la magnetización o otro de la magnetización al cuadrado.
        #   Guardamos las salidas y luego las escribimos en un archivo
        m[i] = magnetizaciones(red)
        e[i] = energias(red, B)

    #   Cerramos los archivos en lo que hemos escrito
    Medidas = np.column_stack((m, np.absolute(m), np.square(m), e, np.square(e)))

    np.savetxt('Data/Medidas_Una_Temp.csv', Medidas, delimiter=',',header='Magnetizacion Magnetization_Absoluta Magnetization_cuadrada Energia Energia_cuadrada')

    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #------------------------------------------PINTAR RED FINAL, PROMEDIOS------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------

    #   Pintamos la red al final del proceso
    pintar(red, N, "final")
    #   Llamamos a la función que calcula los promedios de las cantidades necesarias
    Promedio = promedios(N, beta, Medidas)
    #   Representamos
    Representacion(Medidas)

    print("El promedio de la magnetización es: ", Promedio[0])
    print("El promedio de la magnetización en valor absoluto es: ", Promedio[1])
    print("El promedio de la magnetización al cuadrado es: ", Promedio[2])
    print("La susceptibilidad es: ", Promedio[3])
    print("El promedio de la energía es: ", Promedio[4])
    print("El promedio de la energía al cuadrado es: ", Promedio[5])
    print("La capacidad calorífica es: ", Promedio[6])

    return None

list_Input = np.loadtxt('./Input/Input.csv', delimiter=',', usecols=(1,),dtype=np.float64)

N = int(list_Input[0]) # Número de puntos de la red
N_mover=int(list_Input[1])*N**2 # Número de veces que movemos antes de medir
N_med=int(list_Input[2])   # Número de veces que medimos
N_calentar=int(list_Input[3])*N**2  # Número de movimientos de calentamiento
B = list_Input[4] # Campo externo (B=\mu H)
pintar_intermedios = bool(int(list_Input[5])) # Variable que nos dice si pintar los pasos intermedios o no
loop_T = int(list_Input[6]) # Cantidad de puntos en los que se ejecuta el loop de temperaturas
temp_i = list_Input[7]
temp_f = list_Input[8]
una_temp = list_Input[9]

One_Temp(N, N_calentar, N_med, N_mover, una_temp, B, pintar_intermedios)