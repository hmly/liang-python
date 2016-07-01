# Liang 5.6

def mileToKilometer(mile):
    return mile * 1.609

def kilometerToMile(kilometer):
    return kilometer * 0.621

def main():
    print ('%-10s %-10s | %-12s %-10s' % ('Miles', 'Kilometers', 'Kilometers', 'Miles'))
    for i in range(20, 66):
        print ('%-10d %-10.3f | %-12d %-10.3f' % (i-19, mileToKilometer(i-19), i, kilometerToMile(i)))

main()
