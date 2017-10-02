#Voorbereiding, variabeles maken enzo

import time

print("Welkom Bij Galgje")
print("")
print("Om het hele woord te raden: raad eerst een vraagteken")

geheimwoord = "derrie"
geraden = 0

alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

galg = 0
foutgeraden = 0;

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
while geraden == 0:
    voortgang()
    geradenletter = input("Raad een Letter: ")

    if geradenletter == "?":
        raadwoord = input("raad het hele woord: ")
        if not len(raadwoord) == lengte:
            print("De lengte komt niet overeen met het geheime woord")
        elif raadwoord == geheimwoord:
            break
        else:
            print("Dat is niet goed, ga verder met letters raden of probeer het opnieuw!")
        time.sleep(1)
    elif len(geradenletter) == 0:
        print("Je moet 1 letter opgeven")
        time.sleep(1)
    elif len(geradenletter) > 1:
        print("Je mag maar 1 letter opgeven")
        time.sleep(1)
    elif not geradenletter in alfabet:
        print("Je mag alleen letter zeggen, geen leesteken, hoofdletters, cijfers e.d.")
        time.sleep(1)
    elif geradenletter in geradenletters:
        print("je mag geen letter zeggen die je al hebt geraden")
        time.sleep(1)
    else:
        for i in range(lengte):
            if geradenletter == geheimwoord[i]:
                print("Je hebt de letter " + geradenletter + " geraden")
                geradenwoord[i] = geradenletter
                if added == 0:
                    geradenletters.append(geradenletter)
                lettersgeraden = lettersgeraden + 1
                added = 1
                eenlettergoed = 1
        if lettersgeraden == lengte:
            geraden = 1

        if eenlettergoed == 0:
            if added == 0:
                geradenletters.append(geradenletter)
            added = 1
            foutgeraden = foutgeraden + 1
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

    Print voorgang: galg, streepjes en al geraden letters

    Vraag om een letter

    # onderstaande kan ook in een switch case

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

