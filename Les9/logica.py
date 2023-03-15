'''
Zo moet het wel!

Dit is een file met hulpfuncties voor logica.

@author     Lina Blijleven (lina.blijleven@hu.nl)
@copyright  Hogeschool Utrecht 2023
'''

def and_functie(conditie1, conditie2):
    '''
    Bekijk de uitkomst van twee eisen en kijk
    of we aan de voorwaarden voldoen.

    :param  bool    Eis #1
    :param  bool    Eis #2
    :return bool    Voldoen we aan beide?
    '''
    return conditie1 and conditie2

def or_functie(conditie1, conditie2):
    '''
    Bekijk de uitkomst van twee eisen en kijk
    of we aan _een_ voorwaarde voldoen.

    :param  bool    Eis #1
    :param  bool    Eis #2
    :return bool    Voldoen we aan een voorwaarde?
    '''
    return conditie1 or conditie2

# Zijn de condities waar? (Hier zou je waarschijnlijk een
# andere functie aanroepen)
conditie1, conditie2 = True, False

# Zijn ze beide waar?
if and_functie(conditie1, conditie2):
    print("We voldoen aan de eisen!")
# Is een van de twee waar?
elif or_functie(conditie1, conditie2):
    print("We voldoen aan 1/2 eisen.")