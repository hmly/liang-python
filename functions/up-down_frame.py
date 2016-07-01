from tkinter import *

class UpDown:
    def __init__(self):
        self.window = Tk()
        self.window.title('UpDown Counter')

        self.topFrame = Frame(self.window)
        self.topFrame.pack()
        
        self.button = Button(self.topFrame,
                             text = 'Add',
                             fg = 'red',
                             command = self.do_button)
        self.button['bg'] = '#FFFF00'
        self.button.pack(side=LEFT)

        self.radio = IntVar(value = 0)
        Radiobutton(self.topFrame,
                    variable = self.radio,
                    value = 0, text = '[+]',
                    command = self.reLabel).pack(side=LEFT)
        Radiobutton(self.topFrame,
                    variable = self.radio,
                    value = 1, text = '[-]',
                    command = self.reLabel).pack(side=LEFT)
        
        self.bottomFrame = Frame(self.window)
        self.bottomFrame.pack()
        
        self.label = Label(self.buttonFrame,
                           text = 'Result: ').pack(side=LEFT)
        self.label = Label(self.bottomFrame,
                           text = '0').pack(side=LEFT)
        self.count = 0

    def run(self):    
        self.window.mainloop()

    def reLabel(self):
        if self.radio.get() == 0:
            self.button['text'] = 'Add'
        else:
            self.button['text'] = 'Substract'
        
    def do_button(self):
        if self.radio.get() == 0:
            self.count += 1
        else:
            self.count -= 1
        self.label['text'] = str(self.count)

UpDown().run()

















        
