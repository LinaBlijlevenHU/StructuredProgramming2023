import itertools

KLEUREN = ['R', 'G', 'B', 'Y']
LENGTE = 3

permutaties = [code for code in itertools.product(KLEUREN, repeat=LENGTE)]
print(permutaties)
print(len(permutaties))

