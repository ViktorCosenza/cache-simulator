import os
import sys
from myCache import CacheSim as Cache

def main():
    bsize, nsets, assoc =  sys.argv[0], sys.argv[1], sys.argv[2]
    c = Cache(bsize, nsets, assoc)
    


if __name__ == "__main__":
    main()