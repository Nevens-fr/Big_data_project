##
# Ce module donne accès à une classe regroupant les données d'un tweet

class Tweet:

    def __init__(self, id, full_text, user, created_at,polarity, subjectivity):
        self.id = id
        self.full_text = str(full_text)
        self.user = user
        self.created_at = created_at
        self.polarity = polarity
        self.subjectivity = subjectivity
        
    def add_value(self):
        if(float(self.polarity) <= -0.6):
            return "très négatif"
        elif (float(self.polarity) <= -0.2):
            return "plutôt négatif"
        elif(float(self.polarity) <= 0.19):
            return "mitigé/informatif"
        elif(float(self.polarity) <= 0.59):
            return "plutôt positif"
        else:
            return "très positif"

    ##
    #Creation d'un objet json avec toutes les données de la classe
    def jsonified(self):
        return {
            "id" : self.id,
            "full_text" : self.full_text ,
            "created_at" : str(self.created_at) ,
            "polarity" : self.polarity ,
            "subjectivity" : self.subjectivity ,
            "user" : self.user,
            "sentiment" : self.add_value()
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
            elif key == "_id" :self.mid = value
        self.sentiment = self.add_value()