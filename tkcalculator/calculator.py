from tkinter import *
from tkinter import messagebox

master = Tk()
master.title("Calculator")
master.geometry("208x345")
numbers = {
    "b1": "1",
    "b2": "2",
    "b3": "3",
    "b4": "4",
    "b5": "5",
    "b6": "6",
    "b7": "7",
    "b8": "8",
    "b9": "9",
    "b0": "0",
    "point": ".",
    "open_bracket": "(",
    "close_bracket": ")",
    "pi": "3.14",
}
operations = {
    "equals": "=",
    "add": "+",
    "subtract": "-",
    "times": "*",
    "divide": "/",
    "square": "**",
    "percentage": "%",
}
symbols = {"+": 1, "-": 1, "=": 0, "/": 2, "**": 3, "%": 2, "*": 2}
exceptions = {"screen": "nil"}
display_screen = ""
expression = ""
equation = ""
answer = "nil"

def parse_expression(expression):
    result = []
    num_buffer = ''

    for char in expression:
        if char.isdigit():
            num_buffer += char
        else:
            if num_buffer:
                result.append(num_buffer)
                num_buffer = ''
            result.append(char)

    if num_buffer:
        result.append(num_buffer)

    return result


def evaluate(expression):
    postfix = []
    operatorstack = []

    #Dijkstra's shunting yard algorithm to first convert to postfix
    for element in parse_expression(expression):
        if element.isnumeric():
            postfix.append(element)
        elif element == "(":
            operatorstack.append(element)
        elif element == ")":
            while operatorstack and operatorstack[-1] != '(':
                postfix.append(operatorstack.pop())
            operatorstack.pop() 
        elif element in symbols:
            if len(operatorstack) == 0:
                operatorstack.append(element)
            else:
                if operatorstack[-1] in symbols and symbols[operatorstack[-1]] >= symbols[element]: #if operator in stack is greater precendence
                    postfix.append(operatorstack.pop())
                    operatorstack.append(element)
                else:
                    operatorstack.append(element)
                        

    for operator in operatorstack: # anything left over
        postfix.append(operator)
    
    print(postfix)
    #now we got postfix lets evaluate it

    operand_stack = []
    for item in postfix:
        if item.isnumeric():
            operand_stack.append(int(item))
        else:
            right_operand = operand_stack.pop()
            left_operand = operand_stack.pop()
            if item == '+':
                operand_stack.append(left_operand + right_operand)
            elif item == '-':
                operand_stack.append(left_operand - right_operand)
            elif item == '*':
                operand_stack.append(left_operand * right_operand)
            elif item == "**":
                operand_stack.append(left_operand ** right_operand)
            elif item == '/':
                operand_stack.append(left_operand / right_operand)

    return operand_stack.pop()


    

def number(button, num, operation):
    global expression
    if num in numbers:
        print(numbers[num])
        if len(screen["text"]) >= 25:
            print("too many numbers")
        else:
            expression += numbers[num]
            screen["text"] = expression
    if operation == "nil":
        pass
    else:
        if operation == "equals":
            result = str(evaluate(expression))
            screen["text"] = result
            expression = result
        elif operation == "clear":
            expression = ""
            screen["text"] = ""
        elif operation == "delete":
            expression = expression[:-1]
            screen["text"] = expression
        else:
            if screen["text"] == "":
                pass
            else:
                if screen["text"][-1] in symbols:
                    pass
                else:
                    if operation == "percentage":
                        screen["text"] = screen["text"][:-1] + str(
                            int(screen["text"][-1]) / 100
                        )
                        expression = screen["text"]
                    else:
                        expression += operations[operation]
                        screen["text"] = expression


screen = Button(master, text="", anchor=W, height=3, width=28)
b1 = Button(
    master, text="1", height=2, width=6, command=lambda: number(b1, "b1", "nil")
)
b2 = Button(
    master, text="2", height=2, width=6, command=lambda: number(b2, "b2", "nil")
)
b3 = Button(
    master, text="3", height=2, width=6, command=lambda: number(b3, "b3", "nil")
)
b4 = Button(
    master, text="4", height=2, width=6, command=lambda: number(b4, "b4", "nil")
)
b5 = Button(
    master, text="5", height=2, width=6, command=lambda: number(b5, "b5", "nil")
)
b6 = Button(
    master, text="6", height=2, width=6, command=lambda: number(b6, "b6", "nil")
)
b7 = Button(
    master, text="7", height=2, width=6, command=lambda: number(b7, "b7", "nil")
)
b8 = Button(
    master, text="8", height=2, width=6, command=lambda: number(b8, "b8", "nil")
)
b9 = Button(
    master, text="9", height=2, width=6, command=lambda: number(b9, "b9", "nil")
)
b0 = Button(
    master, text="0", height=2, width=6, command=lambda: number(b0, "b0", "nil")
)
subtract = Button(
    master,
    text="-",
    height=2,
    width=6,
    command=lambda: number(subtract, "subtract", "subtract"),
)

add = Button(
    master, text="+", height=2, width=6, command=lambda: number(add, "add", "add")
)

equals = Button(
    master,
    text="=",
    height=2,
    width=6,
    command=lambda: number(equals, "equals", "equals"),
)

times = Button(
    master, text="x", height=2, width=6, command=lambda: number(times, "times", "times")
)

divide = Button(
    master,
    text="÷",
    height=2,
    width=6,
    command=lambda: number(divide, "divide", "divide"),
)

square = Button(
    master,
    text="x^y",
    height=2,
    width=6,
    command=lambda: number(square, "square", "square"),
)

clear = Button(
    master, text="C", height=2, width=6, command=lambda: number(clear, "clear", "clear")
)

delete = Button(
    master,
    text="⌫",
    height=2,
    width=6,
    command=lambda: number(delete, "delete", "delete"),
)

point = Button(
    master, text=".", height=2, width=6, command=lambda: number(point, "point", "nil")
)

open_bracket = Button(
    master,
    text="(",
    height=2,
    width=6,
    command=lambda: number(open_bracket, "open_bracket", "nil"),
)

close_bracket = Button(
    master,
    text=")",
    height=2,
    width=6,
    command=lambda: number(close_bracket, "close_bracket", "nil"),
)

pi = Button(
    master, text="π", height=2, width=6, command=lambda: number(pi, "pi", "nil")
)

percentage = Button(
    master,
    text="%",
    height=2,
    width=6,
    command=lambda: number(percentage, "percentage", "percentage"),
)


screen.grid(row=0, column=0, padx=1, sticky=W)

b1.grid(row=3, column=0, sticky=W)
b2.grid(row=3, column=0, padx=52, sticky=W)
b3.grid(row=3, column=0, padx=104, sticky=W)
b4.grid(row=4, column=0, sticky=W)
b5.grid(row=4, column=0, padx=52, sticky=W)
b6.grid(row=4, column=0, padx=104, sticky=W)
b7.grid(row=5, column=0, sticky=W)
b8.grid(row=5, column=0, padx=52, sticky=W)
b9.grid(row=5, column=0, padx=104, sticky=W)
b0.grid(row=6, column=0, padx=52, sticky=W)

percentage.grid(row=1, column=0, padx=0, sticky=W)
pi.grid(row=1, column=0, padx=52, sticky=W)
open_bracket.grid(row=2, column=0, sticky=W)
close_bracket.grid(row=2, column=0, padx=52, sticky=W)
delete.grid(row=1, column=0, padx=156, sticky=W)
clear.grid(row=1, column=0, padx=104, sticky=W)
square.grid(row=2, column=0, padx=104, sticky=W)
divide.grid(row=2, column=0, padx=156, sticky=W)
times.grid(row=3, column=0, padx=156, sticky=W)
subtract.grid(row=4, column=0, padx=156, sticky=W)
add.grid(row=5, column=0, padx=156, sticky=W)
equals.grid(row=6, column=0, padx=156, sticky=W)
point.grid(row=6, column=0, padx=104, sticky=W)
master.mainloop()
