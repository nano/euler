def factorial(i):
    if i == 0:
        return 1
    return i * factorial(i - 1)

def fibonacci(limit=None):
    i, j = 1, 1
    while limit == None or j <= limit:
        yield j
        i, j = j, i + j

def ispalindrom(i):
    return i == int(str(i)[::-1])

def ispandigital(i):
    s = str(i)
    l = len(s)
    return set(map(int, s)) == set(range(1, l + 1))

def gcd(i, j):
    if j:
        return gcd(j, i % j)
    return i

def lcm(i, j):
    return i * j / gcd(i, j)

def permutations(s):
    if len(s) == 1:
        yield s
    else:
        for p in permutations(s[1:]):
            for i in xrange(len(p) + 1):
                yield p[:i] + s[0:1] + p[i:]

def triangle(limit=None):
    i = 1
    while limit == None or i <= limit:
        yield sum([j for j in xrange(1, i + 1)])
        i += 1

def primes(numbers=None, limit=None):
    i = 0
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2   # first integer to test for primality
    while 1:
        if q not in D:
            if limit and q > limit:
                return
            yield q        # not marked composite, must be prime
            i += 1
            if numbers and i == numbers:
                return
            D[q * q] = [q]   # first multiple of q not already marked
        else:
            for p in D[q]: # move each witness to its next multiple
                D.setdefault(p + q, []).append(p)
            del D[q]       # no longer need D[q], free memory
        q += 1
