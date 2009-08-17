from operator import mul

def p008(data):
    digits = [int(c) for line in data for c in line if c.isdigit()]
    return max(reduce(mul, digits[i:i + 5]) for i in xrange(len(digits) - 5))

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p008, open("data/p008.txt"))
