jugador = {}
print(jugador)

# se agrega un jugador
jugador["nombre"] = "franco"
print(jugador)

#se establece un puntaje
jugador["puntaje"] = 0
print(jugador)

#se incrementa un puntaje
jugador["puntaje"] = 100
print(jugador)

#acceder a un valor
print(jugador.get("consola", "no existe ese valor"))

#iterar en un diccionario
for llave,valor in jugador.items():
    print(llave)
    print(valor)

#eliminar valoresdel diccionario
del jugador["nombre"]
del jugador["puntaje"]
print(jugador)

    

 



