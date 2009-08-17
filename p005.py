from euler import lcm

def p005(n):
    r = 1
    for i in xrange(1, n + 1):
        r = lcm(r, i)
    return r

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p005, 20)
