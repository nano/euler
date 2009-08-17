def p001(n):
    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, xrange(1, n)))

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p001, 1000)
