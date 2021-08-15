import pandas as pd
import random

df = pd.read_csv('pitanjaSve.csv', sep=",")
listaImenik = df.to_dict('records')
random.shuffle(listaImenik)
brOdg = 0
novaLista = []
brojacPitanja = 1
tacni = 0
brojPitanja = int(input("Unesite broj pitanja: "))  # max 83
br2 = brojPitanja
for i in listaImenik:
    l = list(i.items())
    random.shuffle(l)
    d = dict(l)
    novaLista.append(d)

samoPitanje = {}
samoOdgovor = {}
josNovijaLista = []
for i in novaLista:
    # print(i)
    for key, value in i.items():
        if key == "Pitanje":
            samoPitanje["Pitanje"] = value
        else:
            samoOdgovor[key] = value
    # print(samoPitanje,samoOdgovor)
    samoPitanje.update(samoOdgovor)
    # print(samoPitanje)
    josNovijaLista.append(samoPitanje)

    samoPitanje = {}
    samoOdgovor = {}

# print(josNovijaLista)
tacniOdgovori = []
for i in josNovijaLista:
    brOdg = 0
    for key, value in i.items():
        if brOdg == 0:
            print("{}. Pitanje: {}".format(brojacPitanja, value))
            brojacPitanja += 1
            brOdg += 1
        else:
            if type(value) != float:
                print("{}: {}".format(brOdg, (value.replace('*', '', 1))))
                if '*' in value:
                    tacniOdgovori.append(brOdg)
                brOdg += 1
    # print(tacniOdgovori)
    while True:
        try:
            korisnik = int(input("Unesite odgovor: "))
            break
        except ValueError:
            print("Unos nije int, probajte ponovo. ", end='')
            korisnik = 7
    unosi = []
    for digit in str(korisnik):
        unosi.append(int(digit))
    # print(unosi)
    tacniOdgovori.sort()
    unosi.sort()
    if tacniOdgovori == unosi:
        print("Tacno!")
        print("--------------------------------\n")
        tacni += 1
    else:
        print("*******NETACNO!!!!!********   Odgovor je: {}!!!!!!!!!".format(tacniOdgovori))
        print("--------------------------------*******NETACNO!!!!!********   Odgovor je: {}!!!!!!!!!\n".format(
            tacniOdgovori))
    tacniOdgovori = []
    brojPitanja -= 1
    if brojPitanja == 0:
        print("Prosek: {} od {}, znaci {}%".format(tacni, br2, tacni / br2 * 100))
        break
