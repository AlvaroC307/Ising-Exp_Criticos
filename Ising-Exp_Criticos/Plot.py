
import matplotlib.pyplot as plt
#import matplotlib.colors as mcolors # Esto es para cambiar los colores a valores numéricos




def pintar(red, N, nombre):

    Color_Matrix=[]
    for i in range(N):
        Color_List=[]
        for j in range(N):
            if red[i][j]==1:
                #Color_List.append([1., 1., 1., 1.]) # Blanco en RGBA
                Color_List.append([254., 0., 128., 1.]) # Rosa en RGBA
            if red[i][j]==-1:
                #Color_List.append([0., 0., 0., 1.]) # Negro en RGBA
                Color_List.append([124., 252., 0., 1.]) # Verde en RGBA
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



