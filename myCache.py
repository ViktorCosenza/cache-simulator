
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
            'conflict': 0,
            'total': 0
        }
        self.cache = []

    def findSet(self, address):
        return address % self.nsets
    
    def insert(self, address):
        position = self.findSet(address)
        if self.cache[position][][] === None:


        return True
    
    def get(self, address):
        
        return True


        