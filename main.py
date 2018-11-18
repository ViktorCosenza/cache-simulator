import sys
from myCache import CacheSim


def main():
    if len(sys.argv) < 3:
        raise ValueError("Missing arguments, try python main.py nsets:bsize:assoc filename.extension")
    args = sys.argv[1].split(':')
    if len(args) < 3:
        raise ValueError("Bad cache definition, try nsets:bsize:assoc")
    
    nsets = int(args[0])
    bsize = int(args[1])
    assoc = int(args[2])
    if (is_powerof2(nsets) and is_powerof2(bsize) and is_powerof2(assoc)) == False:
        raise ValueError('Number of Sets, Block Size and Associativity must be a power of 2')
    nsets = int(nsets / bsize / assoc)
    if nsets < 1:
        raise ValueError('Bad Cache definition, nsets is to small')
    file = open(sys.argv[2], "r").read()
    print("\n----------CACHE SETTINGS----------\n")
    print("TOTAL CACHE SIZE (BYTES): {}".format(nsets * bsize * assoc))
    print("CACHE POSITIONS/SETS: {}".format(nsets))
    print("BLOCK SIZE: {}".format(bsize))
    print("ASSOCIATIVITY: {}".format(assoc))
    values = file.split(',')
    test_length =  len(values)
    fraction = int(test_length // 100)
    c = CacheSim(nsets, bsize, assoc)
    
    if len(sys.argv) == 4 and sys.argv[3] == 'prefech':
        print("Prefeching {} Values".format(c.size // c.bsize))
        for progress, value in enumerate(values):
            if progress == c.size / c.bsize:
                break
            c.get(int(value))
        c.reset_stats()
    
    for progress, value in enumerate(values):
        if fraction!=0 and progress % fraction == 0:
            print('|',end='', flush=True) 
        c.get(int(value, 2))
    print('\n')
    c.print_statistics()

def is_powerof2(num):
	return num != 0 and ((num & (num - 1)) == 0)


if __name__ == "__main__":
    main()