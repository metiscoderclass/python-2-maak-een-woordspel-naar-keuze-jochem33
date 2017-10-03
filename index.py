#Voorbereiding, variabeles maken enzo

import time
from random import randint

geheimwoorden = []

print("Welkom Bij Galgje")
print("")
print("Om het hele woord te raden: raad eerst een vraagteken")
print("")
moeilijk = input("Wil je een makkelijk, normaal of moeilijk woord? (1, 2 of 3): ")
if moeilijk == "1":
    geheimwoorden = ["bot", "ijs", "hoi", "hark"]
elif moeilijk == "2":
    geheimwoorden = ["eten", "appel", "laptop", "binair"]
elif moeilijk == "3":
    geheimwoorden = ["computer", "blauw", "geel", "comuterarchitectuur"]


geheimwoord = geheimwoorden[randint(0, 2)]
geraden = False

alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

galg = 0
foutgeraden = 0

geradenletters = []
geradenwoord = []

lettersgeraden = 0

added = 0

eenlettergoed = 0

lengte = len(geheimwoord)
for i in range(lengte):
    geradenwoord.append("_")

def voortgang():
    galg()
    print()
    for i in geradenwoord:
        print(i + " ", end='')
    print("")
    print("")
    for i in geradenletters:
        print(i + ", ", end='')
    print("")
    print("")

def galg():
    for i in range(10):
            print("")
    if foutgeraden == 0:
        print("________")
    if foutgeraden == 1:
        for i in range(6):
            print("  |")
        print("__|_____")
    if foutgeraden == 2:
        print(" _________")
        for i in range(6):
            print("  |")
        print("__|_____")
    if foutgeraden == 3:
        print(" _________")
        print("  |/     |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("__|_____")
    if foutgeraden == 4:
        print(" _________")
        print("  |/     |")
        print("  |     ( )")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("__|_____")
    if foutgeraden == 5:
        print(" _________")
        print("  |/     |")
        print("  |     ( )")
        print("  |     /|\ ")
        print("  |     / \ ")
        print("  |")
        print("  |")
        print("__|_____")

#while niet geraden Loop:
while geraden == False: # while not geraden
    voortgang() #Print voorgang: galg, streepjes en al geraden letters
    geradenletter = input("Raad een Letter: ") #Vraag om een letter

    # onderstaande kan ook in een switch case maar die bestaan niet in python
    if geradenletter == "?": #if om het hele woord te raden
        raadwoord = input("raad het hele woord: ")
        if not len(raadwoord) == lengte:
            print("De lengte komt niet overeen met het geheime woord")
        elif raadwoord == geheimwoord:
            break
        else:
            print("Dat is niet goed, ga verder met letters raden of probeer het opnieuw!")
        time.sleep(1)

    elif len(geradenletter) == 0: # ifjes om te zorgen dat er geen leesteken, cijfers, hoofdletters en niet meer of minder dan 1 letter opgeeft
        print("Je moet 1 letter opgeven")
        time.sleep(1)
    elif len(geradenletter) > 1:
        print("Je mag maar 1 letter opgeven")
        time.sleep(1)
    elif not geradenletter in alfabet:
        print("Je mag alleen letters zeggen, geen leesteken, hoofdletters, cijfers e.d.")
        time.sleep(1)
    elif geradenletter in geradenletters:
        print("je mag geen letter zeggen die je al hebt geraden")
        time.sleep(1)

    else: #als je wel een letter hebt ingetypt
        for i in range(lengte): #loop door de letters opzoek naar goede letter
            if geradenletter == geheimwoord[i]:
                print("Je hebt de letter " + geradenletter + " geraden")
                geradenwoord[i] = geradenletter #vervangt het streepje voor de (goed) geraden letter
                if added == 0: #zorgt dat (als de letter 2 keer in het woord zit) hij niet twee keer in geradenletters komt
                    geradenletters.append(geradenletter) #zet de letter in de geradenletters
                lettersgeraden = lettersgeraden + 1
                added = 1
                eenlettergoed = True #zegt dat er een letter is geraden
        if lettersgeraden == lengte: #als je evenveel letters hebt geraden als de lengte van het woord dan heb je het geraden
            geraden = True

        if eenlettergoed == False: # als je geen letter hebt geraden
            if added == 0:
                geradenletters.append(geradenletter)
            added = 1
            foutgeraden += 1
            if foutgeraden == 5:
                voortgang()
                break
        added = 0
        eenlettergoed = 0

print("")
if foutgeraden == 5:
    print("Hellaas! Je hebt verloren, het geheime woord was " + geheimwoord)
else:
    print("Je hebt gewonnen!! Het geheime woord was inderdaad " + geheimwoord + " !")
'''
    if letter is ?
        print: raad een woord
        if geraden woord = geheim woord
            Je hebt het goed geraden!
            Break
        else
            print je hebt het niet goed, ga verder met raden

    if twee letters
        print je hebt twee letters geraden, dat mag niet, probeer het opnieuw!

    elif letter in geraden letters:
        print: je hebt deze letter al geraden

    elif letter is in het woord:
        print goed geraden!
        werk voortgang bij: zet de letter op de streepjes
        if woord is af
            break

    if letter is niet in woord:
        print dat is niet goed
        werk voortgang bij: zet letter bij geraden en bouw de galg verder op


if geraden
    print Gefeliciteerd, je hebt het woord geraden!
else
    print je heb het helaas niet geraden, het woord was: geheim woord

'''

