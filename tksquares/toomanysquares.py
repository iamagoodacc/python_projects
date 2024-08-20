#!/usr/bin/env python3
from tkinter import *
from functools import partial
from itertools import product

positions = product(range(10), range(10))
button_ids = []; coords = []

def change(i):
    bname = (button_ids[i])
    bname.destroy()
    # destroy another button by coordinates
    # (next to the current one in this case)
    button_nextto = coords[i]
    button_nextto = (button_nextto[0] + 1, button_nextto[1])
    hide_by_coords(button_nextto)

def hide_by_coords(xy):
    # this function can destroy a button by coordinates
    # in the matrix (topleft = (0, 0). Argument is a tuple
    try:
        index = coords.index(xy)
        button = button_ids[index]
        button.destroy()
    except (IndexError, ValueError):
        pass

win = Tk()
frame = Frame(win)
frame.pack()

for i in range(10):
    # shape the grid
    setsize = Canvas(frame, width=30, height=0).grid(row=11, column=i)
    setsize = Canvas(frame, width=0, height=30).grid(row=i, column=11)

for i, item in enumerate(positions):
    button = Button(frame, command=partial(change, i))
    button.grid(column=item[0], row=item[1], sticky="n,e,s,w")
    button_ids.append(button)
    coords.append(item)

win.minsize(width=270, height=270)
win.title("Too many squares")
win.mainloop()

