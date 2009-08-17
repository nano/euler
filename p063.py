def p063():
    n = 0
    for power in xrange(1, 22):
        for i in xrange(1, 10):
            j = pow(i, power)
            if len(str(j)) == power:
                n += 1
    return n

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p063)
