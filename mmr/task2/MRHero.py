from mrjob.job import MRJob
from mrjob.step import MRStep
import numpy as np

class MRHero(MRJob):
    
    
    def mapper(self, _, line):
        heroes_split = line.split(' ')
        heroes_array = np.array(heroes_split)
        first_hero = heroes_array[0] 
        friends = int(len(heroes_array[1:]))
        
        yield 'Heroes', (friends, first_hero)

    def reducer(self, key, values):
        
        yield "Hero", max(values)
        


if __name__ == '__main__':
     MRHero.run()
