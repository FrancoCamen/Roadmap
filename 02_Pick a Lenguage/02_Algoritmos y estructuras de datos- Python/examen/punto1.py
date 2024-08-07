# Desarrollar una función recursiva que permita contar cuantas veces aparece una determinada palabra, en un vector de palabras.

palabras = ["Abcd", "Martes", "Palabra", "amigo", "Hola", "Franco"]
print(palabras)
palabra = input("Ingrese la palabra a contar cuantas veces aparece")
def search_palabra(palabra, vector):
    if not vector: 
        return 0
    elif vector[0] == palabra:  
        return 1 + search_palabra(palabra, vector[1:])  
    else:
        return search_palabra(palabra, vector[1:])


repiters = search_palabra(palabra, palabras)
if repiters == 0:
    print("La palabra seleccionada no se repite")
else:
    print(f"La palabra {palabra} se repite {repiters} veces")