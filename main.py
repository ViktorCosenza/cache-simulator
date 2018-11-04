import os
import sys
from myCache import CacheSim

def main():
    bsize, nsets, assoc =  sys.argv[0], sys.argv[1], sys.argv[2]
    c = CacheSim(bsize, nsets, assoc)
    


if __name__ == "__main__":
    main()