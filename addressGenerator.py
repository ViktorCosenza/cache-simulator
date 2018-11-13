
import random

def main():
    generateAddresses(1000, 5452, 'test')

def generateAddresses(quantity=100, seed=None, filename="adresses"):
    random.seed = seed
    addresses = []
    for i in range(int(quantity/2)):
        addresses.append(random.randrange(10))
    for i in range(int(quantity/2)):
        addresses.append(random.randrange(1000))
    open(filename, "w").write(','.join(str(e) for e in addresses))


if __name__ == 'main':
    main()