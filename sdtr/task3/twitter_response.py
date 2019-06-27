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
      req = api.request('search/tweets', {'q': 'pizza'})
      producer.send('tweets', Producer().iterate_tweets(req))
      time.sleep(random.randint(0, 2))

  def iterate_tweets(self, request):
    message = []

    for item in request:
      tweets = []
      tweets = {'name': item['user']['screen_name'], 'text': item['text'],
                'retweet_count': item['retweet_count'], 'location': item['user']['location']}

      message.append([item['id'], tweets])

    return message

class Consumer(threading.Thread):

  def run(self):
    stream = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='latest')
    stream.subscribe(['tweets'])
    unlike_tweets = 0
    
    for tuple in stream:
      for item in json.loads(tuple.value):
        if int(item[1]['retweet_count']) > 0:
          print(item[1])
        else:
          unlike_tweets += 1
          print(f"Unlike tweets: {unlike_tweets}")
        
if __name__ == '__main__':
  threads = [
    Producer(),
    Consumer()
  ]

for t in threads:
  t.start()
