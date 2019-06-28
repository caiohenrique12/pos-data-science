import json
import random
import threading
import time

from kafka import KafkaConsumer, KafkaProducer

class Producer(threading.Thread):
  
  def run(self):
    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
  
    while True:
      data = {}
      id_ = random.randint(0, 1000)
      candidates = {'candidate_1': 0, 'candidate_2': 0, 'candidate_3': 0}

      if data.__contains__(id(id_)):
        message = data.get(id_)
      else:
        for i in range(1, 1000):
          # what candidate, person going to vote
          candidate_vote = random.randint(1, 3)
          candidates[f'candidate_{candidate_vote}'] += 1
        
        print("Finishing Votes! See the next.")
        
        message = [id_, candidates]
        data[id_] = message

      producer.send('voting', message)
      time.sleep(random.randint(0, 2))
    
class Consumer(threading.Thread):

  def run(self):
    stream = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='latest')
    stream.subscribe(['voting'])
    
    for tuple in stream:
      tuple_json = json.loads(tuple.value)[1]
      key_max = max(tuple_json.keys(), key=(lambda k: tuple_json[k]))
      print(f"Winner! Cantidate: {key_max}, Votes: {tuple_json[key_max]}")
    
if __name__ == '__main__':
  threads = [
    Producer(),
    Consumer()
  ]

  for t in threads:
    t.start()
