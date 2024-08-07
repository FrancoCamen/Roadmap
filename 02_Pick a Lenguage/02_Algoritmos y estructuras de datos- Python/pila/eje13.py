from pila import Pila

trajes = Pila()
aux = Pila()

# Cargar pila con trajes
trajes.push({"modelo": "Mark I", "pelicula": "Iron Man", "estado": "Dañado"})
trajes.push({"modelo": "Mark II", "pelicula": "Iron Man", "estado": "Dañado"})
trajes.push({"modelo": "Mark III", "pelicula": "Iron Man", "estado": "Dañado"})
trajes.push({"modelo": "Mark IV", "pelicula": "Iron Man 2", "estado": "Dañado"})
trajes.push({"modelo": "Mark V (Maleta)", "pelicula": "Iron Man", "estado": "Dañado"})
trajes.push({"modelo": "Mark VI", "pelicula": "The Avengers", "estado": "Dañado"})
trajes.push({"modelo": "Mark VII", "pelicula": "Iron Man 3", "estado": "Destruido"})
trajes.push({"modelo": "Mark XLII", "pelicula": "Iron Man 3", "estado": "Dañado"})
trajes.push({"modelo": "Mark XLIII", "pelicula": "Avengers: Age of Ultron", "estado": "Dañado"})
trajes.push({"modelo": "Mark XLIV (Hulkbuster)", "pelicula": "Avengers: Age of Ultron", "estado": "Dañado"})
trajes.push({"modelo": "Mark XLV", "pelicula": "Avengers: Age of Ultron", "estado": "Dañado"})
trajes.push({"modelo": "Mark XLVI", "pelicula": "Captain America: Civil War", "estado": "Dañado"})
trajes.push({"modelo": "Mark L", "pelicula": "Avengers: Infinity War", "estado": "Dañado"})
trajes.push({"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Dañado"})

# Se muestran todos los modelos de trajes con sus caracteristicas
print("Trajes de Iron Man: ")
while trajes.size() > 0:
    traje = trajes.pop()
    print(traje)
    aux.push(traje)
while aux.size() > 0:
    trajes.push(aux.pop())

# Busca si se encuentra el modelo Mark XLIV en la pila de trajes
def buscarModelo_XLIV(trajes):
    resultado = "no";
    peliculas = []
    # Busca modelo entre los modelos de trajes de la Pila
    while trajes.size() > 0:
        traje = trajes.pop()
        modelo_traje = traje["modelo"]
        if modelo_traje == "Mark XLIV (Hulkbuster)":
            resultado = "si"
            peliculas.append(traje["pelicula"])
        aux.push(traje)
    while aux.size() > 0:
        trajes.push(aux.pop())

    # Resultado
    if resultado == "si":
        print(f"El modelo Mark XLIV (Hulkbuster) fue utilizado en las siguientes peliculas: {peliculas}")
    else:
        print("El modelo no fue utilizado en ninguna pelicula")

# Busca y retorno los modelos de los trajes con estado dañado
def modelosDañados(trajes):
    dañados = []
    while trajes.size() > 0:
        traje = trajes.pop()
        estado = traje["estado"]
        if estado == "Dañado":
            dañados.append(traje["modelo"])
        aux.push(traje)
    while aux.size() > 0:
        trajes.push(aux.pop())
    
    # Resultado
    if dañados == []:
        print("No hay modelos de trajes dañados")
    else:
        print(f"Los trajes dañados son: {dañados}")

# Elimina modelos destruidos
def modelosDestruidos(trajes):
    destruidos = []
    while trajes.size() > 0:
        traje = trajes.pop()
        estado = traje["estado"]
        if estado == "Destruido":
            destruidos.append(traje["modelo"])
        else:
            aux.push(traje)
    while aux.size() > 0:
        trajes.push(aux.pop())

    # Resultado
    if destruidos == []:
        print("No se encontraron modelos de trajes Destruidos")
    else:
        print(f"Los modelos de trajes destruidos son: {destruidos}")

# Agrega un nuevo traje a la pila
def agregar(trajes):
    validacion = True;
    while validacion:
        # Pregunta datos del traje
        traje_modelo = input("Ingrese modelo del traje a agregar: ")
        traje_pelicula = input("Ingrese pelicula a la que corresponde el traje: ")
        while True:
            traje_estado = input("Ingresa estado del traje al finalizar la pelicula(Dañado, Destruido o Impecable): ")
            if traje_estado == "Dañado" or "Destruido" or "Impecable":
                break
            else:
                print("El estado del traje ingresado es invalido")

        encontro_traje = "no"
        while trajes.size() > 0:
            traje = trajes.pop()
            if traje_modelo == traje["modelo"] and traje_pelicula == traje["pelicula"] and traje_estado == traje["estado"]:
                encontro_traje = "si"
            aux.push(traje)
        while aux.size() > 0:
            trajes.push(aux.pop())
        
        if encontro_traje == "si":
            print("El traje ingresado ya existe en la pila")
        else:
            trajes.push({"modelo": traje_modelo, "pelicula": traje_pelicula, "estado": traje_estado})
            print("El traje fue agregado correctamente")
            validacion = False
            break
    
    print("Trajes actualizados")
    while trajes.size() > 0:
        traje = trajes.pop()
        print(traje)
        aux.push(traje)
    while aux.size() > 0:
        traje = aux.pop()
        trajes.push(traje)
    
# Muestra traje utilizados en tal pelicula
def mostrar_by_peli(trajes):
    pelicula = input("¿De que pelicula desea visualizar los trajes?")
    trajes_peli = []
    while trajes.size() > 0:
        traje = trajes.pop()
        if pelicula == traje["pelicula"]:
            trajes_peli.append(traje["modelo"])
        aux.push(traje)
    while aux.size() > 0:
        traje = aux.pop()
        trajes.push(traje)
    
    if trajes_peli == []:
        print(f"No se encontro ningun traje usado en {pelicula}")
    else:
        print(f"Trajes usado en ´{pelicula}´: {trajes_peli}")

