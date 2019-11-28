# -*- coding: utf-8 -*-

from mrjob.job import MRJob

class MRSales(MRJob):
    
    def mapper(self, _, line):
        split_line = line.split(',')
        country = split_line[7]
        product = split_line[1]
        
        yield country, product
        
    def reducer(self, key, values):
        values_to_list = list(values)
        dict_product = {}
        count = 0
        
        for item in values_to_list:
            if item not in dict_product:
                dict_product[item] = {}
            
            count += 1
            dict_product[item] = count
        
        yield key, dict_product
        
        
if __name__ == '__main__':
    MRSales.run()