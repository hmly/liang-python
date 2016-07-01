def my_sqrt(x):
    EPSILON = 1e-10
    done = False
    root = (x + 1) / 2

    while not done:
        root1 = (root + x / root) / 2
        done = abs(root - root1) < EPSILON
        root = root1

    return root

def test():
    print ('Eneter a non-negative number and a negative to end the program: ')
    answer = float(input('> '))
    
    while answer >= 0:
        root = my_sqrt(answer)
        print ('The square root of %f is %f' % (answer, root))
        answer = float(input('> '))

if __name__ == '__main__': test()
