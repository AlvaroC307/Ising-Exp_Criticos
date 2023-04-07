<<<<<<< HEAD
using Colors
using Plots
using DataFrames
using CSV

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------PINTAR RED------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

function pintar(red, N, nombre) #Pinta la red

    #Crea una matriz de tipo RGB vacia NxN
    color_matrix = Matrix{RGB}(undef,(N,N))

    #La llena con colores en función del valor de red
    for i in 1:N
        for j in 1:N
            if red[i, j] == 1
                color_matrix[i, j] = RGB(0.99, .25, .60)
            else
                color_matrix[i, j] = RGB(.0, .87, .64)
            end
        end
    end

    #Crea el plot y lo guarda
    plot(color_matrix, axis = false, grid = false, size = (500,500), background = false)
    savefig("Graphics/"*nombre*".png")#Sale con más calidad en png que en pdf (razon? ninguna, pero pasa)

    return nothing
end

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#-------------------------------------------REPRESENTAR RESULTADOS----------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

function Representacion(data)

    Extension = "pdf"#Sale con más calidad en pdf que en png

    #Crea plots de cada columna de datos de la matriz data y los guarda
    plot(data[!,:Magnetización], 
    legend = false, grid = false)
    savefig("Graphics/Magnetizacion."*Extension)

    plot(data[!,:Magnetización_absoluta], 
    legend = false, grid = false)
    savefig("Graphics/Magnetizacion_absoluta."*Extension)

    plot(data[!,:Magnetización_cuadrada], 
    legend = false, grid = false)
    savefig("Graphics/Magnetizacion_cuadrada."*Extension)

    plot(data[!,:Energía], 
    legend = false, grid = false)
    savefig("Graphics/Energía."*Extension)

    plot(data[!,:Energía_cuadrada], 
    legend = false, grid = false)
    savefig("Graphics/Energía_cuadrada."*Extension)

    return nothing
end

function ReadPlot()

    #Por si quieres hacer la representación a partir de los datos guardados
    #Ejecuta en la linea de comandos ReadPlot()

    data=CSV.read("Data/Medidas.csv", DataFrame)
    Representacion(data)

    return nothing
=======
using Colors
using Plots
using DataFrames
using CSV

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------PINTAR RED------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

function pintar(red, N, nombre) #Pinta la red

    #Crea una matriz de tipo RGB vacia NxN
    color_matrix = Matrix{RGB}(undef,(N,N))

    #La llena con colores en función del valor de red
    for i in 1:N
        for j in 1:N
            if red[i, j] == 1
                color_matrix[i, j] = RGB(0.99, .25, .60)
            else
                color_matrix[i, j] = RGB(.0, .87, .64)
            end
        end
    end

    #Crea el plot y lo guarda
    plot(color_matrix, axis = false, grid = false, size = (500,500), background = false)
    savefig("Graphics/"*nombre*".png")#Sale con más calidad en png que en pdf (razon? ninguna, pero pasa)

    return nothing
end

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#-------------------------------------------REPRESENTAR RESULTADOS----------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

function Representacion(data)

    Extension = "pdf"#Sale con más calidad en pdf que en png

    #Crea plots de cada columna de datos de la matriz data y los guarda
    plot(data[!,:Magnetización], 
    legend = false, grid = false)
    savefig("Graphics/Magnetizacion."*Extension)

    plot(data[!,:Magnetización_absoluta], 
    legend = false, grid = false)
    savefig("Graphics/Magnetizacion_absoluta."*Extension)

    plot(data[!,:Magnetización_cuadrada], 
    legend = false, grid = false)
    savefig("Graphics/Magnetizacion_cuadrada."*Extension)

    plot(data[!,:Energía], 
    legend = false, grid = false)
    savefig("Graphics/Energía."*Extension)

    plot(data[!,:Energía_cuadrada], 
    legend = false, grid = false)
    savefig("Graphics/Energía_cuadrada."*Extension)

    return nothing
end

function ReadPlot()

    #Por si quieres hacer la representación a partir de los datos guardados
    #Ejecuta en la linea de comandos ReadPlot()

    data=CSV.read("Data/Medidas.csv", DataFrame)
    Representacion(data)

    return nothing
>>>>>>> 95bbd10921ed654fbb4ecc8bb3d11b30c27ee8b8
end