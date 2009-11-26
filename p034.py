from euler import factorial

def p034(limit):
    def iscurious(n):
        return n == sum(map(factorial, map(int, (c for c in str(n)))))
    return sum(filter(iscurious, xrange(10, limit)))

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p034, 50000) # TODO Check upper bound
