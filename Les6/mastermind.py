# Importeren van libraries (standaard geinstalleerd)
import random
import itertools

# Importeren van onze eigen functies uit andere files
import ai
import gebruiker_input

# Globale variabelen voor de spelinstellingen
LENGTE = 4
KLEUREN = ['A', 'B', 'C', 'D', 'E', 'F']
# Bepaal het aantal gokken dat de gebruiker krijgt met de RickRegel
MAX_GUESSES = LENGTE + len(KLEUREN)
# Genereer alle combinaties (zodat we dit niet elke keer spelen opnieuw hoeven te doen)
PERMUTATIES = [code for code in itertools.product(KLEUREN, repeat=LENGTE)]

def geldige_gok(guess):
    '''
    Bepaal of de gok geldig is
    :param  None|string
    :return boolean
    '''
    # Hebben we een gok van de juiste lengte?
    if (guess == None):
        return False

    if (len(guess) != LENGTE):
        print("Je code heeft niet de juiste lengte.")
        return False

    # Bevat de gok alleen kleuren die voor mogen komen?
    for pin in guess:
        # Als de kleur niet in de toegestane kleuren zit, weten we al dat de code ongeldig is.
        if pin not in KLEUREN:
            print(f"De kleur {pin} is niet geldig. Je kunt kiezen uit {KLEUREN}.")
            return False

    # Alles in orde, de gok is geldig
    return True

def evalueer(gok, geheime_code):
   '''
   Evalueert een gok tegen een geheime code. Er wordt feedback teruggegeven.
   Deze bestaat uit zwarte en witte pinnen, waarbij zwart de juiste kleur op
   de juiste plek is. De witte pinnetjes zijn de juiste kleur op de verkeerde plek.

   :param   tuple
   :param   tuple
   :return  tuple   De feedback voor de gok in de vorm (zwart, wit)
   '''
   zwart, wit = 0, 0
   gebruikt = []

   # Ken de zwarte pinnetjes toe
   for positie in range(len(gok)):
        # Voor zwarte pinnetjes willen we een exacte match
        if gok[positie] == geheime_code[positie]:
            zwart += 1
            gebruikt.append(positie)

   # Maak een kopie
   geheim_kopie = list(geheime_code).copy()
   # Verwijder de posities die we al gebruikt hebben voor zwarte pinnen
   for position in gebruikt:
       geheim_kopie.remove(geheime_code[position])

   # Ken de witte pinnetjes toe
   for i in range(len(gok)):
       # Voor witte pinnetjes moet de kleur voorkomen, maar niet al een zwart pinnetje hebben gekregen.
       if i not in gebruikt:
           if gok[i] in geheim_kopie:
               wit += 1
               geheim_kopie.remove(gok[i])
   return (zwart, wit)

def reduceer(mogelijkheden, vorige_gok, fb):
    '''
    Bepaal de mogelijkheden die nog over zijn na de laatste gok.

    :param array    Mogelijkheden die er nu nog zijn
    :param tuple    Vorige gok
    :param tuple    Feedback (zwart, wit)
    :return:
    '''
    nieuwe_mogelijkheden = []

    # Test voor elke mogelijkheid of die nog steeds mogelijk is
    for code in mogelijkheden:
        # Bepaal de feedback tussen de vorige gok en de mogelijkheid
        # en vergelijk met de vorige feedback die we hebben gekregen
        if fb == evalueer(code, vorige_gok):
            # Code is nog mogelijk
            nieuwe_mogelijkheden.append(code)

    # Geef de nieuwe mogelijkheden terug
    return nieuwe_mogelijkheden

def vraag_input():
    '''
    Vraag de gebruiker om input
    :return:    tuple  De geraden code
    '''
    # We beginnen met een lege gok
    guess = None

    # We vragen codes tot we een geldige gok hebben
    while not geldige_gok(guess):
        print(f"Je kan kiezen uit de volgende kleuren: {KLEUREN}")

        # Kies een permutatie om als voorbeeld te gebruiken.
        voorbeeld = ''.join(random.choice(PERMUTATIES))
        user_input = input(f"Raad een code (bijv. {voorbeeld}): ")

        # Zet de gok om naar een tuple
        guess = tuple(list(user_input))

    return guess

def main():
    '''
    De main game functie (speelt één spel)
    '''
    print(f"Welkom bij Mastermind! Je kan kiezen uit de kleuren {KLEUREN}")

    # Kies een geheime combinatie
    secret = random.choice(PERMUTATIES)
    print(secret)

    # Bepaal alle mogelijkheden
    mogelijkheden = PERMUTATIES.copy()

    # We beginnen met een foute code om de loop in te gaan
    #guess = vraag_input()
    # Kan bijvoorbeeld vervangen worden door een vraag aan de AI
    guess = ai.vraag_gok(mogelijkheden)

    # Het aantal keer dat we geraden hebben
    aantal_gokken = 1

    # Main game loop
    while secret != guess and aantal_gokken < MAX_GUESSES:
        # Informeer de gebruiker
        print(f"De code {guess} is helaas niet goed :(")
        print(f"Je hebt nog {MAX_GUESSES - aantal_gokken} pogingen.")

        # Feedback
        zwart, wit = evalueer(guess, secret)
        print(f"Er staan nu {zwart} pinnetjes op de juiste plek. {wit} pinnetje(s) hebben de juiste kleur, maar de verkeerde plek.")

        # Bepaal welke mogelijkheden nog over zijn
        mogelijkheden = reduceer(mogelijkheden, guess, (zwart, wit))
        print(f"Er zijn nu nog {len(mogelijkheden)} mogelijkheden over.")

        # Laat de gebruiker opnieuw raden
        #guess = vraag_input()
        # Kan bijvoorbeeld vervangen worden door een vraag aan de AI
        guess = ai.vraag_gok(mogelijkheden)

        # Voeg een poging toe
        aantal_gokken += 1

    # Heeft de gebruiker gewonnen?
    if (secret == guess):
        print(f"Je hebt het goed geraden in {aantal_gokken} keer!")
    else:
        print("Sorry! Je hebt de code niet geraden.")

    # Laat de gebruiker opnieuw spelen
    if (gebruiker_input.ja_nee_vraag("Wil je opnieuw spelen?")):
        main()

# Zorg dat het spel alleen runt als we dit specifieke script runnen
if __name__ == "__main__":
    main()