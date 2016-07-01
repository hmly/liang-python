from tkinter.filedialog import*

def copy(iname, oname):
    ifile = open(iname, 'ur')
    ofile = open(oname, 'uw')

    line = ifile.readline()
    while line != '':
        ofile.write(line)
        line = ifile.readline()
    
    ifile.close()
    ofile.close()

def main():
    infilename = askopenfilename()
    if infilename == '':
        return
    
    outfilename = askopenfilename()
    if outfilename == '':
        return

    copy(infilename, outfilename)

if __name__ == '__main__':
    main()
