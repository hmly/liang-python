# Liang 9.7
from tkinter import *

class Grid():
    def __init__(self):
        MAX = 8
        SIZE = 40
        window = Tk()
        window.title('Colored 8x8 Grid')

        self.canvas = Canvas(window, width=320, height=320, bg='white')
        self.canvas.pack()

        for i in range(1, MAX):
            for j in range(1, MAX):
                self.canvas.create_line(j*SIZE, 0, j*SIZE, (i+1)*SIZE, fill='red')
            self.canvas.create_line(0, i*SIZE, MAX*SIZE, i*SIZE, fill='blue')

        window.mainloop()
Grid()
                
        
