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
print(client.sp_db.products.find())

# Lees de data uit

# Zet de data over