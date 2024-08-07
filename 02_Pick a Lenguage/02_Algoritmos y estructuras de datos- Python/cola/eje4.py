from cola import Cola
from random import randint

cola = Cola()

for i in range (10):
    num = randint(1, 100)
    cola.arrive(num)
    print(num)

for i in range(cola.size()):
    numero = cola.atention()
    divisible = False
    for i in range(2, numero):
        if numero % i == 0:
            divisible = True
    if divisible != True:
        cola.arrive(numero)

print("Valores primos en la cola")
while cola.size() > 0:
    print(cola.atention())   
