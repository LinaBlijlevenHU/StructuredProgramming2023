def evaluate(guess, secret):
    '''
    De functie zoals beschreven in de slides van Canvas. Deze is aangepast om uiteindelijk een tuple 
    terug te geven i.p.v. een lijst.
    
    Let op! De tweede parameter moet een lijst zijn, geen tuple. Je kan altijd casten met list(variabele).
    
    :param      list    Eerste code
    :param      list    Tweede code (volgorde wisselen maakt niet uit)
    :return:    tuple   (Zwart, wit)
    '''
   black, white = 0, 0
   used = []
   # The black pins
   for position in range(len(guess)):
        if guess[position] == secret[position]:
            black += 1
            used.append(position)
   # the white pins
   secretCopy = secret[::]
   for position in used:
       secretCopy.remove(secret[position])
   for i in range(len(guess)):
       if i not in used:
           if guess[i] in secretCopy:
               white += 1
               secretCopy.remove(guess[i])
   return (black, white)                        # Geef terug als tuple.