##
# Ce module permet d'enregistrer des données dans une base mongo DB
# Ces données ont été étiquetées par les membres du groupe.

import mongo

##
# Range des données issues des datas dans le dico spécifié entre lim - 20 et lim
def rangeDonnees(dico, data, lim):
    i = lim - 20

    while i < lim:
        ind = int(data[i].split(" ")[0])
        dico[ind] = data[i].split(" ")[-1]
        dico[ind] = dico[ind].replace("\n", " ")
        i+=1
    return dico

##
# créé un json à partir d'un nom, d'un id et d'une valeur
def createJSON(nom, id, val):
    return {
        "nom" : nom,
        "id" : id,
        "val" : val
    }


mongo.init_co()

f = open("etiquettage.txt", "r")

aure = {}
thom = {}
axel = {}

data = f.readlines()

f.close()

aurelien = 20
thomas = 40
axel1 = 60

aure = rangeDonnees(aure, data, aurelien)
thom = rangeDonnees(thom, data, thomas)
axel = rangeDonnees(axel, data, axel1)


for key,value in aure.items():
    mongo.ajoutBDD_eti(createJSON("Aurélien", key, value))
for key,value in thom.items():
    mongo.ajoutBDD_eti(createJSON("Thomas", key, value))
for key,value in axel.items():
    mongo.ajoutBDD_eti(createJSON("Axel", key, value))


mongo.ferme_db()