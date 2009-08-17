def p030(power):
    limit = 1
    while limit * pow(9, power) >= pow(10, limit - 1):
        limit += 1
    def check(i):
        return i == sum(map(lambda n: pow(int(n), power), str(i)))
    return sum(filter(check, xrange(5, limit * pow(10, power))))

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p030, 5)
