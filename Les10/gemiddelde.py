import producten_pickle

# Haal de producten op
producten = producten_pickle.unpickle_rick()

# 1. Bereken het gemiddelde, geef de juiste set daarvoor mee.
def gemiddelde(producten, eigenschap='prijs'):
    totaal = 0
    no_producten = len(producten)

    for product in producten:
        if (eigenschap in product.keys()):
            # Geldige prijs, tel op bij de rest
            totaal += product[eigenschap]
        else:
            # Product met ongeldige prijs
            no_producten -= 1

    # Deel de totale prijs door het daadwerkelijke aantal
    # producten dat ook een prijs heeft.
    return totaal / no_producten

print(f"De gemiddelde prijs van producten is: {gemiddelde(producten)}")
print(f"Het gemiddelde aantal sterren dat een product heeft is: {gemiddelde(producten, 'sterren')}")

# 2. Optioneel argument om te filteren.
def juiste_categorie(product, categorie):
    '''
    Is een product van de juiste categorie?
    :param  dict    Het product
    :param  str     De gezochte categorie
    :return bool
    '''
    # Kijken we naar de categorie?
    if (categorie == None):
        return True

    # Kijk eerst of het product een valide categorie heeft.
    if (not 'categorie' in product.keys()):
        return False

    # Check of de categorie matcht
    return product['categorie'] == categorie

def categorie_gemiddelde(producten, categorie=None):
    totaal = 0
    no_producten = len(producten)

    for product in producten:
        if ('prijs' in product.keys() and juiste_categorie(product, categorie)):
            # Geldige prijs, tel op bij de rest
            totaal += product['prijs']
        else:
            # Product met ongeldige prijs
            no_producten -= 1

    # Geen producten? Dan geen gemiddelde
    if (no_producten < 1):
        return 0

    # Deel de totale prijs door het daadwerkelijke aantal
    # producten dat ook een prijs heeft.
    return totaal / no_producten

# Probeer ook eens pandas en de bijhorende .loc methodes voor makkelijke selectie :)
# Tip: leer gratis op Kaggle! https://www.kaggle.com/learn/pandas
haarproducten = [pr for pr in producten if ('categorie' in pr.keys() and pr['categorie'] == "Haarverzorging")]

gem_prijs = categorie_gemiddelde(producten)
gem_prijs_hp = categorie_gemiddelde(producten, 'Haarverzorging')
gem_prijs_hp2 = categorie_gemiddelde(haarproducten)

print(f"Gemiddelde prijs: {gem_prijs}")
print(f"Gemiddelde prijs voor Haarverzorging: {gem_prijs_hp}")
print(f"Gemiddelde prijs voor Haarverzorging: {gem_prijs_hp2}")
