# MongoDB connectie
from pymongo import MongoClient
# Voor de relationele database + PostgreSQL
import psycopg2

# Maak de connectie met Mongo
client = MongoClient()
print(client)                               # MongoClient
print(client.sp_db)                         # Database
print(client.sp_db.products)                # Collectie (i.e. tabel)
print(client.sp_db.products.find_one())     # Eerste product
print(client.sp_db.products.find())         # Hiermee maken we een cursor aan: zie iterable_demo.py

# De volgende stappen zijn voor jou!
# 1. Lees de data uit

# 2. Maak een selectie van de eigenschappen die je nodig hebt.

# 3. Zet de data over naar een relationele database naar keuze.