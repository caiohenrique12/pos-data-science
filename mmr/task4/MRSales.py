# -*- coding: utf-8 -*-

from mrjob.job import MRJob

class MRSales(MRJob):
    
    def mapper(self, _, line):
        split_line = line.split(',')
        country = split_line[7]
        product = split_line[1]
        qtd = split_line[2]
        
        yield country, (product, qtd)
        
    def reducer(self, key, values):
        to_list = list(values)
        list_prod = {}
        sum_qtd = 0
        
        for item in to_list:
            sum_qtd += int(item[1])
            if item[0] in list_prod:
                list_prod[item[0]] = {}
            list_prod[item[0]] = sum_qtd
        
        yield key, list_prod
        
        
if __name__ == '__main__':
    MRSales.run()