pregunta = "escribe un numero y te diresi es par o impar \r\n"
pregunta += '(si deseas salir de la aplicacion escribe "cerrar")\r\n' 
#al definir la misma varible dos veces con += se incrementa unasobre la otra pero con \r\n deja un renglon
preguntar = True

while preguntar:                     # while se ejecuta mientras la condicion sea verdadera
    numero = input(pregunta)

    if numero == "cerrar":
        preguntar = False
    else:
        numero = int(numero)

        if numero & 2 == 0:
            print(f"el numero {numero} es par")
        else:
            print(f"el numero {numero} es impar")













