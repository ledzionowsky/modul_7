from faker import Faker

fake = Faker()


class BaseContact:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

    def __str__(self):
        return f'{self.imie}, {self.nazwisko}, {self.telefon}, {self.email}'

    def contact(self):
        return f'Wybieram numer {self.telefon} i dzwonię do {self.imie}, {self.nazwisko}'

    @property
    def name_length(self):
        return len(self.imie) + len(self.nazwisko) + 1


class BusinessContact(BaseContact):
    def __init__(self, stanowisko, nazwa_firmy, telefon_s, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stanowisko = stanowisko
        self.nazwa_firmy = nazwa_firmy
        self.telefon_s = telefon_s

    def __str__(self):
        return f'{self.imie}, {self.nazwisko}, {self.telefon}, {self.email}, {self.stanowisko}, {self.nazwa_firmy}, {self.telefon_s}'

    def contact(self):
        return f'Wybieram numer {self.telefon_s} i dzwonię do {self.imie}, {self.nazwisko}'


def create_contacts():
    contact_type = int(input("Wprowadź typ wizytówki\n 1 - Base\n 2 - Business\n:"))
    x = int(input("Podaj ile wizytówek potrzebujesz "))
    if contact_type == 1:
        for i in range(x):
            contact = BaseContact(imie=fake.first_name(), nazwisko=fake.last_name(), telefon=fake.phone_number(),
                                  email=fake.email())
            print(contact)
    elif contact_type == 2:
        for i in range(x):
            contact = BusinessContact(imie=fake.first_name(), nazwisko=fake.last_name(), telefon=fake.phone_number(),
                                      email=fake.email(), stanowisko=fake.job(), nazwa_firmy=fake.company(),
                                      telefon_s=fake.phone_number())
            print(contact)
    return contact_type, x

create_contacts()