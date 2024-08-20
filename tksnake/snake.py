from tkinter import *
import random
master = Tk()

gameWidth = 30
gameHeight = 30
tilesize = 10
snakelength = 3
Locked = False
lockkey = ''

class Snake():
    def __init__(self):
        self.snakeX = [20,20,20]
        self.snakeY = [20,21,22] # variables
        self.key = 'w'
        self.points = 0
    def checkGameOver(self):
        for i in range(1, snakelength, 1):
            if self.snakeY[0] == self.snakeY[i] and self.snakeX[0] == self.snakeX[i]:
                return True # colliding with self
        if self.snakeX[0] < 0 or self.snakeX[0] >= gameWidth or self.snakeY[0] < 0 or self.snakeY[0] >= gameHeight:
            return True # out of bounds
        return False
    def eatApple(self):
        global snakelength
        if self.snakeX[0] == apple.getCordX() and self.snakeY[0] == apple.getCordY():
            #for i in range(120):
            snakelength = snakelength + 1
            x = self.snakeX[len(self.snakeX)-1]
            y = self.snakeY[len(self.snakeY)-1]
            self.snakeX.append(x+1)
            self.snakeY.append(y)
            self.points = self.points + 1
            apple.spawn()
    def getCordX(self, index):
        return self.snakeX[index]
    def getCordY(self, index):
        return self.snakeY[index]
    def getPoints(self):
        return self.points
    def getKey(self, event):
        global lockkey
        if event.char == "w" or event.char == "d" or event.char == "s" or event.char == "a" or event.char == " ":
            if event.char != lockkey:
                self.key = event.char
                
    def move(self):
        global lockkey
        for i in range(snakelength - 1, 0, -1): # snake length handler
                self.snakeX[i] = self.snakeX[i-1]
                self.snakeY[i] = self.snakeY[i-1]
        if self.key == "w":
            lockkey = 's'
            self.snakeY[0] = self.snakeY[0] - 1
        elif self.key == "s":
            lockkey = 'w'
            self.snakeY[0] = self.snakeY[0] + 1
        elif self.key == "a":
            lockkey = 'd'
            self.snakeX[0] = self.snakeX[0] - 1
        elif self.key == "d":
            lockkey = 'a'
            self.snakeX[0] = self.snakeX[0] + 1
        self.eatApple()
class Apple():
    def __init__(self):
        self.appleX = random.randint(1, gameWidth - 2)
        self.appleY = random.randint(1, gameHeight - 2)
    def getCordX(self):
        return self.appleX
    def getCordY(self):
        return self.appleY
    def spawn(self):
        self.appleX = random.randint(1, gameWidth - 2)
        self.appleY = random.randint(1, gameHeight - 2)
class MainLoop():
    def repaint(self):
        global Locked
        canvas.after(200, self.repaint)
        canvas.delete(ALL)
        snake.move()
        if snake.checkGameOver() == False and not Locked:
            canvas.create_rectangle(snake.getCordX(0) * tilesize,
                                    snake.getCordY(0) * tilesize,
                                    snake.getCordX(0) * tilesize + tilesize,
                                    snake.getCordY(0) * tilesize + tilesize,
                                    fill="dark green")
            for i in range(1, snakelength, 1):
                canvas.create_rectangle(snake.getCordX(i)* tilesize,
                                    snake.getCordY(i)* tilesize,
                                    snake.getCordX(i)* tilesize + tilesize,
                                    snake.getCordY(i)* tilesize + tilesize,
                                    fill = 'green')
            canvas.create_rectangle(apple.getCordX() * tilesize,
                                    apple.getCordY() * tilesize,
                                    apple.getCordX() * tilesize + tilesize,
                                    apple.getCordY() * tilesize + tilesize,
                                    fill="red")
        else:
            canvas.delete(ALL)
            Locked = True
            canvas.create_text(150,
                               120,
                               fill="grey",
                               font=("Cartoon", 20),
                               text=f"GAME OVER\nFinal Points: {snake.getPoints()}")

snake = Snake()
game = MainLoop()
apple = Apple()
canvas = Canvas(master, width=300, height=300, bd= 0, highlightcolor = 'black', borderwidth=0, relief='solid', bg = 'white')
canvas.pack()

game.repaint()
master.title = 'Snake game'
master.bind('<KeyPress>', snake.getKey)
master.mainloop()
