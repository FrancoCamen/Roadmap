# Dada una pila de objetos de una oficina de los que se dispone de su nombre y peso (por ejemplo monitor 1 kg, teclado 0.25 kg, silla 7 kg, etc.), ordenar dicha pila de acuerdo a su peso del objeto más liviano al más pesado. Solo pueden utilizar pilas auxiliares como estructuras extras, no se pueden utilizar métodos de ordenamiento.
from pila import Pila

class objeto_oficina():

    def __init__(self, nombre, peso):
        self.__nombre = nombre
        self.__peso = peso
    
    def get_nombre(self):
        return self.__nombre
    def get_peso(self):
        return self.__peso
    def __str__(self):
        return f'{self.__nombre} - {self.__peso}'
    

stack = Pila()
aux = Pila()
obj1 = objeto_oficina("Monitor", 3)
obj2 = objeto_oficina("Teclado", 0.25)
obj3 = objeto_oficina("Escritorio", 30)
obj4 = objeto_oficina("Impresora", 20)
obj5 = objeto_oficina("Estanteria", 15)
obj6 = objeto_oficina("Papelera", 2)
obj7 = objeto_oficina("Fax", 7)
stack.push(obj1)
stack.push(obj2)
stack.push(obj3)
stack.push(obj4)
stack.push(obj5)
stack.push(obj6)
stack.push(obj7)

# Ordenar pila
def ordenar(stack):
    aux = Pila()
    

    while stack.size() > 0:
        element = stack.pop()
        while aux.size() > 0 and aux.on_top().get_peso() > element.get_peso():
            stack.push(aux.pop())
        aux.push(element)
    
    while aux.size() > 0:
        stack.push(aux.pop())
    
    return stack

stack = ordenar(stack)
while stack.size() > 0:
    print(stack.pop())







