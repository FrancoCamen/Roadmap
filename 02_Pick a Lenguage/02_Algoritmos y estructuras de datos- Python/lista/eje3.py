# Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos, una que contenga los números pares y otra para los números impares.
# insert - search - search-r - delete - size - barrido - order_by - get_element_by_index - set_value
from lista import Lista
from random import randint

lista = Lista()
lista_par = Lista()
lista_impar = Lista()

# Cargar lista
for i in range(15):
    lista.insert(randint(1, 50))
lista.barrido()

tamaño = lista.size()-1
for i in range (0, tamaño):
    element = lista.get_element_by_index(i)
    if element % 2 != 0:
        lista_impar.insert(element)
    else:
        lista_par.insert(element)
    
print("Numeros Pares")
lista_par.barrido()
print("Numeros Impares")
lista_impar.barrido()