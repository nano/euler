from euler import triangle

def p042(data):
    words = [s[1:-1] for s in data.split(",")]
    t = set(triangle(max([len(s) for s in words]) * 26))

    def istriangleword(word):
        return sum([ord(c) - 64 for c in word]) in t

    return len(filter(istriangleword, words))

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p042, open("data/p042.txt").read())
