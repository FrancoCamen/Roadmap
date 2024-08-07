#______________________________________________________________________________________________________#
lenguajes = ["python" , "java" , "ruby" , "javascrip"] # cada uno va entre comillas
print (lenguajes)

print (lenguajes[1]) 

#______________________________________________________________________________________________________#
lenguajes.sort () # ordena alfabeticamente la lista, esto es un metodo
print (lenguajes)

#______________________________________________________________________________________________________#
# convinar unstring con un valorde una list
aprendiendo = f"estoy aprendiendo {lenguajes[0]}"
print (aprendiendo)

#______________________________________________________________________________________________________#
# cambiar valorde una lista por otro
lenguajes[2] = "PHP" # importante poner laposiciondel elemento
print (lenguajes)

#______________________________________________________________________________________________________#
# agregar otro valor a una lista
lenguajes.append("Kotil") # esto es un metodo
print (lenguajes)

#______________________________________________________________________________________________________#
# eliminar elementode una lista
del lenguajes[2] # señalar la posicion
print (lenguajes)

#______________________________________________________________________________________________________#
# eliminar con pop (metodo)
lenguajes.pop() # si no especificamos la posicion, pop elimina el ultimo elemento
print (lenguajes)

#______________________________________________________________________________________________________#
# eliminar con nombre con remove(metodo)
lenguajes.remove("ruby")
print (lenguajes)



