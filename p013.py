from euler import primes

def p013(data):
    return str(sum([int(i) for i in data]))[0:10]

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p013, open("data/p013.txt"))
