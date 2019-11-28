# -*- coding: utf-8 -*-
from mrjob.job import MRJob

class MRAvgTotalSales(MRJob):
    
    def mapper(self, _, line):
        split_line = line.split(',')
        timestamp = split_line[0]
        country = split_line[7]
        product = split_line[1]
        price = split_line[2]
        
        yield (country, product), (timestamp, float(price))
        
    def reducer(self, key, values):
        self.windowSize = 2
        values_to_list = list(values)
        key_to_list = list(key)
        sum_price = 0.0        
                        
        values_to_list.sort()
        
        for item in range(0, len(values_to_list)):
            value = values_to_list[item][1]
            sum_price += value
            # amount = min(item + 1, self.windowSize)
            
            if item >= self.windowSize:
                sum_price -= values_to_list[item-self.windowSize][1]
                timestamp = values_to_list[item][0]
                
                yield key_to_list, f"{timestamp} - {value} - {sum_price}"
        
        
if __name__ == '__main__':
    MRAvgTotalSales.run()