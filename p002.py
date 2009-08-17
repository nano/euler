from euler import fibonacci

def p002(limit):
    return sum(filter(lambda x: x % 2 == 0, fibonacci(limit)))

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p002, 4000000)
