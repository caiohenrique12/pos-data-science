from mrjob.job import MRJob


class MoveAvarege(MRJob):

    def mapper(self, _, line):
        name, timestamp, value = line.split(",")
        yield name, (timestamp, float(value))

    def reducer(self, key, values):
        self.windowSize = 2

        data = list(values)
        data.sort()

        sum = 0.0
        

        for i in range(0, len(data)):
            value = data[i][1]
            sum += value

            amount = min(i + 1, self.windowSize)

            if i >= self.windowSize:
                sum -= data[i-self.windowSize][1]

                movingAvarege = sum / amount

                timestamp = data[i][0]

                outputValue = '{0}, {1}, {2}'.format(str(timestamp), str(value), str(movingAvarege))

                yield key, outputValue

        

        

if __name__ == '__main__':
    MoveAvarege.run()