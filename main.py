import os
import sys

from myCache import CacheSim


def main():
    if len(sys.argv) < 3:
        return print("\nMissing arguments!\n  nsets:bsize:assoc filename.extension")
    args = sys.argv[1].split(':')
    if len(args) < 3:
        return print("\nBad cache definition!\n nsets:bsize:assoc")
    nsets = int(args[0])
    bsize = int(args[1])
    assoc = int(args[2])
    file = open(sys.argv[2], "r").read()
    print("\n----------CACHE SETTINGS----------\n\n")
    print(f"BLOCK SIZE: {bsize}")
    print(f"NUMBER OF SETS: {nsets}")
    print(f"ASSOCIATIVITY: {assoc}\n\n")

    c = CacheSim(nsets, bsize, assoc)
    for value in file.split(','):
        c.get(int(value))
    c.print_statistics()

if __name__ == "__main__":
    main()