import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Lees de configuratie
load_dotenv()

# Maak connectie met gebruik van je eigen configuratie
client = MongoClient(
    password=os.getenv('PASSWORD')
)