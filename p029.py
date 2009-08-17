def p029(n):
    return len(set(pow(a, b) for a in xrange(2, n + 1) for b in xrange(2, n + 1)))

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p029, 100)
