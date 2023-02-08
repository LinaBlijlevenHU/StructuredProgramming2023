import random

# Kleuren
colours = ['R', 'G', 'B', 'C', 'M', 'Y']
# De kleur om te raden
secret = random.choice(colours)

# Bepaal alle mogelijkheden
possibilities = colours

print(f"Welkom bij het kleurenraadspel! Je kan kiezen uit de kleuren {colours}")

# Eerste gok
guess = input("Raad een kleur: ")

while secret != guess:
    # Check of de kleur valide is
    if (guess in colours):
        # Informeer de gebruiker
        print("Dat is helaas niet goed :(")

        # Verwijder de mogelijkheid uit het lijstje
        possibilities.remove(guess)
        print(f"Je kunt nog kiezen uit de volgende kleuren: {possibilities}")
    else:
        print(f"Dat is geen geldige kleur. Je kan kiezen uit de volgende kleuren: {colours}")

    # Laat de gebruiker opnieuw raden
    guess = input("Raad een kleur: ")

# Informeer de gebruiker
print("Je hebt het goed geraden!")
