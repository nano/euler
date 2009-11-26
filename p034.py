from euler import factorial

def p034(limit):
    fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

    def iscurious(n):
        return n == sum(fact[int(d)] for d in str(n))

    return sum(filter(iscurious, xrange(10, limit)))

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p034, 50000) # TODO Check upper bound
