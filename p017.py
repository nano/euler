def p017():
    def number2word(i):
        numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ]
        tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        if i == 0:
            return ""
        if i < 20:
            return numbers[i - 1]
        if i < 100:
            return tens[i / 10 - 2] + number2word(i % 10)
        if i < 1000:
            s = number2word(i / 100) + "hundred"
            if i % 100:
                s += "and" + number2word(i % 100)
            return s

    words = []

    for i in xrange(1, 1000):
        words.append(number2word(i))

    return len("".join(words)) + len("onethousand")

if __name__ == "__main__":
    from benchmark import benchmark
    benchmark(p017)
