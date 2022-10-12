import tweepy

auth = tweepy.OAuth1UserHandler(
   "i4ELbXGMEBNE97HB6mrmNuI91", "tWjVFA9yzSzXroZwMSsnrQBE3FQqWV1lr4RmMjSS6vUNSVwBKv", "1572835833345986563-zBLKPbqewLfVIBvTIXem6RI7cOcmQr", "VDZkOJf3e0yUC9SJvI71MS190L9GOSNFuUu5LnbMqPVgs"
)
#consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAAOxrhQEAAAAAJfwkToj3MYyq40OZz2KiXLDbmzo%3Dobj9h2bGR39ff7gzOQhfN9p7vOPrmzkM1iwMAThzhwQkBcH2v0")

api = tweepy.API(auth)


#recherche des 200 derniers tweets de l'user donné et affichage des 3 derniers
userID= "Nivvvvvvees"

tweets = api.user_timeline(screen_name=userID, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )

for info in tweets[:3]:
     print("ID: {}".format(info.id))
     print(info.created_at)
     print(info.full_text)
     print("\n")


