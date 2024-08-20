def fizz_buzz(inpt):
    if ((inpt % 3) == 0) and ((inpt % 5) != 0):
        return 'Fizz'
    elif ((inpt % 5) == 0) and ((inpt % 3) != 0):
        return 'Buzz'
    elif ((inpt % 3) == 0) and ((inpt % 5) == 0):
        return 'Fizz_Buzz'
    else:
        return inpt

print(fizz_buzz(7))
