import random
from functools import reduce
from operator import add

class CacheSim:
    
    def __init__(self, nsets, bsize, assoc):
        self.nsets = int(nsets)
        self.bsize = int(bsize)
        self.assoc = int(assoc)
        self.size = self.nsets * self.bsize * self.assoc
        self.TOTAL_ACCESSES = 0
        self.MISSES = {
            'compulsory': 0,
            'capacity': 0,
            'conflict': 0
        }
        self.cache = [[-1 for block in range(assoc)] for cache_set in range(nsets)]
        self.bit_val = [[0 for block in range(assoc)] for cache_set in range(nsets)]

    def print_statistics(self):
        total = reduce(add, self.MISSES.values())
        compulsory = self.MISSES['compulsory']
        capacity = self.MISSES['capacity']
        conflict = self.MISSES['conflict']

        print("----------CACHE STATS----------\n")
        print("-> ABSOLUTE STATS\n")
        print("COMPULSORY MISSES: {}".format(compulsory))
        print("CAPACITY MISSES : {}".format(capacity))
        print("CONFLICT MISSES: {}".format(conflict))
        print("TOTAL MISSES: {}".format(total))
        print("TOTAL ACCESSES: {}\n".format(self.TOTAL_ACCESSES))

        miss_rate = ((total) / self.TOTAL_ACCESSES) * 100
        compulsory_over_total = 100 * self.MISSES['compulsory'] / total
        conflict_over_total = 100 * self.MISSES['conflict'] / total
        capacity_over_total = 100 * self.MISSES['capacity'] / total
        print("-> PERCENTAGE STATS\n")
        print("MISS RATE: {0:.2f}%".format(miss_rate))
        print("HIT RATE: {0:.2f}%".format(100 - miss_rate))
        print("COMPULSORY/TOTAL MISSES: {0:.2f}%".format(compulsory_over_total))
        print("CAPACITY/TOTAL MISSES: {0:.2f}%".format(capacity_over_total))
        print("CONFLICT/TOTAL MISSES: {0:.2f}%".format(conflict_over_total))
    
    def find_position(self, address):
        return address // self.bsize % self.nsets 
        
    def insert(self, position, address):
        for cache_set in range(self.assoc):
            if self.bit_val[position][cache_set] == 0:
                self.bit_val[position][cache_set] = 1
                self.MISSES['compulsory'] +=1
                break
        else:
            if self.is_full():
                self.MISSES['capacity'] += 1
            else:
                self.MISSES['conflict'] += 1
            cache_set = random.randint(0, self.assoc - 1)
        self.cache[position][cache_set] = address
    
    def is_full(self):
        for row in self.bit_val:
            for value in row:
                if value == 0:
                    return False
        return True

    def reset_stats(self):
        self.TOTAL_ACCESSES = 0
        self.MISSES = {
            'compulsory': 0,
            'capacity': 0,
            'conflict': 0
        }
    
    def get(self, address):
        position = self.find_position(address)
        first_address = int(address / self.bsize) * self.bsize
        for cache_set in range(self.assoc):
            if(self.cache[position][cache_set] == first_address):
                break
        else:
            self.insert(position, first_address)
        self.TOTAL_ACCESSES += 1