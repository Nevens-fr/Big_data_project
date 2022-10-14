class Tweet:

    def __init__(self):
        self.id = "a"
        self.text = "a"
        self.full_text = "a"
        self.user = "a"
        self.created_at = "a"
        self.polarity = "a"
        self.subjectivity = "a"

    ##
    #Creation d'un objet json avec toutes les données de la classe
    #TODO change le user en objet
    def jsonified(self):
        return {
            "id" : self.id,
            "text" : self.text,
            "full_text" : self.full_text ,
            "created_at" : self.created_at ,
            "polarity" : self.polarity ,
            "subjectivity" : self.subjectivity ,
            "user" : self.user ,
        }

    ##
    # Recrée la classe depuis des données json lues
    # data : une chaîne de caractère json
    #TODO user passer dans un read data aussi
    def readData(self, data):
        for key, value in data.items():
            if key == "id": self.id = value
            elif key == "text" : self.text = value
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