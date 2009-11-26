from euler import ispalindrom

def p036(limit):
    def ispalbin(n):
        b = str(bin(n))[2:]
        return b == b[::-1]

    return sum(filter(ispalbin, filter(ispalindrom, xrange(1, limit))))

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p036, 1000000)
