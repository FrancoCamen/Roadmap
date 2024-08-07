nombre = input ("cual es tu nombre? \r\n") #la funcion imput detiene el codigo hasta que se responda la pregunta
                                           #\r\n realiza un salto de renglon                           

print(f"hola {nombre}")

#______________________________________________________________________________________________________#
edad= input ("cual es tu edad?\r\n")

edad = int(edad) # esta funcion convirta edad(string) en un entero

if edad >= 18:
    print("ya puedes votar")
else:
    print("no puedes votar")

#______________________________________________________________________________________________________#
#mezclarlos con operadores y numeros

numero = input ("escribe un numero y te digo si es par o impar \r\n")

numero = int(numero)

if numero % 2 == 0: # signifa si es resto de ese numero al dividirlo por 2 es 0
    print(f"el numero {numero} es par")
else:
    print(f"el numero {numero} es impar")




