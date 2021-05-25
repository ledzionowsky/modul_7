from faker import Faker

fake = Faker()
class BaseContact:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie=imie
        self.nazwisko=nazwisko
        self.telefon=telefon
        self.email=email

    def contact(self):
        return f'Wybieram numer {self.telefon} i dzwonię do {self.imie}, {self.nazwisko}'

    @property
    def name_length(self):
        return len(self.imie) + len(self.nazwisko) + 1

class BusinessContact(BaseContact):
    def __init__(self,stanowisko,nazwa_firmy,telefon_s,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.stanowisko=stanowisko
        self.nazwa_firmy=nazwa_firmy
        self.telefon_s=telefon_s

    def contact(self):
        return f'Wybieram numer {self.telefon_s} i dzwonię do {self.imie}, {self.nazwisko}'

    @property
    def name_length(self):
        return len(self.imie) + len(self.nazwisko) + 1

    def create_contacts(contact_type,x):
        contact_type=input("Wprowadź typ wizytówki (BusinessContact/BaseContact)")
        x=input("Podaj ile wizytówek potrzebujesz")
        if contact_type = 'BusinessContact':
            for i in range(x):

        elif contact_type = 'BaseContact'




