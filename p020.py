from euler import factorial

def p020(n):
    return sum(map(int, str(factorial(n))))

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p020, 100)
