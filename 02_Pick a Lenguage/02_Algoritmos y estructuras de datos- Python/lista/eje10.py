from lista import Lista
from random import randint

class Cancion():
    def __init__(self, nombre, artista, duracion, repro):
        self.nombre = nombre;
        self.artistas = artista;
        self.duracion = duracion;
        self.repro = repro;

    def __str__(self):
        return f'{self.nombre} - {self.artista} - {self.duracion} - {self.repro}';

# Creacion de instancias de la clase Cancion
if 2+2 ==4:
    cancion1 = Cancion("Bohemian Rhapsody", "Queen", 6.07, 500)
    cancion2 = Cancion("Imagine", "John Lennon", 3.03, 300)
    cancion3 = Cancion("Hotel California", "Eagles", 6.30, 450)
    cancion4 = Cancion("Smells Like Teen Spirit", "Nirvana", 5.01, 400)
    cancion5 = Cancion("Hey Jude", "The Beatles", 7.11, 350)
    cancion6 = Cancion("Shape of You", "Ed Sheeran", 3.54, 1000)
    cancion7 = Cancion("Uptown Funk", "Mark Ronson ft. Bruno Mars", 4.30, 850)
    cancion8 = Cancion("Hallelujah", "Leonard Cohen", 4.37, 700)
    cancion9 = Cancion("Despacito", "Luis Fonsi ft. Daddy Yankee", 3.34, 1200)
    cancion10 = Cancion("Hello", "Adele", 4.55, 600)
    cancion11 = Cancion("Blinding Lights", "The Weeknd", 3.20, 850)
    cancion12 = Cancion("Dance Monkey", "Tones and I", 3.29, 700)
    cancion13 = Cancion("Bad Guy", "Billie Eilish", 3.14, 1200)
    cancion14 = Cancion("Someone Like You", "Adele", 4.45, 600)
    cancion15 = Cancion("Stairway to Heaven", "Led Zeppelin", 8.02, 900)
    cancion16 = Cancion("Imagine", "John Lennon", 3.02, 850)
    cancion17 = Cancion("De Música Ligera", "Soda Stereo", 4.11, 900)
    cancion18 = Cancion("Persiana Americana", "Soda Stereo", 4.50, 750)
    cancion19 = Cancion("Prófugos", "Gustavo Cerati", 5.08, 600)
    cancion20 = Cancion("Cuando Pase el Temblor", "Soda Stereo", 3.41, 1000)
    cancion21 = Cancion("Ojos Color Sol", "Calle 13 ft. Silvio Rodríguez", 4.23, 850)
    cancion22 = Cancion("La Flaca", "Jarabe de Palo", 4.11, 800)
    cancion23 = Cancion("Nada Personal", "Soda Stereo", 4.23, 700)
    cancion24 = Cancion("El Matador", "Los Fabulosos Cadillacs", 4.10, 950)
    cancion25 = Cancion("En el Muelle de San Blas", "Maná", 5.35, 600)
    cancion26 = Cancion("El Duelo", "La Ley", 4.33, 800)
    cancion27 = Cancion("El Salmón", "Andrés Calamaro", 5.45, 800)
    cancion28 = Cancion("Una Llave", "Abel Pintos", 3.55, 650)
    cancion29 = Cancion("Trátame Suavemente", "Soda Stereo", 3.29, 700)
    cancion30 = Cancion("Ella Usó Mi Cabeza Como un Revólver", "Soda Stereo", 4.17, 950)
    cancion31 = Cancion("Puente", "Gustavo Cerati", 3.43, 600)
    cancion32 = Cancion("La Bifurcada", "Memphis La Blusera", 3.40, 850)
    cancion34 = Cancion("Lamento Boliviano", "Enanitos Verdes", 3.52, 900)
    cancion35 = Cancion("Tanta Ciudad", "Indio Solari", 4.02, 700)
    cancion36 = Cancion("Luz de Día", "Enanitos Verdes", 4.20, 1000)
    cancion37 = Cancion("La Renga - La Balada del Diablo y La Muerte", "La Renga", 5.19, 750)
    cancion38 = Cancion("Garota de Ipanema", "Antônio Carlos Jobim", 4.50, 800)
    cancion39 = Cancion("Ai Se Eu Te Pego", "Michel Teló", 2.46, 650)
    cancion40 = Cancion("Mas Que Nada", "Sergio Mendes", 2.39, 700)
    cancion41 = Cancion("Chega de Saudade", "João Gilberto", 2.05, 1000)
    cancion42 = Cancion("Trem das Onze", "Adoniran Barbosa", 3.15, 850)
    cancion43 = Cancion("Águas de Março", "Elis Regina & Tom Jobim", 3.33, 800)
    cancion44 = Cancion("Canta, Canta Minha Gente", "Martinho da Vila", 3.33, 700)
    cancion45 = Cancion("Brasileirinho", "Waldir Azevedo", 2.38, 950)
    cancion46 = Cancion("Aquarela do Brasil", "Ary Barroso", 2.57, 650)
    cancion47 = Cancion("Tropicália", "Caetano Veloso", 3.02, 900)
    cancion48 = Cancion("Do I Wanna Know?", "Arctic Monkeys", 4.33, 5000)
    cancion49 = Cancion("R U Mine?", "Arctic Monkeys", 3.21, 700)
    cancion50 = Cancion("Baby I'm Yours", "Arctic Monkeys", 4.56, 900)

# Carga de las instancias en Lista()
lista_canciones = Lista();
for i in range(1, 51):
    obj = "cancion" + str(i) 
    lista_canciones.insert(obj)





