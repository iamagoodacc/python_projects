from tkinter import *

def myfunction(event):
    x, y = event.x, event.y
    if canvas.old_coords:
        x1, y1 = canvas.old_coords
        canvas.create_line(x, y, x1, y1)
        #buttontest = Button(root, text = '', height = 1, width = 1)
        buttontest = Canvas(root, height = 1, width = 1)
        buttontest.place(x=x, y=y)
    canvas.old_coords = x, y

root = Tk()

canvas = Canvas(root, width=400, height=400)
canvas.pack()
canvas.old_coords = None

root.bind('<B1-Motion>', myfunction)
root.mainloop()
