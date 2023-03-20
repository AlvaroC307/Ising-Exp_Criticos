
def Delta_E(i, j, red, N, J, B): # Cálculo la variación de la energía al cambiar un spin 

    if i == (N-1):
        if j == (N-1):
            Delta_E = - J*red[i][j]*(red[0][j]+red[i-1][j]+red[i][0]+red[i][j-1]) -B*red[i][j]
        else:
            Delta_E = - J*red[i][j]*(red[0][j]+red[i-1][j]+red[i][j+1]+red[i][j-1]) -B*red[i][j]
   
    else:
        if j == (N-1):
            Delta_E = - J*red[i][j]*(red[i+1][j]+red[i-1][j]+red[i][0]+red[i][j-1]) -B*red[i][j]
        else:
            Delta_E = - J*red[i][j]*(red[i+1][j]+red[i-1][j]+red[i][j+1]+red[i][j-1]) -B*red[i][j]

    return (2*Delta_E)


def E_0(red, N, J, B):#Calculo de la energía inicial

    E_0=0

    for i in range (N):
        for j in range (N):

            if i == N-1:
                if j == N-1:
                    E_0 += - J*red[i][j]*(red[0][j]+red[i-1][j]+red[i][0]+red[i][j-1]) -B*red[i][j]
                else:
                    E_0 += - J*red[i][j]*(red[0][j]+red[i-1][j]+red[i][j+1]+red[i][j-1]) -B*red[i][j]
   
            else:
                if j == N-1:
                    E_0 += - J*red[i][j]*(red[i+1][j]+red[i-1][j]+red[i][0]+red[i][j-1]) -B*red[i][j]
                else:
                    E_0 += - J*red[i][j]*(red[i+1][j]+red[i-1][j]+red[i][j+1]+red[i][j-1]) -B*red[i][j]

    return E_0


def mag(red, N): # Magnetizacion

    mag = 0
    for i in range (N):
        for j in range(N):
            mag+=red[i][j]
    return mag


def mag2(red, N): # Magnetizacion^2

    mag2 = 0
    for i in range (N):
        for j in range(N):
            mag+=red[i][j]**2
    return mag2


def sus(red, N, beta): # Susceptibilidad

    sus = beta * N * ((mag2(red, N) / N) - (mag(red, N) / N)**2)
    
    return sus
            
