from time import clock

def benchmark(func, *args):
    start, result = clock(), func(*args)
    print "%s (%f sec)" % (result, clock() - start)
