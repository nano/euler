def p006(n):
    return pow(sum(i for i in xrange(1, n + 1)), 2) - sum(pow(i, 2) for i in xrange(1, n + 1))

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p006, 100)
