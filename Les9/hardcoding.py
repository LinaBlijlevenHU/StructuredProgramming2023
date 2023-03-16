import itertools, random
# Leen de frequentiefunctie uit de wiskundemodule
from wiskunde import freq

KLEUREN = ['R', 'G', 'B', 'Y']
LENGTE = 4

# Functie met hardcoding :(
def vraag_gok(mogelijkheden):
    '''
    Kies een gok uit de lijst met mogelijkheden.
    (Dit geeft eigenlijk altijd hetzelfde antwoord omdat we niet reduceren)

    :param      lijst   Lijst met tuple combinaties die nog over zijn
    :return     tuple   Onze gok
    '''
    # We willen een gok met patroon AABB teruggeven,
    # maar door hardcoden raden we altijd dezelfde code of gokken we
    # willekeurig.
    if ('R', 'R', 'G', 'G') in mogelijkheden:
        return ('R', 'R', 'G', 'G')

    # Geef een random gok terug als we niets beters hebben.
    return random.choice(mogelijkheden)

combinaties = [x for x in itertools.product(KLEUREN, repeat=LENGTE)]
print(f"Onze gok met hardcoding is {vraag_gok(combinaties)}")

# Patronen met AABB (bijv.):
# RRGG
# RGRG
# YYBB
# YBBY

# We krijgen altijd dezelfde gok. Hoe kunnen we dit oplossen?
# 1. Stel een lijst op van AABB patronen en vindt er een die nog niet gebruikt is.
# 2. Loop door de lijst van mogelijkheden en geef een code terug die aan het patroon matcht (of random).
# (Nummer 2 is veel makkelijker, dus laten we dat maar doen.)

# We hebben eerst een hulpfunctie nodig om te kijken of een code
# een specifiek patroon matcht.
# bijv: is RRGG van de vorm AABB?
def matcht_patroon(code, patroon):
    '''
    Matcht een code een bepaald patroon voor Mastermind?

    :param  tuple
    :param  tuple
    :return bool
    '''
    code_freq = freq(code)
    patroon_freq = freq(patroon)
    return sorted(code_freq.values()) == sorted(patroon_freq.values())

# Tests voor mijn functie.
#print(matcht_patroon(('R', 'B', 'G', 'R'), ('A', 'A', 'B', 'B')))    # matcht niet: False
#print(matcht_patroon(('R', 'G', 'G', 'R'), ('A', 'A', 'B', 'B')))    # matcht wel: True

def nieuwe_gok(mogelijkheden):
    '''
    Kies een gok uit de lijst met mogelijkheden.
    (Dit geeft eigenlijk altijd hetzelfde antwoord omdat we niet reduceren)

    :param      lijst   Lijst met tuple combinaties die nog over zijn
    :return     tuple   Onze gok
    '''
    # Shuffle onze mogelijkheden (zodat we wat verschillende codes kunnen krijgen,
    # we gebruiken geen reduce in dit voorbeeld)
    random.shuffle(mogelijkheden)

    # Bekijk onze overgebleven mogelijkheden
    for code in mogelijkheden:
        # We gokken in de vorm AABB in de hoop op goede resultaten :)
        if matcht_patroon(code, ('A', 'A', 'B', 'B')):
            return code

    # Geef een random gok terug
    return random.choice(mogelijkheden)

# Test onze nieuwe methode om een gok op te vragen
print(f"Onze nieuwe eerste gok is: {nieuwe_gok(combinaties)}")

# Nadeel: deze heuristiek werkt uiteindelijk alleen met een code van lengte 4.
# Om dit uit te breiden moet je patronen kunnen genereren voor codes van verschillende lengtes.