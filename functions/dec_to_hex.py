# Convert Hexadecimal to Decimal and vise versa
from tkinter import *

class Hex_Dec:
    def __init__(self):
        window = Tk()
        window.title('Decimal - Hexadecimal Convertor')
        self.hexVals = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

        # Entry
        Label(window, text='Enter a number').grid(row=2, column=1)
        self.value = StringVar()
        Entry(window, textvariable=self.value,
              justify=RIGHT).grid(row=2, column=2)

        # Radio Buttons
        self.radio = IntVar()
        Radiobutton(window, text='Hex -> Dec',
                    variable=self.radio, value=1).grid(row=1, column=1)        
        Radiobutton(window, text='Dec -> Hex',
                    variable=self.radio, value=2).grid(row=1, column=2)

        # Label
        self.text = ''
        self.newValue = ''
        self.label = Label(window, text=self.text)
        self.result = Label(window, text=self.newValue)
        self.label.grid(row=3, column=1, sticky=W)
        self.result.grid(row=3, column=2, sticky=E)

        # Button
        Button(window, text='Convert',
               command=self.computeValue).grid(row=4, column=2, sticky=W)
        window.mainloop()

    def hexToDec(self):
        nHex = self.value.get()
        dec = 0

        for i in range(len(nHex)):
            dec += self.hexVals.index(nHex[i])*16**(i)
        return dec
        
    def decToHex(self):
        dec = int(self.value.get())
        dgtHex = [] # Store dec value
        nHex = '' # Store final hex value
        
        while dec > 0:
            dgtHex.append(dec % 16)
            dec //= 16
        for i in range(len(dgtHex)):
            nHex += self.hexVals[dgtHex[-(i+1)]]
        return nHex
        
    def computeValue(self):
        self.result['fg'] = 'red'
        
        if self.radio.get() == 0:
            self.result['text'] = 'Select a conversion first!'    
        elif self.verifyValue() == True:
            self.result['fg'] = 'black'
            if self.radio.get() == 1:
                self.label['text'] ='Decimal'
                self.result['text'] = self.hexToDec()
            else:
                self.label['text'] = 'Hexadecimal'
                self.result['text'] = self.decToHex()   
        else:
            self.result['text'] = 'Invalid Number Entered!'

    def verifyValue(self):
        digts = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

        for v in self.value.get():
            if self.radio.get() == 1:
                if v not in self.hexVals:
                    return False
            else:
                if v not in self.hexVals[:10]:
                    return False
        return True

Hex_Dec()
