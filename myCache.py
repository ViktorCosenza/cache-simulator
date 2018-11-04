import numpy as np
import random

class CacheSim:
    
    def __init__(self, nsets, bsize, assoc):
        self.size = nsets * bsize * assoc
        self.nsets = nsets
        self.bsize = bsize
        self.assoc = assoc
        self.TOTAL_INSERTS = 0
        self.MISSES = {
            'compulsory': 0,
            'capacity': 0,
            'conflict': 0
        }
        self.cache = np.empty(shape=(nsets, assoc), dtype=int).fill(-1)


    def get_total_misses(self):
        return reduce(lambda x,y: x+y , self.MISSES)

    def find_position(self, address):
        return (address / self.bsize) % self.nsets 
    
    def insert(self, position, address):
        cache_set = random.randint(0, self.assoc - 1)
        self.cache[position][cache_set] = address
    
    #TODO: Computar adequadamente cada tipo de miss
    def get(self, address):
        position = self.find_position(address)
        first_address = int(address / self.bsize) * self.bsize
        for cache_set in range(self.assoc):
            if(self.cache[position][cache_set] == -1):
                self.cache[position][cache_set] = first_address
        else:
            self.insert(position, first_address)
            self.MISSES['conflict'] += 1