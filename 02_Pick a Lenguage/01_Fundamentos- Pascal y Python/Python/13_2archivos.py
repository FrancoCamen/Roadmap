def app():
    # cuando se usa with open no es necesario cerrar la conexion con el archivo
    with open("archivo.txt") as archivo:  #r es para lectura, se pone por default
        for contenido in archivo:
            print(contenido.rstrip().)    # .rstrip remueve los saltos de linea

app()