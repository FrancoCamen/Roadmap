FUNCIONES = "lasfunciones sonbloques de codigo diseñadaspara realizar una acion, todos los lenguajes tienen funciones predeterminadas, pero si laque necesitas no existe tendras que crearlatu mismo"
#______________________________________________________________________________________________________#
def informacion ():       # se esta definiendo la funcion
    print ("Name: Franco Camen")
    print ("Edad: 18")

informacion()   # se esta llamando a la funcion ya definida

#______________________________________________________________________________________________________#
def datos (nombre):
    print (f"Name: {nombre}")
    
datos("Franco")
datos("Marti")

#______________________________________________________________________________________________________#
FUNCIONES_INTELIGENTES ="estas funciones utilizan paramtros, y cada uno de estos parametos conlleva un argumento"

def info (nombre, apellido = "desconocido"): # nombre y apellido son parametros y desconocido es un parametro por default
    print(f"mi nombre es {nombre} y mi apellido {apellido}")

info ("Franco", "Camen") # franco y camen son argumentos
info ("Marti",)

#______________________________________________________________________________________________________#
FUNCIONES_CON_RETORNO = "estas funciones poseen un retorno ya que  veces se necesita procesar esa informacion antes de pintarla en pantalla"

def infos (nombre):
    return nombre

estudiante = infos ("Franco")
print(estudiante)

#______________________________________________________________________________________________________#
nombre = "Jose"

def mostrar_nombre(nombre):
    print(f"hola {nombre}")

mostrar_nombre(nombre)

#______________________________________________________________________________________________________#
print(nombre.upper ()) # upper es un metodo que escribe un string en mayus
print(nombre.title ()) # title es un metodo que escribe un string como titulo

#los metodos tienen un sintaxis diferente a una funcion


