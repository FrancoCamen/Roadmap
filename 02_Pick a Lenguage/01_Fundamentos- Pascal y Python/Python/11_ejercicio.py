playlist = {}   #diccionario vacio
playlist['canciones'] = []  #llave canciones sin ningun valor
                            #agrega un valor al diccionario vacio

def app():
    
    agregar_nombre_playlist = True

    while agregar_nombre_playlist:
        nombre_playlist = input ("¿Como deseas que se llame tu playlist? \r\n")
    
        if nombre_playlist:
             playlist['nombre'] = nombre_playlist
             agregar_nombre_playlist = False           #cuando se agregue un nombre se deja de preguntar
             agregar_canciones()

def agregar_canciones():

    agregar_cancion = True

    while agregar_cancion:
        #preguntar que cancion desea agregar
        name_playlist = playlist ["nombre"]
        pregunta = f"agrega canciones a la playlist {name_playlist} \r\n"
        pregunta += 'escribe "x" para dejarde aregar canciones\r\n'

        cancion = input(pregunta)

        if cancion == 'x':
            agregar_cancion = False
            mostrar_playlist()

        else:
            #agregar cancion
            playlist["canciones"].append(cancion)
            

def mostrar_playlist():
    name_playlist = playlist["nombre"]
    print(f"playist : {name_playlist}\r\n")
    print("canciones agregadas \r\n")
    
    for cancion in playlist["canciones"]:
        print(cancion)


app()






