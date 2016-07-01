# Liang 6.48

def format(num, width):
    newNum = ''
    for i in range(width - len(str(num))):
        newNum += '0'
    if num > 0:
        return newNum + str(num)
    else:
        return str(num)[0] + newNum + str(num)[1:len(str(num))]

def main():
    num = int(input('Enter a number: '))
    width = int(input('Enter the width: '))
    print (format(num, width))

if __name__ == '__main__':
    main()
