def p016(n):
    return sum(map(int, str(pow(2, n))))

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p016, 1000)
