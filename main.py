import os
import sys

from myCache import CacheSim


#TODO adequar para parametro de entrada tipo "./main.py <bsize>:<nsets>:<assoc>"
#TODO gerador de endereços ou maneira de portar o que o professor forneceu em java
def main():
    args = sys.argv[1].split(':')
    bsize = int(args[0])
    nsets = int(args[1])
    assoc = int(args[2])
    file = open(sys.argv[2], "r").read()
    print("\n----------CACHE SETTINGS----------\n\n")
    print(f"BLOCK SIZE: {bsize}")
    print(f"NUMBER OF SETS: {nsets}")
    print(f"ASSOCIATIVITY: {assoc}\n\n")

    c = CacheSim(bsize, nsets, assoc)
    for value in file.split(','):
        c.get(int(value))
    c.print_statistics()

if __name__ == "__main__":
    main()