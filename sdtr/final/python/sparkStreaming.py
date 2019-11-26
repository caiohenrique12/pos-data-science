import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":

	sc = SparkContext(master="local[2]", appName="StreamingErrorCount")
	# set to 20 seconds for interval
	ssc = StreamingContext(sc, 20)

	# fault tolerance
	ssc.checkpoint("file:///home/dev/checkpoint")
	
	# sequence to RDDs
	lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2])) 
 
	def countError(newValues, lastSum):
		if lastSum is None:
			lastSum = 0
		return sum(newValues, lastSum)


	# counting word "error"
	counts = lines.flatMap(lambda line: line.split(" "))\
			.filter(lambda word:"ERROR" in word)\
			.map(lambda word: (word, 1))\
			.updateStateByKey(countError)\
	
	# print the row in interval, does not necessary use loops
	counts.pprint() 

	# start the listening to data of streaming
	ssc.start()
  # waiting to ending application
	ssc.awaitTermination()
