from pymongo import MongoClient
import pprint


#Connection à mongoDB
#client = MongoClient(host="localhost", port=27017
#client = MongoClient("mongodb://localhost:27017")
client = MongoClient()
print(client)


#connection à la bd, si n'existe pas, mongo la crééra à la première CRUD opération
#db = client["rptutorials"]
db = client.rptutorials
print(db)

#création de données à insérer

tutorial1 = {
        "title": "Working With JSON Data in Python",
        "author": "Lucas",
        "contributors": [
            "Aldren",
            "Dan",
            "Joanna"
        ],
    "url": "https://realpython.com/python-json/"
}

tutorial2 = {
    "title": "Python's Requests Library (Guide)",
    "author": "Alex",
    "contributors": [
        "Aldren",
        "Brad",
        "Joanna"
    ],
    "url": "https://realpython.com/python-requests/"
}

tutorial3 = {
    "title": "Object-Oriented Programming (OOP) in Python 3",
    "author": "David",
    "contributors": [
        "Aldren",
        "Joanna",
        "Jacob"
    ],
    "url": "https://realpython.com/python3-object-oriented-programming/"
}

#on spécifie la collection dans laquelle insérer les données
tutorial = db.tutorial

#insertion de données
response = tutorial.insert_one(tutorial1)
new_result = tutorial.insert_many([tutorial2, tutorial3])

#sans argument, find retourne toute la collection
for doc in tutorial.find():
    pprint.pprint(doc)

#recherche sur un champs
jon_tutorial = tutorial.find_one({"author": "Jon"})
pprint.pprint(jon_tutorial)

#fermeture de la connexion
client.close()