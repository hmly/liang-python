# Liang 5.26

LIMIT = 97

def sumOfSeries(limit):
    seriesSum = 0;
    i = 1; j = 3
    while i <= LIMIT:
        seriesSum += i / j
        i += 2
        j += 2
    return seriesSum

def main():
    print ('The sum of the series is %f' % sumOfSeries(LIMIT))

main()
