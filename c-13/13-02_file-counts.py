# L 13.2

def countCharWordLine(file):
    infile = open(file, 'r')
    charCount = wordCount = lineCount = 0
    for line in infile:
        charCount += len(line)
        wordCount += len(line.split())
        lineCount += 1
    infile.close()
    return [charCount, wordCount, lineCount]
    
def main():
    file = input('Enter a filename: ')
    counts = countCharWordLine(file)
    print ('%d characters \n%d words \n%d lines' % (counts[0], counts[1], counts[2]))

if __name__ == '__main__':
    main()
