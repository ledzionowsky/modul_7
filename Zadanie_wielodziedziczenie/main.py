import random
from typing import List, Any

lista = []

class Film():
    def __init__(self, tytul, rok_wydania, gatunek, liczba_odtworzen):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen

    def play(self, step=1):
        self.liczba_odtworzen += step

    def __str__(self):
        return f'{self.tytul} ({self.rok_wydania})'


class Serial(Film):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu

    def __str__(self):
        return self.tytul + " S" + "{:02d}".format(self.numer_sezonu) + "E" + "{:02d}".format(self.numer_odcinka)


serial = Serial(tytul="Dexter", rok_wydania="2006", gatunek="kryminał", liczba_odtworzen=122, numer_sezonu=2,
                numer_odcinka=3)
lista.append(serial)

serial2 = Serial(tytul="Breaking Bad", rok_wydania="2010", gatunek="dramat", liczba_odtworzen=12314343, numer_sezonu=4,numer_odcinka=10)
lista.append(serial2)

film = Film(tytul="Shawshank redemption", rok_wydania="1997", gatunek="Dramat", liczba_odtworzen=128882)
lista.append(film)

film2 = Film(tytul="Batman", rok_wydania="2006", gatunek="sci-fi", liczba_odtworzen=34521)
lista.append(film2)


series = []
def get_series():
    for i in lista:
        if isinstance(i, Serial):
            series.append(i)
    return series


movies=[]
def get_movies():
    for i in lista:
        if not isinstance(i, Serial):
            movies.append(i)

    return movies

def print_list(lista):
    for i in lista:
        print(i)

lista.sort(key=lambda x: x.tytul)

def search():
    input_title = str(input("podaj tytuł: "))
    for x in lista:
        if x.tytul==input_title:
            print(x.tytul, x.rok_wydania, x.gatunek, x.liczba_odtworzen)

def generate_views():
    a = random.choice(lista)
    a.liczba_odtworzen = random.randrange(1,100)
    print(a, a.liczba_odtworzen)

def generate_viewsx10():
    for i in range(10):
        generate_views()

def top_titles():
    i = int(input("Podaj ile najpopularniejszych tytułów chcesz poznać: "))
    lista.sort(key=lambda x: x.liczba_odtworzen)
    print_list(lista[:i])

#print_list(lista)
#print()
#print_list(get_series())
#print()
#print_list(get_movies())
#print()
#search()
#print()
#generate_views()
#top_titles()
#generate_viewsx10()