# Insertar el nombre de la diosa griega Atenea en la i-ésima posición debajo de la cima de una pila con nombres de dioses griegos.
from pila import Pila

pila_dioses = Pila();
pila_aux = Pila();

# Carga de la pila
pila_dioses.push("Zeus")
pila_dioses.push("Hera")
pila_dioses.push("Poseidon")
pila_dioses.push("Afrodita")
pila_dioses.push("Ares")
pila_dioses.push("Apolo")
pila_dioses.push("Artemisa")
pila_dioses.push("Hades")
pila_dioses.push("Hermes")
pila_dioses.push("Dionisio")

# Mostramos elementos de la pila de Dioses;
print ("Pila de Dioses")
while pila_dioses.size() > 0:
    nom = pila_dioses.pop();
    pila_aux.push(nom);
    print(nom);
while pila_aux.size() > 0:
    nom = pila_aux.pop();
    pila_dioses.push(nom);

# Posicion de la palabra que desea remplazar 
i = pila_dioses.size();
while i > (pila_dioses.size()-1):
    i = int(input("Ingrese la posicion i-esima debajo de la cima del Dios griego que desea reemplazar por Atenea: "));
    if i <= (pila_dioses.size()-1):
        break
    else:
        print("La posicion ingresada es mayor al tamaño de la pila");

# Desapilar pila_dioses hasta posicion i
for x in range(0, i+1):
    pila_aux.push(pila_dioses.pop());

# Reemplazamos Dios y cargamos en pila_dioses
elemento_i_ésimo = pila_aux.pop();
pila_aux.push("Atenea");
while pila_aux.size() > 0:
    pila_dioses.push(pila_aux.pop());

# Mostramos elementos de pila_dioses
while pila_dioses.size() > 0:
    print(pila_dioses.pop());


