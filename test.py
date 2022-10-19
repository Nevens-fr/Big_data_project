import tweepy
import re
import textblob
import codecs
#from textblob_fr import PatternTagger, PatternAnalyzer

auth = tweepy.OAuth1UserHandler(
   "i4ELbXGMEBNE97HB6mrmNuI91", "tWjVFA9yzSzXroZwMSsnrQBE3FQqWV1lr4RmMjSS6vUNSVwBKv", "1572835833345986563-zBLKPbqewLfVIBvTIXem6RI7cOcmQr", "VDZkOJf3e0yUC9SJvI71MS190L9GOSNFuUu5LnbMqPVgs"
)

#consumer_key, consumer_secret, access_token, access_token_secret

#auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAAOxrhQEAAAAAJfwkToj3MYyq40OZz2KiXLDbmzo%3Dobj9h2bGR39ff7gzOQhfN9p7vOPrmzkM1iwMAThzhwQkBcH2v0")
#client id
#TjVEa1ZkdFJ3bm0yUFVpWXA5ZVc6MTpjaQ
#client secret
#WVMtKnlloHg7j3wG8WJcbtTEHwlNbwmROcFXnOwmjzTPOa0Yzo

api = tweepy.API(auth)

#recherche des 200 derniers tweets de l'user donné et affichage des 3 derniers
#userID= "DasNotMeSorry"
"""
userID= "_Petit_Jean_"

tweets = api.user_timeline(screen_name=userID, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )

for info in tweets[:len(tweets)]:
     print("ID: {}".format(info.id))
     print(info.created_at)
     print(info.full_text)
     print("\n")
"""
#récupération de tous les tweets contenant quoi
#mot = "quoi"
mot="#guncontrol"
#mot ="#GPExplorer"
q = (mot)
q +=  " -filter:retweets"
count = 200
fetched_tweets = api.search_tweets(q, count = count,lang="en",tweet_mode = 'extended')


"""regarde si un mot est a la fin du tweet
if(None == re.search(mot+'$', fetched_tweets[0].full_text)):
   print(fetched_tweets[0].full_text)
   #affichage de l'url pour consulter le résultat dans le navigateur
   print("https://twitter.com/"+str(fetched_tweets[0].user.id) +"/status/"+str(fetched_tweets[0].id))
else:
   print("Ne fini pas par quoi")
"""
print(len(fetched_tweets))

f = codecs.open("resultats.txt", "w",  "utf-8")

i = 0

#affichage d'un tweet entier
#print(fetched_tweets[0].__str__())

while i < len(fetched_tweets):

   text = fetched_tweets[i].full_text

   blob = textblob.TextBlob(text)
   #fr version
   #blob = textblob.TextBlob(text,pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

   #ecriture de l'objet
   #f.write(fetched_tweets[i].__str__())
   f.write("global polarity" + str(blob.polarity) + " subjectivity " + str(blob.subjectivity) + " tweet id : " + str(fetched_tweets[i].id) +"\n")
   f.write("https://twitter.com/"+str(fetched_tweets[i].user.id) +"/status/"+str(fetched_tweets[i].id) + "\n")
   f.write("Created at : " + str(fetched_tweets[i].created_at) + "\n")
   f.write("\n")
   f.write(fetched_tweets[i].full_text)
   f.write("\n")
   f.write("##################################################################################################\n")

   i+=1

f.close()

""""
-1 a -0.6 neg
-0.59 a -0.2 myen neg
-0.19 a 0.19 mitigé
0.2 a 0.59 myen positif
0.6 a 1 positiif


-0.1 a 0.1 informatif
""" 