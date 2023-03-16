'''
Zo moet het wel!

Dit is een file met hulpfuncties voor wiskunde.

@author     Lina Blijleven (lina.blijleven@hu.nl)
@copyright  Hogeschool Utrecht 2023
'''

def tot_de_macht(a, b):
    '''
    Verhef het eerste gegeven getal tot de macht van het tweede
    gegeven getal.

    :param      int|float
    :param      int|float
    :return     int|float
    '''
    return a ** b

# Frequentiefunctie (denk terug aan FA-AI3: Statistiek)
def freq(lijst):
    '''
    Bepaal een dictionary met frequenties voor een gegeven lijst.

    :param  list
    :return dict
    '''
    f = {}
    for element in lijst:
        # Tel 1 op bij de huidige frequentie van het element (default 0)
        f[element] = f.get(element, 0) + 1
    return f