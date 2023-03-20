import pickle

producten = [
    {
        'naam': 'Shampoo',
        'categorie': 'Haarverzorging',
        'prijs': 2.00,
        'sterren': 2
    },
    {
        'naam': 'Conditioner',
        'categorie': 'Haarverzorging',
        'prijs': 3.00,
        'sterren': 4
    },
    {
        'naam': 'Tandpasta',
        'categorie': 'Mondhygiene',
        'prijs': 1.50,
        'sterren': 5
    },
    {
        'naam': 'Ongelukje',
        'categorie': 'Onbekend',
        # Oei geen prijs
        # 'prijs': 2.00
        'sterren': 1
    }
]

def pickle_rick(producten, fname="producten.pickle"):
    # Pickle de producten
    with open(fname, 'wb') as f:
        pickle.dump(producten, f)

def unpickle_rick(fname="producten.pickle"):
    # Unpickle de producten
    with open(fname, 'rb') as f:
        nieuwe_producten = pickle.load(f)
    return nieuwe_producten

pickle_rick(producten)
unpickle_rick()

# Met optioneel argument
#pickle_rick(profielen, 'profielen.pickle')
#unpickle_rick('profielen.pickle')