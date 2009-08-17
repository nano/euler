from euler import ispalindrom

def p055(n):
    def islychrel(n, i=50):
        while i > 1:
            n = n + int(str(n)[::-1])
            if ispalindrom(n):
                return True
            else:
                i -= 1
        return False
    return n - 1 - len(filter(islychrel, xrange(1, n)))

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p055, 10000)
