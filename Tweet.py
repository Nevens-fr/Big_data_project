
class Tweet:

    def __init__(self, id, full_text, user, created_at,polarity, subjectivity):
        self.id = str(id)
        self.full_text = str(full_text)
        self.user = str(user)
        self.created_at = created_at
        self.polarity = str(polarity)
        self.subjectivity = str(subjectivity)

    ##
    #Creation d'un objet json avec toutes les données de la classe
    def jsonified(self):
        return {
            "id" : self.id,
            "full_text" : self.full_text ,
            "created_at" : self.created_at ,
            "polarity" : self.polarity ,
            "subjectivity" : self.subjectivity ,
            "user" : self.user
        }

    def dico(self):
        return {"id" : self.id,"full_text" : self.full_text ,"created_at" : self.created_at ,"polarity" : self.polarity ,"subjectivity" : self.subjectivity ,"user" : self.user}

    ##
    # Recrée la classe depuis des données json lues
    # data : une chaîne de caractère json
    def readData(self, data):
        for key, value in data.items():
            if key == "id": self.id = value
            elif key == "full_text" : self.full_text = value
            elif key == "created_at" : self.created_at = value
            elif key == "polarity" : self.polarity = value
            elif key == "subjectivity" : self.subjectivity = value
            elif key == "user" : self.user = value
"""test
t = Tweet()
print(t.jsonified())
print("")
t.readData(t.jsonified())
print(t.jsonified())"""