from euler import ispalindrom

def p004(a, b):
    numbers = [i * j for i in xrange(a, b + 1) for j in xrange(a, b + 1)]
    return max(filter(ispalindrom, numbers))

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p004, 100, 999)
