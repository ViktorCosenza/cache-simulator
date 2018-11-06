import os
import sys
from myCache import CacheSim

#TODO adequar para parametro de entrada tipo "./main.py <bsize>:<nsets>:<assoc>"
#TODO gerador de endereços ou maneira de portar o que o professor forneceu em java
def main():
    bsize, nsets, assoc =  sys.argv[0], sys.argv[1], sys.argv[2]
    c = CacheSim(bsize, nsets, assoc)
    


if __name__ == "__main__":
    main()