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
    client = MongoClient(host="mongodb+srv://ThomasAurelienAxel:ThomasAurelienAxel@jouetclubcluster.eujzfbg.mongodb.net/")
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
"""
init_co()
#print(retourne_une_date("2022-10-18"))
base = returnCollection()

for a in base:
    tmp = Tweet.Tweet("","","","","","")
    tmp.readData(a)
    #tmp.created_at = str(tmp.created_at).split(" ",1)[0] #enlève les h:mm:ss
    #a["created_at"] = datetime.datetime.strptime(str(tmp.created_at), '%Y-%m-%d')
    #print(a)
    update_add_field(a["_id"], "sentiment", tmp.sentiment)

#check_si_tweet_existe("1582521102420484096","1296633273909641216")
#retourne_un_pour_date(datetime.datetime.strptime("2022-10-20", '%Y-%m-%d'))
#retourne_entre_date(datetime.datetime.strptime("2022-10-15", '%Y-%m-%d'),datetime.datetime.strptime("2022-10-16", '%Y-%m-%d'))
ferme_db()
"""

"""

def parcours():
    for a in base:
        tmp = Tweet.Tweet("","","","","","")
        tmp.readData(a)
        if check_si_tweet_existe(tmp.id, tmp.user):
            #print(a)
            delete_id(tmp.mid)
            return 0
    return 1

init_co()
#print(retourne_une_date("2022-10-18"))
base = returnCollection()
i = 0
while parcours() == 0:
    i+=1
    
    #tmp.created_at = str(tmp.created_at).split(" ",1)[0] #enlève les h:mm:ss
    #a["created_at"] = datetime.datetime.strptime(str(tmp.created_at), '%Y-%m-%d')
    #print(a)
    #updateby_id(a["_id"], a)
print(i)
#check_si_tweet_existe("1582521102420484096","1296633273909641216")
#retourne_un_pour_date(datetime.datetime.strptime("2022-10-20", '%Y-%m-%d'))
#retourne_entre_date(datetime.datetime.strptime("2022-10-15", '%Y-%m-%d'),datetime.datetime.strptime("2022-10-16", '%Y-%m-%d'))
ferme_db()
"""