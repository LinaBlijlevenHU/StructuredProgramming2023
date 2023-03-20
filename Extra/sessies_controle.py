# MongoDB connectie
from pymongo import MongoClient

# Maak de connectie met Mongo
client = MongoClient()

# Houdt de problemen in de sessies bij
buid_missing = 0
buid_error = 0

# Voor alle sessies
for s in client.huwebshop.sessions.find():
    # Bestaat er een BUID?
    if 'buid' in s.keys():
        # Is er slechts één, zodat we correct kunnen koppelen?
        if not len(s['buid']) == 1:
            print(f"Too many BUIDs!: {(s['buid'])}")
            buid_error += 1
    # Geen BUID :(
    else:
        print("BUID missing :(")
        buid_missing += 1

# Print de resultaten
print(f"Missing: {buid_missing}")
print(f"Multiple BUIDS: {buid_error}")