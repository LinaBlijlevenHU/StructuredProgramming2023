import itertools

# Spelinstellingen
KLEUREN = ['A', 'B', 'C', 'D', 'E', 'F']
LENGTE = 4

def feedback(code, pegs):
    '''
    Returns a tuple with the number of correct guesses (black) and the
    number of correct colors but wrong positions (white)

    Source: https://github.com/peterstark72/mastermind/blob/master/mastermind.py
    :param  tuple   The code, e.g. (1,2,3,4)
    :param  tuple   The guess, e.g. (1,1,1,1)
    :return tuple   The feedback (black, white) or (correct, correct/wrong position)

    Example:
    The code (1,2,3,4) and guess (1,1,1,1), will return (1,0) since only the first peg is correct.
    '''

    # Bepaal een set van alle indices bijv. (0, 1, 2, 3)
    positions = set(range(len(code)))

    # Bepaal de posities waar de pinnen al op de goede plek staan.
    black_positions = set(
        [pos for pos, peg in enumerate(pegs) if peg == code[pos]])
    # Bepaal hoeveel pinnen al goed staan.
    blacks = len(black_positions)

    # Vergelijk de sets met indices om te kijken welke pinnetjes nog over zijn
    remains_pos = positions - black_positions
    # Selecteer de onderdelen van de code die nog over zijn
    remains = [code[pos] for pos in remains_pos]

    # Teller voor correcte kleur/verkeerde positie pinnetjes
    whites = 0
    # Set van kleuren waar al witte pinnetjes voor uitgedeeld zijn
    awarded_duplicates = set()
    # Voor elke index van een overgebleven pin
    for pos in remains_pos:
        # Bepaal de kleur
        color = pegs[pos]
        # Staat de kleur verderop in de code? Én zijn er minder of even veel van deze kleur in
        # de overgebleven code en de geheime code.
        if color in remains and pegs.count(color) <= code.count(color):
            # Voeg een witte pin toe
            whites += 1
        # Als anders de kleur verderop in de code staat en de kleur nog niet in
        elif color in remains and color not in awarded_duplicates:
            # Voeg een witte pin toe
            whites += 1
            # We kunnen verder geen witte pinnen meer toevoegen voor deze kleur
            awarded_duplicates.add(color)

    # Geef het resultaat terug als tuple
    return blacks, whites

# Frequentiefunctie
def freq(lijst):
    f = {}

    for element in lijst:
        # Tel 1 op bij de huidige frequentie van het element (default 0)
        f[element] = f.get(element, 0) + 1

    return f

combinaties = [x for x in itertools.product(KLEUREN, repeat=LENGTE)]
print(len(combinaties))

feedback1 = [feedback(combi, ['A', 'A', 'A', 'A']) for combi in combinaties]
feedback2 = [feedback(combi, ['A', 'A', 'A', 'B']) for combi in combinaties]
feedback3 = [feedback(combi, ['A', 'A', 'B', 'C']) for combi in combinaties]

print(freq(feedback1))
print(freq(feedback2))
print(freq(feedback3))