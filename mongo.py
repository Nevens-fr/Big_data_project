from pydoc import cli
from pymongo import MongoClient
import pprint
import Tweet

client = None
db= None
tutorial= None


def init_co():
    global client,db, tutorial
    client = MongoClient(host="mongodb+srv://ThomasAurelienAxel:ThomasAurelienAxel@jouetclubcluster.eujzfbg.mongodb.net/")
    #client = MongoClient("mongodb://localhost:27017")
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

# recherche si plusieurs tweets identiques existent dans la bdd
def check_si_tweet_existe2(id_t, id_u):
    jon_tutorial = tutorial.find({"id": id_t, "user" : id_u})
    print(len(jon_tutorial))
    exit(1)
    return jon_tutorial != None

def delete_id(id):
    tutorial.delete_one({"_id" : id})


def updateby_id(id, tweet):
    tutorial.update_one({"_id" : id}, {"$set" :tweet}, upsert = True)

def update_add_field(id, field, value):
    tutorial.update_one({"_id" : id}, {"$set" :{field : value}})


def mise_a_jour_default():
    init_co()
    base = returnCollection()

    for a in base:
        tmp = Tweet.Tweet("","","","","","")
        tmp.readData(a)
        update_add_field(a["_id"], "sentiment", tmp.sentiment)

    ferme_db()

#parcours la base et supprime tout !!!!!
def parcours():
    for a in base:
        tmp = Tweet.Tweet("","","","","","")
        tmp.readData(a)
        if check_si_tweet_existe(tmp.id, tmp.user):
            delete_id(tmp.mid)
            return 0
    return 1

#vide la base
def suppressions():
    init_co()
    base = returnCollection()
    i = 0
    while parcours() == 0:
        i+=1
        
    print(i)
    ferme_db()


#mise à jour des formats de dates
def mise_a_jour_date():
    init_co()
    base = returnCollection()

    for a in base:
        tmp = Tweet.Tweet("","","","","","")
        tmp.readData(a)
        if(" " in str(tmp.created_at)):
            print(tmp.created_at)
            a["created_at"] = str(tmp.created_at).split(" 00:00:00", 1)[0]
            updateby_id(a["_id"], a)

    ferme_db()