lista=[]
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

    def dodawanie_do_listy(self):
        return lista.append()

class Serial(Film):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu

    def __str__(self):
        return self.tytul + " S" + "{:02d}".format(self.numer_sezonu) + "E" + "{:02d}".format(self.numer_odcinka)


serial = Serial(tytul="Dexter", rok_wydania="2006", gatunek="kryminał", liczba_odtworzen=122, numer_sezonu=2,
                numer_odcinka=3)
film = Film(tytul="Shawshank redemption", rok_wydania="1997", gatunek="Dramat", liczba_odtworzen=128882)
print(serial)
lista.append(serial)
print(film)
lista.append(film)
print(lista)