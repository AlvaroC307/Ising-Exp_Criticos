import numpy as np
from PIL import Image

def red_random(N):  # Función que crea la red cuadrada

    # Crea una red (matriz) de NxN elementos con valores -1 o +1

    red = np.random.choice([-1, -1], size=(N, N))   # Elige un número aleatorio entre los que estén entre corchetes
    return red

def pintar(red, N, nombre):

    spin_up = np.array([252, 64, 153]) # Color para el spin up en RGB 0.99, .25, .60
    spin_down = np.array([0, 222, 163]) # Color para el spin down en RGB .0, .87, .64

    Color_Matrix = np.zeros((N, N, 3), dtype=np.uint8) # Crea una matriz de ceros

    Color_Matrix[red == 1] = spin_up # Pone el color spin_up en las posiciones que coincidan con un 1 en la red
    Color_Matrix[red == -1] = spin_down # Pone el color spin_down en las posiciones que coincidan con un -1 en la red

    img = Image.fromarray(Color_Matrix) # Crea la imagen a partir de la matriz RGB
    img = img.resize((500, 500), resample=Image.NEAREST) # La redimensiona y evita que sea difusa cuando tenemos pocos píxeles
    img.save('./Graphics/Ising_' + nombre + '.png', bbox_inches='tight') # Guarda la imagen
    img.close() # Cierra la imagen
