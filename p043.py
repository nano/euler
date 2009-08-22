from euler import permutations

def p043():
    P = [2, 3, 5, 7, 11, 13, 17]
    N = filter(lambda x: x[0] is not "0", permutations("0123456789"))

    def check(n):
        for i in xrange(6, -1, -1):
            x = int("%d%d%d" % tuple(map(int, n[i+1:i+4])))
            if not (x % P[i] == 0):
                return False
        return True

    return sum(map(int, filter(check, N)))

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p043)
