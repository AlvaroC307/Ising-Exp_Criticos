<<<<<<< HEAD

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------SPIN SUMA-----------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

#mod1() calcula el resto de la división pero si fuera a salir 0 da N, (no se, funciona bien con estos vectores que van de 1 a N).
SpinSuma(i, j, red, N) = red[mod1(i+1,N), j]+red[mod1(i-1,N), j]+red[i, mod1(j+1,N)]+red[i, mod1(j-1,N)]
#Tambien se puede definir asi:

#= function SpinSuma(i, j, red, N) # Función que calcula la suma de los spines vecinos al red[i,j]     
    ssuma = red[mod1(i+1,N), j]+red[mod1(i-1,N), j]+red[i, mod1(j+1,N)]+red[i, mod1(j-1,N)]
    return ssuma
end =#

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#-------------------------------------------MAGNETIZACIONES-----------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

function magnetizaciones(red, N) # Magnetizaciones
    m = sum(red)/N^2
    return [m abs(m) m^2]
    #Aqui los vectores se pueden poner como [a, b, c] o [a b c] (es lo mismo)
end

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#------------------------------------------------ENERGÍAS-------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

function Energia(red, N, B) #Calculo de la energía total

    E = 0

    for i in 1:N
        for j in 1:N
            E += -red[i, j]*(red[mod1(i+1,N), j]+red[i, mod1(j+1,N)]+B)
            #Aqui solo usa los spines de la derecha y de abajo (para no contar ninguno 2 veces)     
        end
    end
    
    return [E E^2]
end

#---------------------------------------------------------------------------------------------------------------------

function energias(i, j, red, N, E_0, B) # Calcula la variación de energía al cambiar el spin [i, j]
    #No se usa en el programa porque se calcula la energía entera cada vez que se mide (aunque se puede cambiar)

    Delta_E = 2*red[i, j]*(SpinSuma(i, j, red, N)+B)  # Ecuación 3.10 del Newman

    E = E_0 + Delta_E
    e = E/(N^2)
    e2 = e^2
    return [e e2 E]
end

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------PROMEDIOS--------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

function promedios(N, β, data)
    
    #Recupera los datos del DataFrame de datos usando el título de la columna para elegirla
    m_vec = data[!,:Magnetización]
    m2_vec = data[!,:Magnetización_cuadrada]
    E_vec = data[!, :Energía]
    E2_vec = data[!, :Energía_cuadrada]

    # Miramos las longitudes
    N_med=length(m_vec)
    N_mover=length(E_vec)

    # Hallamos los promedios
    prom_m = sum(m_vec)/N_med
    prom_m2 =sum(m2_vec)/N_med
    sus = β*N^2*(prom_m2-prom_m^2)

    prom_E = sum(E_vec)/N_mover
    prom_E2 =sum(E2_vec)/N_mover
    cap_cal = (β/N)^2*(prom_E2-prom_E^2)
    
    println("------------------------------------------------------------------")
    # print("Buenas tardes, usuario.")
    println("Promedio de la magnetización: ", prom_m, ".")
    println("Promedio de la magnetización al cuadrado ", prom_m2, ".")
    println("Susceptibilidad: ", sus)
    println("Promedio de la energía: ", prom_E, ".")
    println("Promedio de la energía al cuadrado ", prom_E2, ".")
    println("Capacidad calorífica: ", cap_cal)
    # print("Muchas gracias por utilizar nuestro programa. Un cordial saludo.")
    println("<3")
    # print(":D")

    return [prom_m prom_m2 sus]
=======

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------SPIN SUMA-----------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

#mod1() calcula el resto de la división pero si fuera a salir 0 da N, (no se, funciona bien con estos vectores que van de 1 a N).
SpinSuma(i, j, red, N) = red[mod1(i+1,N), j]+red[mod1(i-1,N), j]+red[i, mod1(j+1,N)]+red[i, mod1(j-1,N)]
#Tambien se puede definir asi:

#= function SpinSuma(i, j, red, N) # Función que calcula la suma de los spines vecinos al red[i,j]     
    ssuma = red[mod1(i+1,N), j]+red[mod1(i-1,N), j]+red[i, mod1(j+1,N)]+red[i, mod1(j-1,N)]
    return ssuma
end =#

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#-------------------------------------------MAGNETIZACIONES-----------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

function magnetizaciones(red, N) # Magnetizaciones
    m = sum(red)/N^2
    return [m abs(m) m^2]
    #Aqui los vectores se pueden poner como [a, b, c] o [a b c] (es lo mismo)
end

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#------------------------------------------------ENERGÍAS-------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

function Energia(red, N, B) #Calculo de la energía total

    E = 0

    for i in 1:N
        for j in 1:N
            E += -red[i, j]*(red[mod1(i+1,N), j]+red[i, mod1(j+1,N)]+B)
            #Aqui solo usa los spines de la derecha y de abajo (para no contar ninguno 2 veces)     
        end
    end
    
    return [E E^2]
end

#---------------------------------------------------------------------------------------------------------------------

function energias(i, j, red, N, E_0, B) # Calcula la variación de energía al cambiar el spin [i, j]
    #No se usa en el programa porque se calcula la energía entera cada vez que se mide (aunque se puede cambiar)

    Delta_E = 2*red[i, j]*(SpinSuma(i, j, red, N)+B)  # Ecuación 3.10 del Newman

    E = E_0 + Delta_E
    e = E/(N^2)
    e2 = e^2
    return [e e2 E]
end

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------PROMEDIOS--------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

function promedios(N, β, data)
    
    #Recupera los datos del DataFrame de datos usando el título de la columna para elegirla
    m_vec = data[!,:Magnetización]
    m2_vec = data[!,:Magnetización_cuadrada]
    E_vec = data[!, :Energía]
    E2_vec = data[!, :Energía_cuadrada]

    # Miramos las longitudes
    N_med=length(m_vec)
    N_mover=length(E_vec)

    # Hallamos los promedios
    prom_m = sum(m_vec)/N_med
    prom_m2 =sum(m2_vec)/N_med
    sus = β*N^2*(prom_m2-prom_m^2)

    prom_E = sum(E_vec)/N_mover
    prom_E2 =sum(E2_vec)/N_mover
    cap_cal = (β/N)^2*(prom_E2-prom_E^2)
    
    println("------------------------------------------------------------------")
    # print("Buenas tardes, usuario.")
    println("Promedio de la magnetización: ", prom_m, ".")
    println("Promedio de la magnetización al cuadrado ", prom_m2, ".")
    println("Susceptibilidad: ", sus)
    println("Promedio de la energía: ", prom_E, ".")
    println("Promedio de la energía al cuadrado ", prom_E2, ".")
    println("Capacidad calorífica: ", cap_cal)
    # print("Muchas gracias por utilizar nuestro programa. Un cordial saludo.")
    println("<3")
    # print(":D")

    return [prom_m prom_m2 sus]
>>>>>>> 95bbd10921ed654fbb4ecc8bb3d11b30c27ee8b8
end