from euler import primes

def p010(limit):
    return sum(primes(limit=limit))

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p010, 2e6)
