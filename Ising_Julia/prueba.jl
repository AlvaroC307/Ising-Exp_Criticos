function prueba()
    N=50000000
    for i in 1:N
        i^i
    end

end

@time prueba()