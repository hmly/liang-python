# L 15.3

def gcd(m, n):
    if m % n == 0:
        return n
    return gcd(n, m % n)

def main():
    m, n = input('Enter two numbers: ').split(',')
    print (gcd(int(m), int(n)))

if __name__ == '__main__':
    main()
