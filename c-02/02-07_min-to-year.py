# Liang 2.7

def minutesToYearsDays(mins):
    days = mins//60//24
    years = days // 365
    remainDays = days % 365
    
    print (mins, 'minutes is approximately', years,\
           ('years' if years > 1 else 'year'), 'and',\
           remainDays, ('days' if days > 1 else 'day'))

def main():
    minutes = int(input('Enter the number of minutes(e.g. 100): '))
    minutesToYearsDays(minutes)

main()
