from tkinter import *
from tkinter import messagebox as msgb
import time
import random
import math
import threading

cords = ''
main = Tk()
main.geometry('1000x600')
x = ''
y = ''
he = 1
finish = True
timeset = 2
randx = random.randint(1,1200)
randy = random.randint(1,700)
randsize = random.randint(6,20)
score = 0

def complete():
    global finish
    if finish == True:
        finish = False
        print('finish')
def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y
def makebutton(btext, bheight, bwidth):
    createbutton = Button(main, text = btext, height = bheight, width = bwidth)
    createbutton.pack()
def gameover():
    print('time gone')
    msgb.showerror(title = 'Game Messge', message = f'GAME OVER! Your final score was {score}')

def timeconfig():
    global timeset
    while True:
        if timeset != 0:
            main.update()
            time.sleep(1)
            main.update()
            timeset -= 1
        else:
            gameover()
            break
def on_drag_motion(event):
    global cords, timeset
    global x,y
    global he,finish, score
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)
    cords = x,y
    cord.config(text = str(x)+','+str(y))
    if x in range(1, 20) and y in range(1, 20):
        he += 1
    if x in range((cord.winfo_x() - (cord['width'])),((cord.winfo_x() + 13*(cord['width'])))) and y in range((cord.winfo_y() - (cord['height'])),((cord.winfo_y()) + 13*(cord['height']))) and timeset != 0:
        complete()
        score += 1
        status.config(text = 'score: '+str(score))
        randx = random.randint(1,1200)
        randy = random.randint(1,700)
        randsize = random.randint(6,20)
        cord.place(x = randx, y = randy)
        cord.config(width = randsize + 1, height = int(round(randsize/2)))
        timeset = 2
       
timer = Button(main, text = '', width = 10)
status = Button(main, text = '', width = 10)
cord = Label(main, text = '', bg = 'grey', width = randsize + 1, height = int(round(randsize/2)))
button = Label(main, bd=4, bg="black", height = 1, width = 2)
button.place(x=10, y=10)
status.place(x = 490, y = 0)
cord.place(x = randx, y = randy)
make_draggable(button)
threading.Thread(target = timeconfig).start()

main.mainloop()

