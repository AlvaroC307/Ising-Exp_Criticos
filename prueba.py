from Medidas import *
from Montecarlo import *

""" plt.rcParams["savefig.dpi"] = 300
plt.rcParams["figure.dpi"] = 100
plt.rcParams["font.size"] = 10


red=red_random(100)
Energia_in=E_0(red, 1, 0, 100)
print(Energia_in)

pintar(red, 100)

for i in range(1):
    for j in range(1000):
        for k in range(1000):
            red[j][k]=1

    Energia_in=E_0(red, 1, 0, 1000)
    print(Energia_in) """

N=50
print(N)

red=red_random(N)
print(red)
Energia_in=E_0(red, N, 1, 0)
print(Energia_in)
print("Hola")

