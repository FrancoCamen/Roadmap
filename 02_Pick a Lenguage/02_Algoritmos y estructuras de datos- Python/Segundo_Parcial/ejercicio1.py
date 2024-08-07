from arbolFranco import BinaryTree

name = BinaryTree()
number = BinaryTree()
type = BinaryTree()

pokemon_data = [
    {'name':"Bulbasaur", 'numero':1, 'tipo':"Planta-Veneno"},
    {'name':"Charmander", 'numero':4, 'tipo':"Fuego"},
    {'name':"Squirtle", 'numero':7, 'tipo':"Agua"},
    {'name':"Pikachu", 'numero':25, 'tipo':"Eléctrico"},
    {'name':"Jigglypuff", 'numero':39,'tipo': "Normal-Hada"},
    {'name':"Gengar", 'numero':94, 'tipo':"Fantasma-Veneno"},
    {'name':"Snorlax", 'numero':143, 'tipo':"Normal"},
    {'name':"Mewtwo", 'numero':150, 'tipo':"Psíquico"},
    {'name':"Gyarados", 'numero':130, 'tipo':"Agua-Volador"},
    {'name':"Machamp", 'numero':68, 'tipo':"Lucha"},
    {'name': "Jolteon", 'numero': 135, 'tipo': "Eléctrico"},
    {'name': "Lycanroc", 'numero': 745, 'tipo': "Roca"},
    {'name': "Tyrantrum", 'numero': 697, 'tipo': "Roca-Dragón"},
    {'name': "Lucario", 'numero': 448, 'tipo': "Lucha-Acero"}
]

for pokemon in pokemon_data:
    name.insert_node(pokemon['name'], [pokemon['numero'], pokemon['tipo']])
    number.insert_node(pokemon['numero'], [pokemon['name'], pokemon['tipo']])
    type.insert_node(pokemon['tipo'], [pokemon['numero'], pokemon['name']])

def point_B():
    num=int(input("Ingrese el numero de Pokemon a buscar"))
    number.search_Number_Pokemons(num)

    print()
    namein=input("Ingrese nombre de Pokemon a buscar")
    name.search_Name_Pokemons(namein)

point_B()

def point_C():
    print("Muestra los nombres de los Pokemones de tipo Agua, Fuego, Planta o Electrico")
    type.inorden_Types()

point_C()

def point_D():
    print("Se muestra en orden ascendentes los pokemons segun su numero")
    number.inorden_Number()
    print()

    print("Se muestra en orden ascendentes los pokemons segun su nombre")
    name.inorden_Name()
    print()

    print("Se muestra un listado por nivel de los pokemons segun su nombre")
    name.by_level_Name()
    print()

point_D()

def point_E():
    print("Muestra los datos del Pokemon Jolteon, Lycanroc y Tyrantrum")
    name.search_Name_Pokemons("Jolteon")
    name.search_Name_Pokemons("Lycanroc")
    name.search_Name_Pokemons("Tyrantrum")


point_E()

def point_F():
    print("Muestra cuantos Pokémons hay de tipo eléctrico y acero")
    print(f"Electricos: {type.contarElectricos()}, Aceros: {type.contarAcero()}")

point_F()

