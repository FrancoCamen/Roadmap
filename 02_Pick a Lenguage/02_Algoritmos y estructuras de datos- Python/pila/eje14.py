# Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden ordenados de forma creciente. Solo puede utilizar una pila auxiliar como estructura extra –no se pueden utilizar métodos de ordenamiento–

from pila import Pila
stack = Pila()

def agregar(stack, valor):
    aux = Pila()
    if stack.size() > 0:
        while stack.size() > 0:
            element = stack.pop()
            if valor < element:
                stack.push(element)
                stack.push(valor)
                break
            elif valor > element:
                aux.push(element)
                if stack.size() == 0: 
                    stack.push(valor)
                    break
        while aux.size() > 0:
            stack.push(aux.pop())
        return stack
    else:
        stack.push(valor)
        return stack

def visualizar(stack):
    aux = Pila()
    while stack.size() > 0:
        element = stack.pop()
        print(element)
        aux.push(element)
    while aux.size() > 0:
        stack.push(aux.pop())

while True:
    opcion = input("Ingrese que accion desea realisar (Agregar, Visualizar o Salir)")
    if opcion != "Agregar" and opcion != "Visualizar" and opcion != "Salir":
        print("La opcion ingresada es incorrecta")
    else:
        if opcion == "Agregar":
            valor = int(input("Ingrese valor a agregar"))
            stack = agregar(stack, valor)
        elif opcion == "Visualizar":
            visualizar(stack)
        else:
            break



