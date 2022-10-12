import tweepy
import re

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
userID= "_Petit_Jean_"

tweets = api.user_timeline(screen_name=userID, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
"""
for info in tweets[:len(tweets)]:
     print("ID: {}".format(info.id))
     print(info.created_at)
     print(info.full_text)
     print("\n")
"""
#récupération de tous les tweets contenant quoi
mot = "quoi"
q = (mot)
count = 100
fetched_tweets = api.search_tweets(q, count = count,tweet_mode = 'extended')

if(None == re.search(mot+'$', fetched_tweets[0].full_text)):
   print(fetched_tweets[0].full_text)
   #affichage de l'url pour consulter le résultat dans le navigateur
   print("https://twitter.com/"+str(fetched_tweets[0].user.id) +"/status/"+str(fetched_tweets[0].id))
else:
   print("Ne fini pas par quoi")
