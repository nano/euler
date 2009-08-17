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

def sieve(limit):
    s = range(limit + 1)
    s[1] = 0
    for i in xrange(2, int(pow(limit, 0.5)) + 1):
        if s[i] != 0:
            s[2*i::i] = [0] * (limit / i - 1)
    return filter(None, s)
