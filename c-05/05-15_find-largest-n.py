# Liang 5.15
LIMIT = 12000

def findLargestN(limit):
    n = 1
    while n*n*n < limit:
        n += 1
    return n - 1

def main():
    print ('The largest n such that n^%d is less than %d is %d.' %\
           (3, LIMIT, findLargestN(LIMIT)))

main()
