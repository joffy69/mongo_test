import pymongo
import os
from os import path
if path.exists("env.py"):
    import env

MONGODB_URI = os.getenv('MONGODB_URI')
DBS_NAME="MyTestDB"
COLLECTION_NAME="MyFirstMD"

def mongo_connect(url): 
    
    try:
        conn = pymongo.MongoClient(url)
        print("MONGO is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("NO MONGO: %s") %e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]



coll.remove({'first': 'douglas'})

documents = coll.find()

for doc in documents:
    print (doc)