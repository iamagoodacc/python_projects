import random
from tkinter import *
from tkinter import messagebox as msgbox
parts = ['the water is absorbed by the root hairs in the plant', 'it is transported into the roots', 'then transported to the xylem in the vascular bundle', 'water moves from the xylem into the mesophyll cells', 'the water evaporates from the surfaces of the mesophyll cells', 'the water leaves the plant by diffusion through the stomata']
complete = {parts[0]: '1', parts[1]: '2', 'then transported to the xylem in the vascular bundle': '3', 'water moves from the xylem into the mesophyll cells': '4', 'the water evaporates from the surfaces of the mesophyll cells': '5', 'the water leaves the plant by diffusion through the stomata': '6'}
placeholder = [1, 2, 3, 4, 5, 6]
numbers = [1, 2, 3, 4, 5, 6]
master = Tk()
master.geometry('450x250')
status = 0
correct = 0
results = ''
def check():
    global results
    global correct
    for part in buttonparts:
        if part['text'] == buttonparts[part]:
            correct += 1
    if correct == 6:
        print('all correct')
        print(f'{correct}/6 correct')
        result['text'] = f'{correct}/6 correct'
    else:
        print(f'{correct}/6 correct')
        result['text'] = str(correct)+'/6 correct'
def click(button, mainbutton):
    global status
    status += 1
    button['text'] = status
    mainbutton['state'] = 'disabled'
    if status == 6:
        check()

part1 = Button(master, text = parts[0], command = lambda: click(check1, part1))
check1 = Button(master, text = '', width = 3)
part2 = Button(master, text = parts[1], command = lambda: click(check2, part2))
check2 = Button(master, text = '', width = 3)
part3 = Button(master, text = parts[2], command = lambda: click(check3, part3))
check3 = Button(master, text = '', width = 3)
part4 = Button(master, text = parts[3], command = lambda: click(check4, part4))
check4 = Button(master, text = '', width = 3)
part5 = Button(master, text = parts[4], command = lambda: click(check5, part5))
check5 = Button(master, text = '', width = 3)
part6 = Button(master, text = parts[5], command = lambda: click(check6, part6))
check6 = Button(master, text = '', width = 3)

buttonparts = {check1: 1, check2: 2, check3: 3, check4: 4, check5: 5, check6: 6}

result = Button(master, text = '', width = 42)
result.grid(row = 0, column = 1, padx = 70, sticky = W)

ranrow = random.choice(numbers)
part1.grid(row = ranrow, column = 1, padx = 100, sticky = W)
check1.grid(row = ranrow, column = 1, padx = 70, stick = W)
numbers.remove(ranrow)
ranrow = random.choice(numbers)
part2.grid(row = ranrow, column = 1, padx = 100, sticky = W)
check2.grid(row = ranrow, column = 1, padx = 70, stick = W)
numbers.remove(ranrow)
ranrow = random.choice(numbers)
part3.grid(row = ranrow, column = 1, padx = 100, sticky = W)
check3.grid(row = ranrow, column = 1, padx = 70, stick = W)
numbers.remove(ranrow)
ranrow = random.choice(numbers)
part4.grid(row = ranrow, column = 1, padx = 100, sticky = W)
check4.grid(row = ranrow, column = 1, padx = 70, stick = W)
numbers.remove(ranrow)
ranrow = random.choice(numbers)
part5.grid(row = ranrow, column = 1, padx = 100, sticky = W)
check5.grid(row = ranrow, column = 1, padx = 70, stick = W)
numbers.remove(ranrow)
ranrow = random.choice(numbers)
part6.grid(row = ranrow, column = 1, padx = 100, sticky = W)
check6.grid(row = ranrow, column = 1, padx = 70, stick = W)
numbers.remove(ranrow)

master.mainloop()
