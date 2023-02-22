ANTWOORDEN_JA = ['ja', 'j', 'yes', 'y', 'oke', 'okay', 'okidoki']
ANTWOORDEN_NEE = ['nee', 'n', 'no', 'nada', 'null', 'nope']

def schoon_op(antwoord):
    '''
    Schoon een stukje tekst op

    :param  string
    :return string
    '''
    return antwoord.strip(' ,.;').lower()

def ja_nee_vraag(vraag):
    '''
    Stel de gebruiker een ja of nee vraag.

    :param   string     De vraag om aan de gebruiker te stellen
    :return: boolean    True/False
    '''
    antwoord = None

    # Blijf vragen tot we een bruikbaar antwoord hebben
    while not (antwoord in ANTWOORDEN_JA or antwoord in ANTWOORDEN_NEE):
        # Stel de vraag aan de gebruiker
        print(vraag)
        # Geef de gebruiker de mogelijkheid om opnieuw te spelen
        antwoord = schoon_op(input("Typ ja of nee: "))

    return antwoord in ANTWOORDEN_JA