def p048(n):
    return str(sum(pow(i, i) for i in xrange(1, n + 1)))[-10:]

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p048, 1000)
