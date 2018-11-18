import numpy as np
import sys

def main():
    if len(sys.argv) < 3:
        raise ValueError("Argument length and filename are required, try python addressGenerator.py <quantityr> <filename>")
    quantity = int(sys.argv[1])
    filename = sys.argv[2]
    value_range = sys.argv[3].split(':') if len(sys.argv) == 4 else [10, 12]
    value_range = [int(value) for value in value_range]
    print("Generating {} addresses".format(quantity))
    generateAddresses(quantity=quantity, filename=filename, value_range=value_range)
    print("Done!")

def generateAddresses(quantity=100, filename="adresses", value_range=[10, 12]):
    lower = 2**value_range[0]
    upper = 2**value_range[1]
    print("Range: {lower} to {upper}".format(lower=lower, upper=upper))
    centre = (lower + upper) // 2
    variation = upper // (np.log2(upper) * 2)
    addresses = np.random.normal(centre, variation, quantity).astype(int)
    open(filename, "w").write(','.join("{0:b}".format(address) for address in addresses))


if __name__ == '__main__':
    main()
