import tweepy
import textblob
import Tweet
import mongo
import datetime

mongo.init_co()

auth = tweepy.OAuth1UserHandler(
   "i4ELbXGMEBNE97HB6mrmNuI91", "tWjVFA9yzSzXroZwMSsnrQBE3FQqWV1lr4RmMjSS6vUNSVwBKv", "1572835833345986563-zBLKPbqewLfVIBvTIXem6RI7cOcmQr", "VDZkOJf3e0yUC9SJvI71MS190L9GOSNFuUu5LnbMqPVgs"
)


api = tweepy.API(auth)

i = 0

for a in tweepy.Cursor(api.search_tweets,  
              q="guncontrol OR gunviolence OR banguns OR gunsuck -filter:retweets",
              tweet_mode = 'extended',
              result_type="recent",
              lang="en",
              count=2000).items():
   blob = textblob.TextBlob(a.full_text)
   a1 = Tweet.Tweet(a.id, a.full_text, a.user.id, a.created_at, blob.polarity, blob.subjectivity)
   if mongo.check_si_tweet_existe(a1.id, a1.user) == False:
      i+=1
      a1.created_at = str(a1.created_at).split(" ",1)[0] #enlève les h:mm:ss
      a1.created_at = str(datetime.datetime.strptime(str(a1.created_at), '%Y-%m-%d')).split(" 00:00:00", 1)[0]
      mongo.ajoutBDD(a1.jsonified())

print("Nombre de nouveauw tweets trouvés : " + str(i))

mongo.ferme_db()