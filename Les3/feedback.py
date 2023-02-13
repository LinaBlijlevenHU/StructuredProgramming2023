import itertools

# Spelinstellingen
KLEUREN = ['A', 'B', 'C', 'D', 'E', 'F']
LENGTE = 3

# Feedbackfunctie uit de klas
def code_feedback(secret, gok):
    goed, bijnagoed = 0, 0

    # Kopieer de codes om te kunnen bewerken
    gok, secret = list(gok).copy(), list(secret).copy()

    # Vervang alle exacte matches door een plusje
    for i in range(LENGTE):
        if secret[i] == gok[i]:
            secret[i], gok[i] = '+', '+'
            goed += 1

    # Als de kleur ergens anders in de code zit telt hij als
    # bijna goed
    for j in range(LENGTE):
        if (gok[j] != '+') and (gok[j] in secret):
            bijnagoed += 1

    return (goed, bijnagoed)

# Damian's versie van de feedbackfunctie
def generate_feedback(combo, gok):
    # Starter feedback if no letters are correct
    feedback = [0, 0]
    # Check every letter in the combination
    for i in range(LENGTE):
         # If the letter is in the right spot
        if combo[i] == gok[i]:
            feedback[0] += 1
            feedback[1] -= 1
        # If the letter is in the wrong spot
        elif combo[i] in gok:
            feedback[1] += 1
    if feedback[1] < 0:
        feedback[1] = 0
    return feedback

# Frequentiefunctie
def freq(lijst):
    f = {}

    for element in lijst:
        # Tel 1 op bij de huidige frequentie van het element (default 0)
        f[element] = f.get(element, 0) + 1

    return f

combinaties = [x for x in itertools.product(KLEUREN, repeat=LENGTE)]
print(len(combinaties))

feedbackAAA = [code_feedback(combi, ['A', 'A', 'A']) for combi in combinaties]
feedbackAAB = [code_feedback(combi, ['A', 'A', 'B']) for combi in combinaties]
feedbackABC = [code_feedback(combi, ['A', 'B', 'C']) for combi in combinaties]

print(freq(feedbackAAA))
print(freq(feedbackAAB))
print(freq(feedbackABC))