
import random
import sys

def main():
    if len(sys.argv) < 3:
        return print("Argument length required!")
    quantity = int(sys.argv[1])
    filename = sys.argv[2]
    print(f"Generating {quantity} addresses")
    generateAddresses(quantity=quantity, filename=filename)
    print("Done!")

def generateAddresses(quantity=100, seed=None, filename="adresses"):
    random.seed = seed
    addresses = []
    for i in range(int(quantity/2)):
        addresses.append(random.randrange(10))
    for i in range(int(quantity/2)):
        addresses.append(random.randrange(1000))
    open(filename, "w").write(','.join(str(e) for e in addresses))


if __name__ == '__main__':
    main()