import numpy as np
import random
from functools import reduce

class CacheSim:
    
    def __init__(self, nsets, bsize, assoc):
        self.nsets = int(nsets)
        self.bsize = int(bsize)
        self.assoc = int(assoc)
        self.size = self.nsets * self.bsize * self.assoc
        self.TOTAL_INSERTS = 0
        self.MISSES = {
            'compulsory': 0,
            'capacity': 0,
            'conflict': 0
        }
        self.cache = np.zeros(shape=(nsets, assoc), dtype=int) -1


    def get_total_misses(self):
        return reduce(lambda x,y: x+y , self.MISSES)

    def find_position(self, address):
        return int(address / self.bsize) % self.nsets 
    
    def insert(self, position, address, cache_set=None):
        if cache_set is None:
            cache_set = random.randint(0, self.assoc - 1)
        self.cache[position][cache_set] = address
    
    #TODO: Computar adequadamente cada tipo de miss
    #TODO: Computar quando há um hit 
    def get(self, address):
        position = self.find_position(address)
        first_address = int(address / self.bsize) * self.bsize
        for cache_set in range(self.assoc):
            if(self.cache[position][cache_set] == -1):
                self.insert(position, first_address, cache_set=cache_set)
                self.MISSES['compulsory'] +=1
        else:
            self.insert(position, first_address)
            self.MISSES['conflict'] += 1