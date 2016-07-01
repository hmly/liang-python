# Liang 9.3
from tkinter import *

class GeometricShapes:
    def __init__(self):
        window = Tk()
        window.title('Select Geometric Shapes')
        self.width = 400
        self.height = 100
        
        frame1 = Frame(window)
        frame1.pack()
        self.canvas = Canvas(frame1, width=self.width, height=self.height, bg='white')
        self.canvas.pack()
        
        frame2 = Frame(window)
        frame2.pack()
        self.radio = IntVar()
        self.cButton = IntVar()
        Radiobutton(frame2, text='Rectangle', variable=self.radio,
                    value=1, command=self.drawShape).grid(row=1, column=1)
        Radiobutton(frame2, text='Oval', variable=self.radio,
                    value=2, command=self.drawShape).grid(row=1, column=2)
        Checkbutton(frame2, text='Fill', variable=self.cButton,
                    command=self.drawShape).grid(row=1, column=3)
        window.mainloop()

    def drawShape(self):
        DIST = 20
        color = 'white'
        self.clearCanvas()

        if self.cButton.get() == 1:
            color = 'gold'
        
        if self.radio.get() == 1:
            self.canvas.create_rectangle(DIST, DIST, self.width-DIST, self.height-DIST,
                                         fill=color, tags='rect')
        elif self.radio.get() == 2:
            self.canvas.create_oval(DIST, DIST, self.width-DIST, self.height-DIST,
                                    fill=color, tags='oval')

    def clearCanvas(self):
        self.canvas.delete('rect', 'oval')


GeometricShapes()
