# Liang 4.3

def compute2x2LinearEq(a, b, c, d, e, f):
    if a*d - b*c != 0:
        return [(e*d - b*f) / (a*d - b*c), (a*f - e*c) / (a*d - b*c)]
    else:
        return 'The equation has no solution.'

def main():
    values = input('Enter a, b, c, d, e, f (seperated by comma): ')
    a,b,c,d,e,f = [float(v) for v in values.split(',')]
    solutionEq = compute2x2LinearEq(a,b,c,d,e,f)

    if isinstance(solutionEq, str):
        print (solutionEq)
    else:
        print ('x is %0.1f and y is %0.1f' % (solutionEq[0], solutionEq[1]))

main()
