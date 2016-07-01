# Liang 4.11

def computeDaysInMonth(m, year):
    months = ('January', 'February', 'March', 'April', 'May', 'June', 'July',\
              'August', 'September', 'October', 'November', 'December')
    if months[m-1] in ['January', 'March', 'May', 'July', 'August', 'October', 'December']:
        return '%s %d has %d days' % (months[m-1], year, 31)
    elif months[m-1] in ['April', 'June', 'September', 'November']:
        return '%s %d has %d days' % (months[m-1], year, 30)
    else:
        if (year % 4 == 0  and year % 100 != 0) or (year % 400 == 0):
            return '%s %d has %d days' % (months[m-1], year, 29)
        else:
            return '%s %d has %d days' % (months[m-1], year, 28)

def main():
    userInputs = input('Enter a month and a year (1=January and 12=December e.g. 1, 2014): ')
    month, year = [int(v) for v in userInputs.split(',')]
    print (computeDaysInMonth(month, year))

main()
