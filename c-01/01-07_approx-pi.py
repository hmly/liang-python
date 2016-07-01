# Liang 1.7

# n: number of terms
def approxPI(n):
    PI = j = 0
    
    for i in range(1, 2*n, 2):
        if j % 2 == 0:
            PI += 1/i
        else:
            PI -= 1/i
        j += 1
        
    return PI * 4

def main():
    print ('Approx of PI to the...')
    print ('6th term:', approxPI(6))
    print ('8th term:', approxPI(8))

    # Test - match success
    # print (4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11))
    # print (4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15))

main()
