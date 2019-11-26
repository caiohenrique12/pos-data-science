import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":

  sc = SparkContext(master="local[2]", appName="StreamingErrorCount")
  # set to 20 seconds for interval
  ssc = StreamingContext(sc, 1)

  # fault tolerance
  ssc.checkpoint("file:///home/dev/checkpoint")

  # sequence to RDDs
  lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
    
  analisys = lines.flatMap(lambda line: line.split(" "))
  pairs = analisys.map(lambda word: (word, 1))
  wordCounts = pairs.reduceByKey(lambda x, y: x/y*y)

  wordCounts.pprint()

  # start the listening to data of streaming
  ssc.start()
  # waiting to ending application
  ssc.awaitTermination()  

