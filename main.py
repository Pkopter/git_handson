from pprint import pprint
DATA = [
    {
        "imie": "Kacper",
        "gatunek": "Homo sapiens",
        "waga": 90,
        "wiek": 19.5
    },
    {
        "imie": "Uszatek",
        "gatunek": "mis",
        "waga": 40,
        "wiek": 60
    },
    {
        "imie": "Reksio",
        "gatunek": "pies",
        "waga": 6,
        "wiek": 10,
    },
]
Dane = DATA
def display(Dane):
    pprint("Dane:", Dane)
display(Dane)
