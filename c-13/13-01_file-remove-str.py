# L 13.1

def removeString(file, string):
    data = ''
    infile = open(file, 'r')
    
    for line in infile:
        if string in line:
            line = line.replace(string, '')
        data += line
    infile.close()
    outfile = open(file, 'w')
    outfile.write(data)
    outfile.close()
    
    return 'Done'

def main():
    file = input('Enter a filename: ')
    string = input('Enter the string to be removed: ')
    print (removeString(file, string))

if __name__ == '__main__':
    main()
