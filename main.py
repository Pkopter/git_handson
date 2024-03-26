import json
print("Git Handson")
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
    print("Dane:", Dane)
display(Dane)

f = open("data.json")
aha = json.load(f)
f2 = open("data2.json")
D2 = json.load(f2)
aha.extend(D2)
display(aha)