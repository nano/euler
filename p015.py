def p015(size):
    triangle = [[1]]
    for i in range(size * 2):
        row = [1]
        for j in range(i):
            row.append(triangle[-1][j] + triangle[-1][j + 1])
        row.append(1)
        triangle.append(row)
    return triangle[-1][size]

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p015, 20)
