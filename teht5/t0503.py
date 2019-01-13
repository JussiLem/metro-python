# -*- coding: utf-8 -*
sijainti = "merkkijonoja.txt"

try:
    tiedosto = open(sijainti)
    salasana = tiedosto.readlines()
    for rivi in salasana:
        rivi = rivi.strip()
        if rivi.isalnum():
            print(rivi, "kelpaa salasanaksi.")
        elif not rivi.isalnum():
            print(rivi, "sisältää virheellisiä merkkejä.")
        elif not rivi:
            break
    tiedosto.close()
except IOError:
    print("tiedostoa ei löytnyt")