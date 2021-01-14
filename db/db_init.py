__author__ = 'mmalca'

import pymongo
##from db import db_add_ingredients
def init_db():
    mongo_server = pymongo.MongoClient("mongodb://193.106.55.98:5000/")

    #use DB
    db = mongo_server["RecipeForMe"]
    return db

def init_collection(collection_name):
    #Connect to the DB
    mongo_server = pymongo.MongoClient("mongodb://193.106.55.98:5000/")

    #use DB
    db = mongo_server["RecipeForMe"]

    #specific collection name
    collection = db[collection_name]

    return collection