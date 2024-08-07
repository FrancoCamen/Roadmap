#creando un diccionario simple
horario = {
    "matematica" : "lunes y jueves",   # llave y valor
    "lengua" : "miercoles y viernes",
    "historia" : "martes y jueves",
}

print(horario)

#acceder a un valor del diccionario
print(horario["matematica"])

#mezclar un string con un diccionario
matematica = horario["matematica"]  # se utiliza una variable

print(f"tengo matematicas los {matematica}")

#agregar valor nuevo 
horario["geografia"] = "miercoles y jueves"
print(horario)

#cambiar valor existente
horario["lengua"] = "lunes y martes"
print(horario)

#eliminar un valor
del horario["historia"]
print(horario)
