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

t = Tweet()
print(t.jsonified())