#############
# Itertools #
#############
import itertools
KLEUREN = ['A', 'B', 'C', 'D', 'E', 'F']

print("Itertools.product is vanbinnen: ")
print(itertools.product(KLEUREN, repeat=4))

# Met list comprehension
#combinaties = [x for x in itertools.product(KLEUREN, repeat=4)]

# Alle combinaties toevoegen zonder list comprehension
# Maak een lege lijst aan voor de combinaties
combinaties = []

# Vraag steeds de volgende combinatie op en voeg deze toe aan de lijst
for x in itertools.product(KLEUREN, repeat=4):
    combinaties.append(x)

#########
# Mongo #
#########

# Om dit voorbeeld te runnen moet je Mongo hebben draaien.
from pymongo import MongoClient
client = MongoClient()

print("De producten in MongoDB worden aangewezen met een cursor")
print(client.sp_db.products.find())

# Producten opslaan met list comprehension
# (Mijn database heet 'sp_db' en mijn collectie met producten heet 'producten')
producten = [product for product in client.sp_db.products.find()]
print(f"Er zijn totaal {len(producten)} producten.")
print("Het eerste product")
print(producten[0])