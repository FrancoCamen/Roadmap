#______________________________________________________________________________________________________#
balance = 10
if balance > 0:
    print ("puede pagar")
if balance < 0:
    print ("no puede pagar")

#______________________________________________________________________________________________________#
dinero = 10
if dinero >= 15:
    print ("puede comprar")
else: # se va a correr cuando la condicion de arriba no se cumpla
    print ("no puede pagar")

#______________________________________________________________________________________________________#
likes = 200
if likes >= 200:
    print ("felicitaciones")
else:
    print ("sos re malo")

#______________________________________________________________________________________________________#
# == igual, >= mayor o igual, <= menor o igual 
lenguaje = "php"
if not lenguaje == "python": # el not hace que la condicionse cumpla cuando no sea asi
    print("buena eleccion")
#significa diferente a

#______________________________________________________________________________________________________#
#evaluar un boolean
usuario_verificado = True
if usuario_verificado == True: #puedes eliminar el true y igual se va a ejecutar cuando sea verdadero
    print ("Acceso permitido")
else:
    print ("Acceso denegado")

#______________________________________________________________________________________________________#
#evaluar elemento de una lista
lenguajes = ["python", "kotlin", "ruby","java", "go"]

if "python" in lenguajes:  
    print("si esta")
else:
    print("no esta")

#______________________________________________________________________________________________________#
"if anidados"
usuario_verificado = True
usuario_admin = False

if usuario_verificado:
    if usuario_admin:
        print("llego el admin pa")
    else:
        print("acceso permitido")
else:
    print("acceso denegado")

#______________________________________________________________________________________________________#
ocupado = True
estudiante = False
jubilado = True


if ocupado:
    if estudiante:
        print("tienes 50% de descuento")
    if jubilado:
        print("tienes 40% de descuento")
else:
    print("no tienes descuento")

#______________________________________________________________________________________________________#
"elif" #evalua dos o mas condiciones dentro de una misma variable
ocupacion = "Estudiante"

if ocupacion == "Estudiante":
    print("tienes 50% de descuento")
elif ocupacion == "Jubilado":
    print("tienes 40% de descuento") 
else:
    print("debes pagar el 100%")

#______________________________________________________________________________________________________#
# el operador AND y OR evalua dos condiciones a la ves
usuario_logueado = True
usuario_admin = True

if usuario_logueado and usuario_admin: # AND es sinonimo de Y y OR sinonimo de O
    print ("administrador")
elif usuario_logueado:
    print("acceso permitido")
else:
    print("acceso denegado")




