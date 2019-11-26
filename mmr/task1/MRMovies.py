from mrjob.job import MRJob
from mrjob.step import MRStep

class MRMovies(MRJob):
    
    def steps(self):
        return [
                MRStep(mapper=self.mapper,
                       reducer=self.reducer),
                MRStep(reducer=self.reducer_sort)
        ]
    
    def mapper(self, _, line):
        _, movie, rating, _, = line.split('\t')
        
        yield movie, int(rating)

    def reducer(self, key, values):
        list_rating = list(values)
        avg_rating = float(sum(list_rating)/len(list_rating))
                
        yield "Movies", (round(avg_rating,2), key)
        
    
    def reducer_sort(self, key, values):
        list_movies = list(values)
        list_movies.sort()
        
        for item in list_movies:
            yield item[1], item[0]


if __name__ == '__main__':
     MRMovies.run()