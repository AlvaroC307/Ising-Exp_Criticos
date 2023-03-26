import matplotlib.pyplot as plt
import csv 
import numpy as np

def pintar(red, N, nombre):

    Color_Matrix=[]
    for i in range(N):
        Color_List=[]
        for j in range(N):
            if red[i][j]==1:
                #Color_List.append([1., 1., 1., 1.]) # Blanco en RGBA
                Color_List.append([0.99, .25, .60, 1]) # Barbie Pink (2005-2009) en RGBA
            if red[i][j]==-1:
                #Color_List.append([0., 0., 0., 1.]) # Negro en RGBA
                Color_List.append([.0, .87, .64, 1]) # Asda Green (1985) en RGBA
        Color_Matrix.append(Color_List)
        

    #color_array = np.array([[mcolors.to_rgba(color) for color in row] for row in Color_Matrix])


    # Create a figure and plot the image
    fig, ax = plt.subplots(figsize=(5, 5)) # figsize habla sobre el tamaño de la imagen
    ax.imshow(Color_Matrix)

    # Quitar los ejes, guardar y mostrar en pantalla la imagen 
    ax.axis('off')
    plt.savefig('./Graphics/Ising_' + nombre + '.png', bbox_inches='tight') # Guardar la imagen como un png
    #plt.savefig('./Graphics/Ising_' + nombre + '.pdf', bbox_inches='tight') # Guardar la imagen como un png
    #plt.show() # Mostrar la imagen
    plt.close()


def Representacion():

    csv_M = open('./Data/Magnetizacion.csv', 'r') # Abrir el fichero donde están los datos de la magnetización por spin
    Reader_M = csv.reader(csv_M) # Definir un objeto que lee el fichero
    csv_M2 = open('./Data/Magnetizacion2.csv', 'r') # Abrir el fichero donde están los datos de la magnetización por spin al cuadrado
    Reader_M2 = csv.reader(csv_M2) # Definir un objeto que lee el fichero
    csv_E = open('./Data/Energia.csv', 'r') # Abrir el fichero donde están los datos de la magnetización por spin al cuadrado
    Reader_E = csv.reader(csv_E) # Definir un objeto que lee el fichero

    M_vec=[]
    M2_vec=[]
    E_vec = []

    for row in Reader_M:
        M_vec.append(eval(row[0])) # Añadir cada elemento de cada fila del csv en una lista

    for row in Reader_M2:
        M2_vec.append(eval(row[0])) # Añadir cada elemento de cada fila del csv en una lista

    for row in Reader_E:
        E_vec.append(eval(row[0])) # Añadir cada elemento de cada fila del csv en una lista

    N_med=len(M_vec)
    E_len = len(E_vec)

    csv_M.close() # Cerrar el fichero
    csv_M2.close() # Cerrar el fichero
    csv_E.close() # Cerrar el fichero

    plt.plot( M_vec, "k", alpha = 0.3, lw = 3)
    plt.title("Magnetización por spin")
    plt.ylabel("Magnetización por spin, m")
    plt.xlabel("Tiempo")
    plt.savefig('./Graphics/M_plot.png', bbox_inches = 'tight')
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
