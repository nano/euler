def p009(n):
    for a in xrange(1, n + 1):
        for b in xrange(1, n + 1):
            c = n - a - b
            if pow(a, 2) + pow(b, 2) == pow(c, 2):
                return a * b * c

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p009, 1000)
