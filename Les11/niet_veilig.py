from pymongo import MongoClient

client = MongoClient(
    'port'=27017,
    'host': 127.0.0.1,
    'database': "huwebshop",
    'password': "EenSuperGeheimWachtwoord"
)