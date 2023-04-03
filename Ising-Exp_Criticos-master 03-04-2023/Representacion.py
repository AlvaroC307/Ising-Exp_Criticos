import matplotlib.pyplot as plt
import csv

def Representacion():

    csv_med = open('./Data/Medidas.csv', 'r') # Abrir el fichero donde están los datos de la magnetización por spin
    Reader_med = csv.reader(csv_med) # Definir un objeto que lee el fichero
    next(Reader_med)  # Saltar la primera línea (títulos)

    #   Definimos los vectores donde guardaremos los datos de cada variable
    M_vec=[]
    Mabs_vec=[]
    M2_vec=[]
    E_vec=[]
    E2_vec=[]

    #   Leemos los ficheros y los metemos en los vectores
    for row in Reader_med:
        M_vec.append(eval(row[0])) # Añadir cada elemento de cada fila del csv en una lista
        Mabs_vec.append(eval(row[1])) # Añadir cada elemento de cada fila del csv en una lista
        M2_vec.append(eval(row[2])) # Añadir cada elemento de cada fila del csv en una lista
        E_vec.append(eval(row[3])) # Añadir cada elemento de cada fila del csv en una lista
        E2_vec.append(eval(row[4])) # Añadir cada elemento de cada fila del csv en una lista

    N_med=len(M_vec)
    E_len = len(E_vec)

    csv_med.close() # Cerrar el fichero

    plt.plot( M_vec, "k", alpha = 0.3, lw = 3)
    plt.title("Magnetización por spin")
    plt.ylabel("Magnetización por spin, m")
    plt.xlabel("Tiempo")
    plt.savefig('./Graphics/M_plot.png', bbox_inches = 'tight')
    plt.close()

    plt.plot( Mabs_vec, "k", alpha = 0.3, lw = 3)
    plt.title("Magnetización por spin en valor absoluto")
    plt.ylabel("Magnetización por spin en valor absoluto, |m|")
    plt.xlabel("Tiempo")
    plt.savefig('./Graphics/M_abs_plot.png', bbox_inches = 'tight')
    plt.close()

    plt.plot( M2_vec, "k", alpha = 0.3, lw = 3)
    plt.title("Magnetización por spin al cuadrado")
    plt.ylabel("Magnetización por spin al cuadrado, $m^2$")
    plt.xlabel("Tiempo")
    plt.savefig('./Graphics/M2_plot.png', bbox_inches = 'tight')
    plt.close()

    plt.plot( E_vec, "k", alpha = 0.3, lw = 3)
    plt.title("Energía")
    plt.ylabel("Energía")
    plt.xlabel("Tiempo")
    plt.savefig('./Graphics/E_plot.png', bbox_inches = 'tight')
    plt.close()

    plt.plot( E2_vec, "k", alpha = 0.3, lw = 3)
    plt.title("Energía al cuadrado")
    plt.ylabel("Energía al cuadrado")
    plt.xlabel("Tiempo")
    plt.savefig('./Graphics/E2_plot.png', bbox_inches = 'tight')
    plt.close()
