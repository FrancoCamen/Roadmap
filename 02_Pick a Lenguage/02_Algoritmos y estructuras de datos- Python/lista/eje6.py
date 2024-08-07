# Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición, casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar las siguientes actividades:
from lista import Lista
from random import randint
sh = Lista()

# Clase SuperHeroe
class SuperHeroe():
    def __init__(self, name, year, empresa, biografia):
        self.name = name
        self.year = year
        self.empresa = empresa
        self.biografia = biografia

    def __str__(self):
        return f'{self.name} - {self.year} - {self.empresa} - {self.biografia}'

# lista de listas con los datos de cada superheroe
Personajes = [["Superman", 1938, "DC",
               "Superman, también conocido como Clark Kent, es el último hijo de Krypton. Fue enviado a la Tierra antes de la destrucción de su planeta natal y criado como el periodista Clark Kent en el pequeño pueblo de Smallville. Posee una fuerza sobrehumana, la capacidad de volar y una invulnerabilidad increíble. Se convierte en el defensor de Metrópolis, luchando contra el crimen y protegiendo a la humanidad."],
              ["Spider-Man", 1962, "Marvel",
               "Spider-Man, también conocido como Peter Parker, es un estudiante de secundaria con habilidades arácnidas. Después de ser mordido por una araña radiactiva, adquiere la fuerza proporcional de una araña, agilidad sobrehumana y la habilidad de trepar paredes. Peter lucha contra el crimen en Nueva York mientras lidia con su vida personal y su responsabilidad como héroe."],
              ["Batman", 1939, "Marvel",
               " Batman, también conocido como Bruce Wayne, es un multimillonario empresario y filántropo que se convierte en el vigilante enmascarado de Gotham City. Motivado por el asesinato de sus padres, Bruce utiliza su entrenamiento físico y su ingenio para combatir el crimen en la ciudad. Aunque no tiene superpoderes, cuenta con una amplia gama de gadgets y tecnología para ayudarlo en su lucha contra el crimen."],
              ["Iron Man", 1963, "Marvel",
               "Iron Man, también conocido como Tony Stark, es un genio empresario e ingeniero. Después de sufrir una lesión en el pecho, crea un traje blindado equipado con tecnología avanzada para mantenerse con vida y luchar contra el mal. Tony Stark utiliza su armadura para proteger al mundo y defender la justicia."],
              ["Wonder Woman", 1941, "DC",
               "Wonder Woman, también conocida como Diana Prince, es una guerrera amazona de la isla paradisíaca de Themyscira. Dotada de fuerza sobrehumana, habilidades de combate excepcionales y un lazo mágico de la verdad, se convierte en una defensora de la paz y la justicia. Wonder Woman deja su hogar para proteger el mundo de los mortales contra las amenazas que lo acechan."],
              ["Hulk", 1962, "Marvel",
               "Hulk es el alter ego de Bruce Banner, un científico brillante expuesto a radiación gamma. Cuando Bruce se enoja o se emociona intensamente, se transforma en Hulk, una criatura de piel verde con una fuerza descomunal. Aunque Hulk es a menudo incomprendido y perseguido, Bruce intenta controlar y canalizar su poder para proteger a los inocentes."],
              ["Captain America", 1941, "Marvel",
               "Captain America, también conocido como Steve Rogers, es un super soldado de la Segunda Guerra Mundial. Sometido a un experimento que lo convierte en un ser humano mejorado, Steve Rogers se convierte en el símbolo de la libertad y la justicia. Con su escudo indestructible, lucha contra las fuerzas del mal y defiende los valores americanos."],
              ["Linterna Verde", 1940, "DC",
               "Linterna Verde es el nombre compartido por varios miembros de la fuerza policial intergaláctica conocida como los Green Lantern Corps. Cada Linterna Verde porta un anillo de poder que le otorga la capacidad de crear construcciones de energía pura según su fuerza de voluntad. Estos héroes galácticos protegen el universo de las amenazas y representan el juramento de la Linterna Verde: En el día más brillante, en la noche más oscura, ningún mal escapará a mi vista, que aquellos que adoran el poder del mal teman mi poder... ¡la luz de la Linterna Verde!"],
              ["Wolverine", 1974, "Marvel",
               "Wolverine, también conocido como Logan o James Howlett, es un mutante con un factor de curación acelerado y garras retráctiles de adamantium en sus manos. Con un pasado misterioso y un temperamento feroz, Wolverine es conocido por su regeneración rápida y su habilidad en el combate cuerpo a cuerpo. Ha sido miembro destacado de los X-Men y ha luchado en numerosos conflictos para proteger a los mutantes y a la humanidad de amenazas sobrenaturales y enemigos mutantes. A pesar de su actitud áspera, Wolverine tiene un sentido feroz de la justicia y protege ferozmente a aquellos a quienes considera su familia."],
              ["Dr. Strange", 1963, "Marvel",
               "Doctor Strange, también conocido como Stephen Strange, es un antiguo cirujano convertido en hechicero supremo. Después de sufrir un accidente que dañó gravemente sus manos y lo dejó sin poder realizar cirugías, Stephen busca una cura desesperadamente y se adentra en el mundo de la magia y las artes místicas. Bajo la tutela de los antiguos maestros, adquiere poderes místicos y conocimientos para defender el plano terrenal contra amenazas místicas y extradimensionales. Doctor Strange es conocido por su astucia, su dominio de las artes místicas y su capacidad para manipular la realidad, protegiendo el universo de peligros sobrenaturales que pocos pueden enfrentar."],
              ["Capitana Marvel", 1968, "Marvel",
               "La Capitana Marvel, cuyo nombre real es Carol Danvers, es una poderosa heroína cósmica. Inicialmente conocida como Ms. Marvel, adquiere sus habilidades después de sufrir una explosión de un dispositivo alienígena llamado Psyche-Magnitron. Esta explosión fusiona su ADN humano con el de un Kree, otorgándole superpoderes, que incluyen fuerza sobrehumana, resistencia, velocidad y la capacidad de volar. La Capitana Marvel es una líder valiente y defensora de la justicia, protegiendo la Tierra y otros planetas contra amenazas extraterrestres. Su poder se amplifica aún más cuando se convierte en portadora del poder cósmico, convirtiéndola en una de las heroínas más poderosas del universo Marvel."],
              ["Flah", 1940, "DC",
               "Flash es el nombre compartido por varios personajes en el Universo DC que poseen la capacidad de correr a velocidades increíbles. El Flash más conocido es Barry Allen, un científico forense que obtiene sus poderes después de ser alcanzado por un rayo mientras trabaja en su laboratorio. Esta descarga de energía le otorga la habilidad de moverse a velocidades sobrehumanas y el poder de alterar la realidad a través de la Fuerza de la Velocidad. Flash utiliza sus habilidades para proteger Central City y el resto del multiverso DC, siendo un miembro clave de los superhéroes de la Liga de la Justicia. Su velocidad le permite realizar hazañas increíbles, como correr sobre el agua, viajar en el tiempo y vibrar a través de objetos sólidos."],
              ["Star-Lord", 1976, "Marvel",
               "Star-Lord, cuyo nombre real es Peter Quill, es un aventurero espacial y líder de los Guardianes de la Galaxia. Después de ser abducido de la Tierra cuando era niño, Peter se convierte en un experto piloto y ladrón interestelar. Él viaja por el cosmos en su nave espacial, la Milano, y se embarca en misiones para proteger la galaxia de amenazas alienígenas. Star-Lord es conocido por su carisma, su habilidad para improvisar y su sentido del humor. Además de ser un hábil combatiente, también utiliza tecnología avanzada, como sus icónicas pistolas de energía y su casco con capacidades de vuelo y comunicación. A lo largo de sus aventuras, Peter Quill se ha convertido en un héroe galáctico y un protector de la paz en el universo Marvel."]]

# Carga las listas en cada objeto superheroe y a la lista sh
for personaje in Personajes:
    superheroe = SuperHeroe(personaje[0], personaje[1], personaje[2], personaje[3])
    sh.insert(superheroe, "name")

# Mostrar lista sh
# sh.barrido()

# Funcion que remueve Linterna Verde
def remove_GreenLantern(sh):
    valor = sh.delete("Linterna Verde", "name")

# Funcion que muestra el año de aparicion de Wolverine
def get_year_Wolverine(sh):
    index = sh.search("Wolverine", "name")
    superheroe = sh.get_element_by_index(index)
    print(f"El año de aparicion de Wolverine es: {superheroe.year}")

# Cambiar empresa de Dr. Strange
def change_DrStrange(sh, search_value, new_value, criterio):
    index = sh.search(search_value, criterio)
    if criterio is not None:
        superheroe = sh.get_element_by_index(index)
        superheroe.empresa = new_value

# Busca los nombres de los heroes con "traje" o "armadura" en su biografia
# Y devuelve una lista
def search_suitORarmor(sh):
    nombres = []
    for index in range(0, sh.size()-1):
        superheroe = sh.get_element_by_index(index)
        biografia = superheroe.biografia
        if "traje" in biografia or "armadura" in biografia:
            nombres.append(superheroe.name)
    return nombres
        
print(f"Los superheores con traje o armadura en su biografia son {search_suitORarmor(sh)}")

    


