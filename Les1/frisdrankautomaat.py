# Producten toevoegen

# Betaalsoorten, van groot naar klein
MUNTSOORTEN = [200, 100, 50, 20, 10, 5, 2, 1]

def betaal_wisselgeld(wisselgeld):    
    # Betaal elke munt uit
    for munt in MUNTSOORTEN:
        # Bereken het aantal munten dat we uit kunnen betalen
        aantal = wisselgeld // munt

        # Bereken het restbedrag 
        wisselgeld = wisselgeld % munt

        # Print het aantal munten voor de gebruiker
        print(f"Je krijgt {aantal} muntjes van {munt} cent.")

def regel_wisselgeld(betaald, prijs):
    print(f"Uw product kost {prijs} eurocent en u heeft {betaald} eurocent betaald.")
    # Bereken het wisselgeld in eurocent
    wisselgeld = betaald - prijs

    # Te veel betaald?
    if (wisselgeld > 0):
        betaal_wisselgeld(wisselgeld)
    # Precies genoeg betaald
    elif (wisselgeld == 0):
        print(f"Je hebt gepast betaald. Geniet van je aankoop!")
    # Te weinig betaald
    else:
        print(f"Je hebt nog niet genoeg geld ingeworpen. Betaalt u a.u.b. nog {abs(wisselgeld)} cent.")
        betaald += int(input("Hoeveel heeft u ingeworpen (in eurocent)? "))
        print(f"Er is nu totaal {betaald} cent betaald.")
        regel_wisselgeld(betaald, prijs)

def main():
    # Input van de gebruiker
    prijs = int(input("Wat is de prijs van het product (in eurocent)? "))
    optie = int(input("Wilt u contact betalen? Druk dan op 1. Wilt u pinnen? Druk dan op 2. "))

    # Contant betalen
    if (optie == 1):
        betaald = int(input("Hoeveel cent heb je ingeworpen? "))
        regel_wisselgeld(betaald, prijs)
    # Betalen met de pinpas
    else:
        print(f"U kunt nu betalen bij de terminal. Bedankt voor uw aankoop!")

# Voer de code alleen uit als we dit script zelf uitvoeren (dus niet bij importeren)
if __name__ == "__main__":
    main()