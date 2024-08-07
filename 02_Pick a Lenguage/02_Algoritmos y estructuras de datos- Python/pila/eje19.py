from pila import Pila

class Peliculas():
    def __init__(self, title, study,  year):
        self.__title = title
        self.__study = study
        self.__year = year
    def get_title(self):
        return self.__title
    def get_study(self):
        return self.__study
    def get_year(self):
        return self.__year
    def __str__(self):
         return f'{self.__title} - {self.__study} - {self.__year}'
    
pelis = Pila()
pelis.push(Peliculas("Titanic", "Paramount Pictures", 1997))
pelis.push(Peliculas("The Avengers", "Marvel Studios", 2012))
pelis.push(Peliculas("The Shawshank Redemption", "Castle Rock Entertainment", 1994))
pelis.push(Peliculas("Harry Potter and the Philosopher's Stone", "Warner Bros. Pictures", 2001))
pelis.push(Peliculas("The Dark Knight", "Warner Bros. Pictures", 2008))
pelis.push(Peliculas("Pulp Fiction", "Miramax Films", 1994))
pelis.push(Peliculas("Inception", "Warner Bros. Pictures", 2010))
pelis.push(Peliculas("The Lion King", "Walt Disney Pictures", 1994))
pelis.push(Peliculas("Avatar", "20th Century Fox", 2009))
pelis.push(Peliculas("La La Land", "Summit Entertainment", 2016))
pelis.push(Peliculas("Guardians of the Galaxy", "Marvel Studios", 2014))
pelis.push(Peliculas("Black Panther", "Marvel Studios", 2016))
aux = Pila()

# Peliculas estrenada en 2014
pelis2014 = []
while pelis.size() > 0:
    peli = pelis.pop()
    if peli.get_year() == 2014:
        pelis2014.append(peli.get_title())
    aux.push(peli)
while aux.size() > 0:
    pelis.push(aux.pop())
if pelis2014 == []:
    print("Dentro de la pila no hay peliculas estrenadas en 2014")
else:
    print(f"Las peliculas estrenadas en 2014 son: {pelis2014}")

# Cuantas pelis se estrenaron en 2018
contador = 0
while pelis.size() > 0:
    peli = pelis.pop()
    if peli.get_year() == 2018:
        contador += 1
    aux.push(peli)
while aux.size() > 0:
    pelis.push(aux.pop())
if contador == 0:
    print("Dentro de la pila no hay peliculas estrenadas en 2018")
else:
    print(f"Dentro de la pila hay {contador} peliculas que se estrenaron en 2018")

# Peliculas de Marvel estrenadas en 2016
pelis2016 = []
while pelis.size() > 0:
    peli = pelis.pop()
    if peli.get_year() == 2016 and peli.get_study() == "Marvel Studios":
        pelis2016.append(peli.get_title())
    aux.push(peli)
while aux.size() > 0:
    pelis.push(aux.pop())
if pelis2016 == []:
    print("Dentro de la pila no hay peliculas de Marvel Studios estrenada en 2016")
else:
    print(f"Las peliculas de Marvel estrenadas en 2016 son: {pelis2016}")





