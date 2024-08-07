# Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista
from lista import Lista
from random import randint
# insert - search - search-r - delete - size - barrido - order_by - get_element_by_index - set_value

lista = Lista()

# Cargar lista
for i in range(15):
    lista.insert(randint(1, 50))
lista.barrido()

position = int(input("Ingrese la posicion i-ésima en la que desea ingresar el nodo"))

def insertar_termino(lista, position):
    elements = []
    sima = lista.size() -1
    while sima >= position:
        index = lista.get_element_by_index(sima)
        elements.append(lista.delete(index))
        sima = sima - 1
    lista.insert(randint(1, 50))
    while len(elements) > 0:
        valor = elements.pop()
        lista.insert(valor)

insertar_termino(lista, position)
lista.barrido()





