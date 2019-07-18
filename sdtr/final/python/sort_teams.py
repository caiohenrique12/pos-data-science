import json
import random
import threading
import time

from kafka import KafkaConsumer, KafkaProducer, TopicPartition

class ProducerSerieA(threading.Thread):

  def run(self):
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    teams = ["#atletico_mg", "#atletico_pr", "#avai", "#bahia", "#botafogo", "#ceara", "#chapecoense", "#corinthians", "#cruzeiro", "#csa", "#flamengo", "#fluminense", "#fortaleza", "#goias", "#gremio", "#internacional", "#palmeiras", "#santos", "#sao_paulo", "#vasco"]
    
    while True:
      number = random.randint(0, 19)
      time.sleep(random.randint(0, 3))
      # print(teams[number])
      producer.send('serie-a', teams[number])
      

class ProducerSerieB(threading.Thread):

  def run(self):
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    teams = ["#america_mg", "#atletico_go", "#botafogo_sp", "#bragantino", "#brasil_de_pelotas", "#coritiba", "#criciuma", "#crb", "#cuiaba", "#figueirense", "#guarani", "#londrina", "#oeste", "#operario", "#parana", "#ponte_preta", "#sao_bento", "#sport", "#vila_nova", "#vitoria"]

    while True:
      number = random.randint(0, 19)
      time.sleep(random.randint(0, 3))
      # print(teams[number])
      producer.send('serie-b', teams[number])


class ConsumerSeries(threading.Thread):

  def run(self):
    stream = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='latest', group_id='series')
    stream.subscribe(['serie-a', 'serie-b'])

    for tuple in stream:
      print(f"{tuple.value}, {tuple.topic}")


if __name__ == '__main__':
  threads = [
    ProducerSerieA(),
    ProducerSerieB(),
    ConsumerSeries()
  ]
  
  for t in threads:
    t.start()
