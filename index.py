#Voorbereiding, variabeles maken enzo

geheimwoord = "appel"
geraden = 0

galg = 0
foutgeraden = 0;

geradenletters = []
geradenwoord = []

lengte = len(geheimwoord)
for i in range(lengte):
    geradenwoord.append("_")

def voortgang():
    galg()
    print()
    for i in geradenwoord:
        print(i + " ", end='')
    print()
    for i in geradenletters:
        print(i + ", ", end='')
    print()

def galg():
    for i in range(10):
            print("")
    if foutgeraden == 0:
        print("________")
    if foutgeraden == 1:
        for i in range(6):
            print("    |")
        print("__|_____")
    if foutgeraden == 2:
        print(" _________")
        for i in range(6):
            print("  |")
        print("__|_____")
    if foutgeraden == 4:
        print(" _________")
        print("  |/     |")
        print("  |")
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

    if len(geradenletter) > 1 or len(geradenletter) < 0:
        print("Je moet 1 letter opgeven")

         


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

