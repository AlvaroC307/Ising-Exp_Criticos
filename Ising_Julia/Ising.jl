#A mi por defecto se me ejecuta con el boton ▷ en REPL, que es lo más rápido
#La primera vez que lo ejecutas tarda un ratito en empezar a ejecutar el programa (30 segundos +-)
#El resto de veces tarda muy poco
#(Creo que tiene que abrir el terminal y mierdas)
#ACTUALIZACION
#(Probando a ejecutarlo desde el REPL de julia.exe tarda lo mismo la primera vez
#Probablemente tiene que cargar paquetes o algo, no será abrir el terminal)
#ACTUALIZACION2
#Probando tiene que hacer ambas cosas, en abrir el terminal tarda unos 8 segundos
#Y en cargar los paquetes (supongo) o mierdas unos 22 segundos

#Si lo ejecutar con Ctrl+F5 o con otra cosa no se por qué tarda en empezar a ejecutarlo
#No se, no soy experto, probablemento haya otra forma de ejecutarlo sin que tenga que cargar el terminal ni tarde tanto en empezar

#Para incluir otros archivos con funciones: include("Nombre.jl")
include("Medidas.jl")
include("Montecarlo.jl")
include("Representación.jl")

#Para usar paquetes: using NombrePaquete
#ANTES HAY QUE INSTALARLOS. PARA INSTALAR:(mirar "Notas/pkg_add.csv")
#Escribir ] en el terminal de julia de VSCode (esto abre el terminal para instalar paquetes)
#Escribir es este terminal add "NombrePaquete" (mirar "Notas/pkg_add.csv" para ver los
#paquetes que hay que instalar)
using CSV
using DataFrames
using ProgressBars
using Plots

function main()

    #Lee el archivo input, lo mete en un DataFrame y lo guarda en input. [!,2] elige todas las filas y solo la columna 2.
    #Un DataFrame es una tabla con titulos, 
    #las columnas y filas de input son lo que está "dentro" de la tabla (sin titulos)
    #Para ver que es un DataFrame se puede ejecutar println(CSV.read("Input/Input.csv", DataFrame))

    input = CSV.read("Input/Input.csv", DataFrame)[!,2]
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------INPUT--------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------

    #Guarda cada dato en una variable y le da el tipo correspondiente
    N = Int(input[1])
    N_mover = Int(input[2]*N^2)
    N_med = Int(input[3])
    N_calentar = Int(input[4]*N^2)
    B = input[5]
    β = input[6]
    red_intermedia = Bool(input[7])

    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #------------------------------------VECTORES EXPONENCIALES-----------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------

    #Escribe en una matriz 2x5 los posibles valores de la exponencial.
    vec_exp = zeros(2,5)
    s0 = -1
    for i in 1:2
        for j in 1:5
            vec_exp[i, j] = exp(2*β*(s0*((j-3)*2)+B*s0))
        end
        s0 = -s0
    end

    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------RED INICIAL--------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------

    #Crea la red inicial, la guarda y la imprime por pantalla
    red = red_random(N)
    pintar(red, N, "inicial")

    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------CALENTAMIENTO------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------

    #Realiza N_calentar movimientos de calentamiento. ProgressBar() muestra la barra de progreso
    println("Calentamiento: ")
    #Hacemos movimientos de calentamiento
    for i in ProgressBar(1:N_calentar)
        Metropolis(red, N, vec_exp)
    end    

    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------METROPOLIS----------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------

    println("Montecarlo: ")
    #Crea 5 vectores vacíos para meter las medidas
    m, m_abs, m2, E, E2 = [], [], [], [], []
    #Ejecutamos el algortimo de metropolis. Movemos N_mover entre cada medida. Medimos N_med veces
    for i in ProgressBar(1:N_med)
        for j in 1:N_mover
            Metropolis(red, N, vec_exp)
        end

        medida_m = magnetizaciones(red, N)
    #push! hace lo mismo que append en python (añade el valor medida_m[i] al vector m)
        push!(m, medida_m[1])
        push!(m_abs, medida_m[2])
        push!(m2, medida_m[3])

        medida_E = Energia(red, N, B)
        push!(E, medida_E[1])
        push!(E2, medida_E[2])

    # Cada vez que midamos pintamos el estado de la red, si así lo hemos decidido antes
        if red_intermedia == true
            pintar(red, N, "Pasos intermedios")
        end

    end

    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------GUARDAR DATOS------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------

    #Guardamos en un DataFrame las medidas con su correspondiente título
    #Así es más fácil guardarlo y extraer datos del DataFrame
    data = DataFrame(Magnetización = m,
    Magnetización_absoluta = m_abs,
    Magnetización_cuadrada = m2,
    Energía = E,
    Energía_cuadrada = E2)
    
    #Escribimos las medidas en el archivo Medidas.csv
    CSV.write("Data/Medidas.csv",data)

    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------REPRESENTACION, RED FINAL Y PROMEDIOS-----------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------

    #Representamos los datos en plots
    Representacion(data)

    #Pintamos la red al final de la simulación
    pintar(red, N, "final")

    #Calculamos los promedios de magnetizaciones y energias, sus y cap_calorifica
    promedios(N, β, data)
    
    return nothing
end


#@time function() mide el tiempo que tarda en ejecutar dicha función
#@time "Algo" function() escribe Algo y luego te dice cuanto ha tardado en ejecutarse la función
#También se puede usar:
#@time begin
#    codigo
#    codigo
#end
#Y te dice el tiempo que tarda en ejcutar el codigo entre el begin y el end

@time "Ha tardado" main()

#println() y print() son diferentes:
#println() imprime lo que hay entre paréntesis seguido de un salto de línea
#print() lo imprime sin salto de línea 
#Lo que significa que si pones
#print("Lo que sea")
#print("Lo que sea2")
#Lo imprime en la misma línea: Lo que seaLo que sea2

println()
println("------------------------------------------------------------------")
println()
println("MAGNETO")
println("""⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣶⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⡿⢛⣿⣿⣿⣿⣿⣿⣿⣿⡛⢿⣦⡀⠀⠀⠀
⠀⠀⣰⣿⡟⠀⠀⣿⣿⠿⠛⠛⠿⣿⣿⠀⠀⢻⣿⣆⠀⠀
⠀⣰⣿⣿⣿⡀⠀⠹⣿⠀⠀⠀⠀⣿⠏⠀⢀⣿⣿⣿⣧⠀
⢠⣿⣿⣿⣿⣿⣦⣤⣘⣇⠀⠀⣸⣁⣤⣴⣿⣿⣿⣿⣿⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⠟⠛⠛⠻⣿⣿⣿⣿⠟⡛⠛⠻⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣇⠀⠚⠛⠓⠈⠛⠛⠁⠚⠛⠓⠀⣹⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣷⣤⣤⣄⠀⠀⠀⠀⣠⣤⣤⣾⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠘⠻⠿⣿⣿⣿⣿⣿⣿⠛⠛⠛⠛⣿⣿⣿⣿⣿⣿⠿⠟⠃
⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠉⠋⠉⠉⠀⠀⠀⠀⠀""")
