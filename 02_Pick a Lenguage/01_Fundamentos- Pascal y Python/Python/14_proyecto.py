import os 

CARPETA = "contactos/"  # carpeta de contactos
EXTENSION = ".txt"      # extension de archivos

#Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


def app():
    #revisar si existe la carpeta o no 
    crear_directorio()
    #muestra el menu de opciones
    mostrar_menu()

    #preguntar al usuario la accion a realizar
    preguntar = True
    while preguntar:
        opcion = input("Seleccione una opcion: \r\n")
        opcion = int(opcion)

        #Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contacto()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print("Opcion no valida, intentar de nuevo")

def eliminar_contacto():
    nombre = input("Seleccione el Contacto que desea eliminar: \r\n")

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print("\r\n Contacto Eliminado Correctmente \r\n")
    except:
        print("El contacto no existe")

    app()


def buscar_contacto():
    nombre = input("Seleccione el Contacto que desea buscar: \r\n")

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print("\r\n Informacion del contacto: \r\n")
            for linea in contacto:
                print(linea.rstrip())
            print("\r\n")
    except IOError:
        print("El contacto no existe")
        print(IOError)
    
    app()


def mostrar_contacto():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print("\r\n")


def editar_contacto():
    print("¿Que Contacto deseas editar?")
    nombre_anterior = input("Nombre del contacto que desea editar: \r\n")

    #revisar si el archivo ya existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, "w") as archivo:


            #Resto de los campos
            nombre_contacto = input("Agrega el nuevo Nombre: \r\n")
            telefono_contacto = input("Agregar el nuevo Telefono:  \r\n")
            categoria_contacto = input("Agregar la nueva Categoria: \r\n")

            #instanciar
            #contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            

            #Escribir en el archivo
            archivo.write("Nombre: " + nombre_contacto + "\r\n")
            archivo.write("Telefono: " + telefono_contacto + "\r\n")
            archivo.write("Categoria: " + categoria_contacto + "\r\n")

            #renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
    else:
        print("Ese Contacto no existe")
        app()


def agregar_contacto():
    print("Escribe los datos necesarios para un nuevo Contacto ")
    nombre_contacto = input("Nombre del contacto: \r\n")

    #revisar si el archivo ya existe antes de crearlo
    existe = os.path.isfile(CARPETA + nombre_contacto + EXTENSION)

    if not existe:
        #esto va a crear el archivo al nombrarlo y tmb escribir dentro del archivo
        with open(CARPETA + nombre_contacto + EXTENSION, "w") as archivo:
            #resto de los campos
            telefono_contacto = input("Agregar Telefono:  \r\n")
            categoria_contacto = input("Agregar Categoria: \r\n")

            #instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el archivo
            archivo.write("Nombre: " + contacto.nombre + "\r\n")
            archivo.write("Telefono: " + contacto.telefono + "\r\n")
            archivo.write("Categoria: " + contacto.categoria + "\r\n")

            #Mostrar mensaje de exito
            print("\r\n Contacto creado correctamente \r\n")
    else:
        print("Ese Contacto ya existe")
    
    #reiniciar la app
    app()
    

def mostrar_menu():
    print("seleccione del menu lo que desea realizar")
    print("1) Agregar Nuevo Contacto")
    print("2) Editar Contacto")
    print("3) Ver Contactos")
    print("4) Buscar Contacto")
    print("5) Eliminar Contacto")


def crear_directorio():
    if not os.path.exists(CARPETA):  # si la carpeta no existe esta funcion la crea
        os.makedirs(CARPETA)         # esta funcion crea un directorio o carpeta


def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()

