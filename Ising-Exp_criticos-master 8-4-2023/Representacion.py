import matplotlib.pyplot as plt
import numpy as np

def Representacion(data):

    # Extract columns from data
    M_vec = data[:, 0]
    Mabs_vec = data[:, 1]
    M2_vec = data[:, 2]
    E_vec = data[:, 3]
    E2_vec = data[:, 4]

    plt.plot( M_vec, "k", alpha = 0.3, lw = 3)
    plt.title("Magnetización por spin")
    plt.ylabel("Magnetización por spin, m")
    plt.xlabel("Tiempo")
    plt.savefig('./Graphics/M_plot.pdf', bbox_inches = 'tight')
    plt.close()

    plt.plot( Mabs_vec, "k", alpha = 0.3, lw = 3)
    plt.title("Magnetización por spin en valor absoluto")
    plt.ylabel("Magnetización por spin en valor absoluto, |m|")
    plt.xlabel("Tiempo")
    plt.savefig('./Graphics/M_abs_plot.pdf', bbox_inches = 'tight')
    plt.close()

    plt.plot( M2_vec, "k", alpha = 0.3, lw = 3)
    plt.title("Magnetización por spin al cuadrado")
    plt.ylabel("Magnetización por spin al cuadrado, $m^2$")
    plt.xlabel("Tiempo")
    plt.savefig('./Graphics/M2_plot.pdf', bbox_inches = 'tight')
    plt.close()

    plt.plot( E_vec, "k", alpha = 0.3, lw = 3)
    plt.title("Energía")
    plt.ylabel("Energía")
    plt.xlabel("Tiempo")
    plt.savefig('./Graphics/E_plot.pdf', bbox_inches = 'tight')
    plt.close()

    plt.plot( E2_vec, "k", alpha = 0.3, lw = 3)
    plt.title("Energía al cuadrado")
    plt.ylabel("Energía al cuadrado")
    plt.xlabel("Tiempo")
    plt.savefig('./Graphics/E2_plot.pdf', bbox_inches = 'tight')
    plt.close()

def Representación_T(data):

    # Extract columns from data
    temp = data[:, 0]
    M_vec = data[:, 1]
    Mabs_vec = data[:, 2]
    M2_vec = data[:, 3]
    Sus_vec = data[:, 4]
    E_vec = data[:, 5]
    E2_vec = data[:, 6]
    Cap_cal_vec = data[:, 7]


    plt.plot(temp, Mabs_vec, alpha = 1, lw = 3, label = 'Magnetización absoluta', color = 'pink')
    plt.plot(temp, Cap_cal_vec, alpha = 1, lw = 3, label = 'Capacidad calorífica', color = 'green')
    plt.title("Gráfica 3.7")
    plt.ylabel("Eje y")
    plt.xlabel("Temperatura")
    plt.legend()
    plt.savefig('./Graphics/Graph3_7.pdf', bbox_inches = 'tight')
    plt.close()

# def ReadRepresentación():
#     # Load data from CSV into NumPy arrays
#     data = np.loadtxt('./Data/Medidas.csv', delimiter=',')
#     data2 = np.loadtxt('./Data/Promedios(T).csv', delimiter=',')
#     Representacion(data)
#     Representación_T(data2)

# ReadRepresentación()