# -*- coding: utf-8 -*
sijainti = "faktat.txt"
lisattavaTeksti = "Aenean convallis erat."
try:
    tiedosto = open(sijainti, 'r')
    luettuTeksti = tiedosto.read()
    print("Tiedostosta luettiin teksti: ", luettuTeksti)
    tiedosto.close()
except IOError:
    print("Tiedostoa ei löytnyt")
