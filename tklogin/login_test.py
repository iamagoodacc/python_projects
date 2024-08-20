from tkinter import *
import random
master = Tk()

#Essentials
LCharacters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UCharacters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Punctuation = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '/', '<', '=', '>', '?', '@', '[', '\\', ']', '_', '{', '|', '}']
CharacterSets = [LCharacters, UCharacters, Numbers, Punctuation]

allowedChars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_']
ConfirmPasswordEntry = None
Confirm = None
Visible = False

def randomPass():
    global Visible, RandomPass, Signup, Login, Username, UsernameEntry, Password, PasswordEntry, Errors, Home, Confirm, ConfirmPasswordEntry
    Length = 10
    GeneratedPass = ''
    for i in range(Length):
        CharacterSet = random.choice(CharacterSets)
        Character = random.choice(CharacterSet)
        #print(Character)
        GeneratedPass = GeneratedPass + Character
    PasswordEntry.delete(0,"end")
    PasswordEntry.insert(0, GeneratedPass)
    ConfirmPasswordEntry.delete(0,"end")
    ConfirmPasswordEntry.insert(0, GeneratedPass)
    Visible = False
    passVisible()
    print(GeneratedPass)
    
def validUser(Username, Password, data):
    for line in data:
        User = line.split(',')
        CUsername = User[0].split('-')
        CPassword = User[1].split('-')
        if str(Username) == str(CUsername[1]):
            if str(Password) == str(CPassword[1].strip()):
                return True
    return False
    

def validName(Username):
    for character in Username:
        if str(character) not in allowedChars:
            return False
    return True

def passVisible():
    global PasswordEntry, Visible, ConfirmPasswordEntry
    if Visible == False:
        Visible = True
        PasswordEntry.configure(show='')
    elif Visible == True:
        Visible = False
        PasswordEntry.configure(show='*')

def logIn():
    global RandomPass, Signup, Login, Username, UsernameEntry, Password, PasswordEntry, Errors, Home, Confirm, ConfirmPasswordEntry
    if UsernameEntry == None:
        clearScreen()
        Username = Label(master, text="Username")
        Password = Label(master, text="Password")
        Login = Button(master, text = 'Log in', width = 8, height = 1, command = lambda: logIn())
        UsernameEntry = Entry(master)
        PasswordEntry = Entry(master, show = '*')
        Errors = Label(master, text = '', width = 26, height = 1)
        Home = Button(master, text = 'Home', width = 8, height = 1, command = lambda: homePage())

        Home.grid(row=3, column=0, sticky = 'W')
        UsernameEntry.grid(row=1, column=1, sticky = 'W', padx = 18)
        PasswordEntry.grid(row=2, column=1, sticky = 'W', padx = 18)
        Username.grid(row=1, sticky = 'W')
        Password.grid(row=2, sticky = 'W')
        Login.grid(row=3, column=1, sticky = 'W', padx = 46)
        Errors.config(font=('TkTextFont', 10))
        Errors.grid(row=0, column=0, sticky = 'W', columnspan=4)
        
    file = open('users.txt','r')
    data = file.readlines()
    file.close()
    GotUsername = UsernameEntry.get()
    GotPassword = PasswordEntry.get()
    if GotUsername == '' or GotPassword == '': return
    if validUser(GotUsername, GotPassword, data):
        Errors['text'] = 'Logged in'
        print('Successfully logged in')
    elif not validUser(GotUsername, GotPassword, data):
        Errors['text'] = 'Password incorrect'
        print('Password incorrect')
def signUp():
    global ShowPass, RandomPass, Signup, Login, Username, UsernameEntry, Password, PasswordEntry, Errors, Home, Confirm, ConfirmPasswordEntry

    if ConfirmPasswordEntry == None:
        clearScreen()
        Username = Label(master, text="Username")
        Password = Label(master, text="Password")
        Signup = Button(master, text = 'Sign up', width = 8, height = 1 , command = lambda: signUp())
        Login = Button(master, text = 'Log in', width = 8, height = 1, command = lambda: logIn())
        UsernameEntry = Entry(master)
        PasswordEntry = Entry(master, show = '*')
        Errors = Label(master, text = '', width = 26, height = 1)
        ShowPass = Button(master, text = '●', image=pixelVirtual, compound='c', width = 12, height = 12, command = lambda: passVisible())
        RandomPass = Button(master, text = 'R', image=pixelVirtual, compound='c', width = 12, height = 12, command = lambda: randomPass())
        ConfirmPasswordEntry = Entry(master, show = '*')
        Confirm = Label(master, text="Confirm Pass")
        Home = Button(master, text = 'Home', width = 8, height = 1, command = lambda: homePage())

        Home.grid(row=4, column=0, sticky = 'W')
        ShowPass.grid(row=2, column=1, sticky = 'W', padx = 161, pady = 1)
        RandomPass.grid(row=2, column=1, sticky = 'W', padx = 141, pady = 1)
        UsernameEntry.grid(row=1, column=1, sticky = 'W', padx = 18)
        PasswordEntry.grid(row=2, column=1, sticky = 'W', padx = 18)
        Username.grid(row=1, sticky = 'W')
        Password.grid(row=2, sticky = 'W')
        Confirm.grid(row=3, sticky = 'W', columnspan=2)
        ConfirmPasswordEntry.grid(row=3, column=1, sticky = 'W', padx = 18)
        Signup.grid(row=4, column=1, sticky = 'W', padx = 46)
        Errors.config(font=('TkTextFont', 10))
        Errors.grid(row=0, column=0, sticky = 'W', columnspan=4)
    
    foundUser = False
    GotUsername = UsernameEntry.get()
    GotPassword = PasswordEntry.get()
    ConfirmPass = ConfirmPasswordEntry.get()
    if GotUsername == '' or GotPassword == '' or ConfirmPass == '': return
    if ConfirmPass != GotPassword:
        Errors['text'] = "Confirm pass doesn't match"
        print('Confirm password and password do not match')
        foundUser = True
    file = open('users.txt','r')
    data = file.readlines()
    file.close()
    file = open('users.txt','a')
    for line in data:
        User = line.split(',')
        CUsername = User[0].split('-')
        CPassword = User[1].split('-')
        if not foundUser and not validName(GotUsername):
            Errors['text'] = 'Username invalid!'
            print('Username can only contain letters, number and one underscore')
            foundUser = True
        if not foundUser and str(GotUsername) == str(CUsername[1]):
            Errors['text'] = 'Username already in use!'
            print('Username already used!')
            foundUser = True
        elif not foundUser and len(str(GotUsername)) < 3:
            Errors['text'] = 'Username length too short'
            print('Username length too short')
            foundUser = True
        elif not foundUser and len(str(GotUsername)) > 25:
            Errors['text'] = 'Username length too long'
            print('Username length too long')
            foundUser = True
        elif not foundUser and len(str(GotPassword)) < 5:
            Errors['text'] = 'Password length too short'
            print('Password length too short')
            foundUser = True
        elif not foundUser:
            Errors['text'] = 'Created new account'
            foundUser = False
    if not foundUser:
        print(GotUsername)
        file.write(f'Username-{GotUsername},Password-{GotPassword}')
        file.write('\n')
    file.close()
def clearScreen():
    global ShowPass, RandomPass, Signup, Login, Username, UsernameEntry, Password, PasswordEntry, Errors, Home, Confirm, ConfirmPasswordEntry
    if Signup:
        Signup.destroy()
        Signup = None
    if Login:
        Login.destroy()
        Login = None
    if UsernameEntry:
        Username.destroy()
        Username = None
        UsernameEntry.destroy()
        UsernameEntry = None
    if PasswordEntry:
        Password.destroy()
        Password = None
        PasswordEntry.destroy()
        PasswordEntry = None
    if Errors:
        Errors.destroy()
        Errors = None
    if ConfirmPasswordEntry:
        Confirm.destroy()
        Confirm = None
        ConfirmPasswordEntry.destroy()
        ConfirmPasswordEntry = None
    if Home:
        Home.destroy()
        Home = None
    if RandomPass:
        RandomPass.destroy()
        RandomPass = None
    if ShowPass:
        ShowPass.destroy()
        ShowPass = None
def homePage():
    global RandomPass, Signup, Login, Username, UsernameEntry, Password, PasswordEntry, Errors, Home, Confirm, ConfirmPasswordEntry
    clearScreen()
    Signup = Button(master, text = 'Sign up', width = 8, height = 1 , command = lambda: signUp())
    Login = Button(master, text = 'Log in', width = 8, height = 1, command = lambda: logIn())

    Login.grid(row=4, column=0, sticky = 'W', padx = 50)
    Signup.grid(row=5, column=0, sticky = 'W', padx = 50)

pixelVirtual = PhotoImage(width=1, height=1)
Username = Label(master, text="Username")
Password = Label(master, text="Password")
Signup = Button(master, text = 'Sign up', width = 8, height = 1 , command = lambda: signUp())
Login = Button(master, text = 'Log in', width = 8, height = 1, command = lambda: logIn())
UsernameEntry = Entry(master)
PasswordEntry = Entry(master, show = '*')
ShowPass = Button(master, text = '●', image=pixelVirtual, compound='c', width = 12, height = 12, command = lambda: passVisible())
RandomPass = Button(master, text = 'R', image=pixelVirtual, compound='c', width = 12, height = 12, command = lambda: randomPass())
Errors = Label(master, text = '', width = 26, height = 1)
ConfirmPasswordEntry = Entry(master, show = '*')
Confirm = Label(master, text="Confirm Pass")
Home = Button(master, text = 'Home', width = 8, height = 1, command = lambda: homePage())

ShowPass.grid(row=2, column=1, sticky = 'W', padx = 161, pady = 1)
RandomPass.grid(row=2, column=1, sticky = 'W', padx = 141, pady = 1)
Home.grid(row=4, column=0, sticky = 'W')
UsernameEntry.grid(row=1, column=1, sticky = 'W', padx = 18)
PasswordEntry.grid(row=2, column=1, sticky = 'W', padx = 18)
Username.grid(row=1, sticky = 'W')
Password.grid(row=2, sticky = 'W')
Confirm.grid(row=3, sticky = 'W', columnspan=2)
ConfirmPasswordEntry.grid(row=3, column=1, sticky = 'W', padx = 18)
Signup.grid(row=4, column=1, sticky = 'W', padx = 46)
#Errors.config(font=('lucida 20 bold italic', 10))
Errors.config(font=('TkTextFont', 10))
Errors.grid(row=0, column=0, sticky = 'W', columnspan=4)

master.mainloop()
