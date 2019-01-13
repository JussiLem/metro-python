# -*- coding: utf-8 -*
try:
    tiedostonNimi = input("Minkäniminen tiedosto luodaan?: ")
    tiedosto = open(tiedostonNimi, 'w')
    kirjoitus = input("Mitä kirjoitetaan tiedostoon?: ")
    tiedosto.write(kirjoitus)
    print("Luotiin tiedosto", tiedostonNimi, "ja siihen tallennettiin teksti:", kirjoitus)
    tiedosto.close()
except IOError:
    print("Tiedostoa ei löytnyt")
