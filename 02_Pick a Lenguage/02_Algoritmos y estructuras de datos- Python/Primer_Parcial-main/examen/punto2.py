from lista import Lista
from cola import Cola

class Personajes():
    def __init__(self, supername, name, team, year):
        self.supername = supername
        self.name = name
        self.team = team
        self.year = year

    def __str__(self):
        return f"{self.supername} - {self.name} - {self.team} - {self.year}"
    
personajes = [["Capitana Marvel", "Carol Danvers", "Vengadores", 1968],
              ["Star-Lord", "Peter Quill", "Guardianes de la Galaxia", 1976],
              ["Señor de las Estrellas", "Peter Quill", "Guardianes de la Galaxia", 1976],
              ["Drax el Destructor", "Arthur Douglas", "Guardianes de la Galaxia", 1973],
              ["Gamora", "", "Guardianes de la Galaxia", 1975],
              ["Groot", "", "Guardianes de la Galaxia", 1960],
              ["Rocket Raccoon", "Rocket", "Guardianes de la Galaxia", 1976],
              ["Sr. Fantástico", "Reed Richards", "Los Cuatro Fantásticos", 1961],
              ["La Mujer Invisible", "Susan Storm", "Los Cuatro Fantásticos", 1961],
              ["La Antorcha Humana", "Johnny Storm", "Los Cuatro Fantásticos", 1961],
              ["La Cosa", "Ben Grimm", "Los Cuatro Fantásticos", 1961],
              ["Vlack Widow", "Natasha Romanoff", "Vengadores", 1964],
              ["Iron Man", "Tony Stark", "Vengadores", 1963],
              ["Capitán América", "Steve Rogers", "Vengadores", 1941],
              ["Thor", "", "Vengadores", 1962],
              ["Hulk", "Bruce Banner", "Vengadores", 1962],
              ["Hawkeye", "Clint Barton", "Vengadores ", 1964],
              ["Viuda Negra", "Yelena Belova", "Vengadores", 1999],
              ["Pantera Negra", "T'Challa", "Vengadores", 1966],
              ["Doctor Strange", "Stephen Strange", "Vengadores", 1963]]

sh = Lista()
for personaje in personajes:
    sh.insert(Personajes(personaje[0], personaje[1], personaje[2], personaje[3]), "supername")

# Busca Capitana Marvel y muestra nombre de personaje
def search_CM(sh):
    index = sh.search("Capitana Marvel", "supername")
    if index != None:
        personaje = sh.get_element_by_index(index)
        print(f"El nombre de personaje de Capitana Marvel es {personaje.name}")
    else:
        print("Capitana Marvel no esta en la Lista")

# Almacena los Guardianes de la galaxia en una cola e indica cuantos son
def search_Guardianes(sh):
    guardians = Cola()
    for i in range (0, sh.size()-1):
        personaje = personaje = sh.get_element_by_index(i)
        team = personaje.team
        if team == "Guardianes de la Galaxia":
            guardians.arrive(personaje)
    cant = guardians.size()
    if cant != 0:
        print(f"La cantidad de guardianes de la galaxia es {cant}")
    else:
        print("No hay personajes Guardianes de la Galaxia en la lista")

# Muestra de manera descendente los 4 fantasticos y Guradianes de la galaxia
def show(sh):
    fourFantastic = Lista()
    guardianes = Lista()
    sh.order_by("supername", True)
    for i in range (0, sh.size()-1):
        personaje = personaje = sh.get_element_by_index(i)
        if personaje.team == "Los Cuatro Fantásticos":
            fourFantastic.insert(personaje.supername)
        if personaje.team == "Guardianes de la Galaxia":
            guardianes.insert(personaje.supername)
    print("____ Los Cuatro Fantásticos ____")
    fourFantastic.barrido()
    print("____ Guardianes de la Galaxia ____")
    guardianes.barrido()

# Lista superheores con year mayor a 1960
def year1960(sh):
    shs = Lista()
    for i in range (0, sh.size()-1):
        personaje = sh.get_element_by_index(i)

        if personaje.year > 1960 and personaje.name != "":
            shs.insert(personaje, "supername")
    print("____ Heores con nombre de personaje y apariciones posterioeres a 1960 ____")
    shs.barrido()

# Modifica Vlack Widow por Black widow
def modify(sh):
    sh.order_by("supername", False)
    pos = sh.search("Vlack Widow", "supername")
    personaje = sh.get_element_by_index(int(pos))
    print("____ Personaje sin modificar ____")
    print(personaje)
    personaje.supername = "Black Widow"
    sh.insert(personaje, "supername")
    sh.order_by("supername", False)
    index = sh.search("Black Widow", "supername")
    personaje = sh.get_element_by_index(index)
    print("____ Personaje Modificado ____")
    print(personaje)

# Lista auxiliar con otros personajes
personajes = [["Black Cat", "Felicia Hardy", "Aliados de Spider-Man", 1979],
              ["Hulk", "Bruce Banner", "Vengadores", 1962],
              ["Rocket Raccoon", "Rocket", "Guardianes de la Galaxia", 1976],
              ["Loki ", "", "Vengadores", 1962]]
sh_aux = Lista()
for personaje in personajes:
    sh_aux.insert(Personajes(personaje[0], personaje[1], personaje[2], personaje[3]), "supername")

# Agrega sh_aux a sh en caso de que no esten
def agregar(sh, sh_aux):
    for heroe in range (0, sh_aux.size()-1):
        personaje_aux = sh_aux.get_element_by_index(heroe)
        coincide = False
        for i in range (0, sh.size()-1):
            personaje = sh.get_element_by_index(i)
            if personaje_aux.supername == personaje.supername:
                coincide == True
        if coincide == False:
            sh.insert(personaje_aux, "supername")

# Mostrar los que empiezen con C , P o S
def mostrarCPS(sh):
    nombres = []
    for i in range (0, sh.size()-1):
        personaje = sh.get_element_by_index(i)
        letras = ["C", "P", "S"]
        if personaje.supername[0] in letras:
            nombres.append(personaje.supername)
    if nombres != []:
        print(f"Los personajes que empiezan con C, P o S son {nombres}")
    else:
        print("No hay personajes que comienzen con C, P o S")




print()
search_CM(sh)
print()
search_Guardianes(sh)
print()
show(sh)
print()
year1960(sh)
print()
modify(sh)
print()
agregar(sh, sh_aux)
print()
mostrarCPS(sh)
print()
