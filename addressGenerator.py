
import random
import sys

def main():
    if len(sys.argv) < 3:
        raise ValueError("Argument length required!")
    quantity = int(sys.argv[1])
    filename = sys.argv[2]
    print("Generating {} addresses".format(quantity))
    generateAddresses(quantity=quantity, filename=filename)
    print("Done!")

def generateAddresses(quantity=100, seed=None, filename="adresses"):
    random.seed = seed
    addresses = []
    for i in range(int(quantity/2)):
        addresses.append(random.randrange(2**30, 2**31))
    for i in range(int(quantity/2)):
        addresses.append(random.randrange(2**32))
    open(filename, "w").write(','.join("{0:b}".format(address) for address in addresses))


if __name__ == '__main__':
    main()