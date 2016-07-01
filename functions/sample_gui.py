from tkinter import *

class sampleGUI:
    def __init__(self):
        self.count = 0
        self.window = Tk()
        self.button = Button(self.window,
                             text = 'Button',
                             fg = 'red',
                             command = self.do_button)
        self.button['bg'] = '#FFFF00'
        self.button.pack()
        self.label = Label(self.window,
                           text = 'Label')
        self.label.pack()

    def run(self):    
        self.window.mainloop()
        
    def do_button(self):
        pass

class Counter(sampleGUI):
    def __init__(self):
        super().__init__()
        self.button['text'] = 'Add'
        self.label['text'] = '0'
        self.count = 0

    def do_button(self):
        self.count += 1
        self.label['text'] = str(self.count)

Counter().run()

















        
