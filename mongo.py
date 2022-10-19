from pydoc import cli
from pymongo import MongoClient
import pprint

client = None
db= None
tutorial= None


def init_co():
    global client,db, tutorial
    client = MongoClient(host="localhost", port=27017)
    #client = MongoClient("mongodb://localhost:27017")
    #client = MongoClient()
    db = client.rptutorials
    tutorial = db.tutorial

def ajoutBDD(tweet):
    global client,db, tutorial
    tutorial.insert_one(tweet)

def ferme_db():
    global client,db, tutorial
    client.close()

def returnCollection():
    global client,db, tutorial
    #sans argument, find retourne toute la collection
    for doc in tutorial.find():
        pprint.pprint(doc)
    return tutorial.find()

def retourne_une_date(date):
    global client,db, tutorial
    #recherche sur un champs
    jon_tutorial = tutorial.find_one("created_at{$gte:ISODate("+str(date)+"}")
    pprint.pprint(jon_tutorial)
    return jon_tutorial



init_co()
print(retourne_une_date("2022-10-18"))
ferme_db()