def p067(data):
    triangle = [[int(i) for i in line.split(" ")] for line in data]
    for i in xrange(len(triangle) - 2, -1, -1):
        for j in xrange(0, len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j:j+2])
    return triangle[0][0]

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p067, open("data/p067.txt"))
