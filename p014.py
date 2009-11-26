def p014(limit):
    cache, maxcl, maxn = {}, 0, 0

    def collatz(i):
        cl = 0
        while i > 1:
            if i in cache:
                return cl + cache[i]
            else:
                if i % 2 == 0:
                    i /= 2
                else:
                    i = 3 * i + 1
                cl += 1
        return cl

    for i in xrange(limit):
        cache[i] = collatz(i)
        if cache[i] > maxcl:
            maxcl = cache[i]
            maxn = i

    return maxn

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p014, 1000000)
