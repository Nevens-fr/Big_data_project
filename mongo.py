from pydoc import cli
from pymongo import MongoClient
import pprint
import Tweet
import datetime

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
    return tutorial.find()

def retourne_un_pour_date(date):
    global client,db, tutorial
    #recherche sur un champs
    #jon_tutorial = tutorial.find_one("created_at{$gte:ISODate("+str(date)+"}")
    jon_tutorial = tutorial.find_one({"created_at": date})

def retourne_entre_date(date, date2):
    jon_tutorial = tutorial.find_one({"created_at": {"$gte": date, "$lte" : date2}})

    pprint.pprint(jon_tutorial)
    return jon_tutorial


def check_si_tweet_existe(id_t, id_u):
    jon_tutorial = tutorial.find_one({"id": id_t, "user" : id_u})
    return jon_tutorial != None



def updateby_id(id, tweet):
    tutorial.update_one({"_id" : id}, {"$set" :tweet}, upsert = True)


"""
init_co()
#print(retourne_une_date("2022-10-18"))
base = returnCollection()

for a in base:
    tmp = Tweet.Tweet("","","","","","")
    tmp.readData(a)
    #tmp.created_at = str(tmp.created_at).split(" ",1)[0] #enlève les h:mm:ss
    a["created_at"] = datetime.datetime.strptime(str(tmp.created_at), '%Y-%m-%d')
    print(a)
    updateby_id(a["_id"], a)

#check_si_tweet_existe("1582521102420484096","1296633273909641216")
#retourne_un_pour_date(datetime.datetime.strptime("2022-10-20", '%Y-%m-%d'))
#retourne_entre_date(datetime.datetime.strptime("2022-10-15", '%Y-%m-%d'),datetime.datetime.strptime("2022-10-16", '%Y-%m-%d'))
ferme_db()
"""