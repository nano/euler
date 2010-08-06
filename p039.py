import math

def p039(amax=500):
    results = {}

    for a in range(1, amax + 1):
        for b in range(1, a):
            c = math.sqrt(pow(a, 2) + pow(b, 2))
            p = a + b + c

            if p in results:
                results[p] += 1
            else:
                results[p] = 1

    maxr = maxp = 0

    for (p, r) in results.items():
        if r > maxr:
            maxr = r
            maxp = p

    return maxp

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p039)
