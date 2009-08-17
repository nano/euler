def p028(size):
    return sum(4 * pow(i, 2) - 6 * i + 6 for i in xrange(3, size + 1, 2)) + 1

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p028, 1001)
