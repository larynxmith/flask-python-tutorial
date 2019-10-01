from pymongo import MongoClient
import os
mongo_client = os.environ.get(
    'MONGO_URI', default='mongodb://localhost:27017')

client = MongoClient(mongo_client)
db = client['loopy-things']
