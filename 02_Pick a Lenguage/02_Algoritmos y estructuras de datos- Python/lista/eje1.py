# Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.
from lista import Lista
# insert - search - search-r - delete - size - barrido - order_by - get_element_by_index - set_value

lista = Lista()

# Cargar lista
class Persona():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido

    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.edad}'

persona1 = Persona('Juana', 'Gomez', 34)
persona2 = Persona('Mario', 'Impini', 47)
persona3 = Persona('Laurato', 'Perez', 19)
lista.insert(persona1, "edad")
lista.insert(persona2, "edad")
lista.insert(persona3, "edad")

lista.barrido()

# Determinar cantidad de nodos en Lista
print(f"La cantidad de nodos es: {lista.size()}")

