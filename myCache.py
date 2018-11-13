import numpy as np
import random
from functools import reduce

class CacheSim:
    
    def __init__(self, nsets, bsize, assoc):
        self.nsets = int(nsets)
        self.bsize = int(bsize)
        self.assoc = int(assoc)
        self.size = self.nsets * self.bsize * self.assoc
        self.TOTAL_ACCESSES = 0
        self.MISSES = {
            'compulsory': 0,
            'other': 0
        }
        self.cache = np.zeros(shape=(nsets, assoc), dtype=int) -1


    def print_statistics(self):
        total = reduce(lambda x,y: x+y , self.MISSES.values())
        compulsory = self.MISSES['compulsory']
        other = self.MISSES['other']
        print("----------CACHE STATS----------\n\n")
        print("-> ABSOLUTE STATS\n")
        print(f"COMPULSORY MISSES: {compulsory}")
        print("CAPACITY ", end='') if self.nsets == 1 else print("CONFLICT ", end='')
        print(f"MISSES : {other}")
        print(f"TOTAL MISSES: {total}")
        print(f"TOTAL ACCESSES: {self.TOTAL_ACCESSES}\n")

        print("-> PERCENTAGE STATS\n")

    def find_position(self, address):
        return int(address / self.bsize) % self.nsets 
    
    def insert(self, position, address, cache_set=None):
        if cache_set is None:
            cache_set = random.randint(0, self.assoc - 1)
        self.cache[position][cache_set] = address
    
    #TODO: Computar adequadamente cada tipo de miss
    def get(self, address):
        position = self.find_position(address)
        first_address = int(address / self.bsize) * self.bsize
        for cache_set in range(self.assoc):
            #COMPULSORY MISS
            if(self.cache[position][cache_set] == -1):
                self.insert(position, first_address, cache_set=cache_set)
                self.MISSES['compulsory'] +=1
            #HIT
            if(self.cache[position][cache_set] == first_address):
                break
        #CAPACITY/CONFLICT MISS
        else:
            self.insert(position, first_address)
            self.MISSES['other'] += 1
        self.TOTAL_ACCESSES += 1