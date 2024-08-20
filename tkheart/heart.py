from tkinter import *
import time
master = Tk()
master.geometry('500x500+500+100')
finaltext = """
    $$$$         $$$$
    $$$$$$$$     $$$$$$$$
    $$$$$$$$$$$$ $$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$
    $$$$$$$
    $$$
    $
"""
heart = """
     $$$$         $$$$
   $$$$$$$$     $$$$$$$$
 $$$$$$$$$$$$ $$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$
 $$$$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$
          $$$$$$$
            $$$
             $
"""
text = ''
def click():
    global text
    for letter in finaltext:
        text = text + letter
        displaytext['text'] = text
        master.update()
        time.sleep(0.03)
        master.update()
displaytext = Label(master, text = '', width = 67, height = 30, font=("Courier", 20))
#displaytext.place(x = 5, y = 5)
time.sleep(1)
click()
master.mainloop()
