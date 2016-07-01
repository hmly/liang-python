# Liang 9.19
from tkinter import *

class animateCircle:
    def __init__(self):
        window = Tk()
        window.title('Keyboard Movable Circle')
        WIDTH = 800
        HEIGHT = 400
        LENGTH = 50
        self.x1 = WIDTH // 2.1
        self.y1 = HEIGHT // 2.3
        self.x2 = WIDTH // 2.1 + LENGTH
        self.y2 = HEIGHT // 2.3 + LENGTH

        # Canvas
        frame = Frame(window)
        frame.pack()
        self.canvas = Canvas(frame, width=WIDTH, height=HEIGHT, bg='white')
        window.bind('<Left>', self.move)
        window.bind('<Right>', self.move)
        window.bind('<Up>', self.move)
        window.bind('<Down>', self.move)
        self.canvas.create_text(self.x1 + 30, self.y1 + 20, font=('Old English Text MT', 20),
                                text='Welcome', tags='intro')
        self.canvas.create_text(self.x1 + 30, self.y1 + 40, font=('Monotype Corsiva', 14),
                                text='Press any arrow keys to start', tags='intro')
        self.canvas.pack()
        window.mainloop()

    def move(self, event):
        MOVEDIST = 20
        self.canvas.delete('circle', 'intro')
        
        if event.keysym == 'Left':
            self.x1 -= MOVEDIST
            self.x2 -= MOVEDIST
            self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, tags='circle')
        elif event.keysym == 'Right':
            self.x1 += MOVEDIST
            self.x2 += MOVEDIST
            self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, tags='circle')
        elif event.keysym == 'Up':
            self.y1 -= MOVEDIST
            self.y2 -= MOVEDIST
            self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, tags='circle')
        else:
            self.y1 += MOVEDIST
            self.y2 += MOVEDIST
            self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, tags='circle')
        
animateCircle()
