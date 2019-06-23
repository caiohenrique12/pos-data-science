import os
import time
import json
import random
import threading

from TwitterAPI import TwitterAPI
from kafka import KafkaConsumer, KafkaProducer

class Producer(threading.Thread):

  def run(self):
    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    api = TwitterAPI(os.environ['CONSUMER_KEY']
                     , os.environ['CONSUMER_SECRET']
                     , os.environ['TOKEN_KEY_TWITTER']
                     , os.environ['TOKEN_SECRET_TWITTER'])
    
    while True:
      req = api.request('search/tweets', {'q': 'favorites'})
      producer.send('favorite_tweets', Producer().iterate_tweets(req))
      time.sleep(random.randint(0, 2))

  def iterate_tweets(self, request):
    tweets = {}

    for item in request:
      if item['retweet_count'] > 0:
        tweets.update({f"{item['user']['screen_name']}": {'msg': "Favorite Tweet", 'text': item['text'], 'retweet_count': item['retweet_count'], 'location': item['user']['location']}})
      else:
        tweets.update({f"{item['user']['screen_name']}": {'msg': "Not favorite Tweet", 'text': item['text'], 'location': item['user']['location']}})

    message = [item['id'], tweets]

    return message

class Consumer(threading.Thread):

  def run(self):
    stream = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='latest')
    stream.subscribe(['favorite_tweets'])

    for tuple in stream:
      print(tuple.value)

if __name__ == '__main__':
  threads = [
    Producer(),
    Consumer()
  ]

for t in threads:
  t.start()
