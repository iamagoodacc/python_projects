import re


def main(doc):
    currentdirection = "up"
    currentpos = [0,0]
    positions = 1 #1 for the initial point
    map = []

    for i, line in enumerate(doc): #create boolean map
        array = []
        for char in line:
            if char == "^":
                currentpos = [line.index(char), i] #x,y pos
            array.append(False)
        map.append(array)
    while True:
        if currentpos[0] >= len(doc[0])-1:
            break
        if currentpos[1] >= len(doc)-1:
            break
        if currentpos[0] <= 0:
            print(currentpos)
            break
        if currentpos[1] <= 0:
            break
        if currentdirection == "up":
            if currentpos[1]-1 >= 0 and doc[currentpos[1]-1][currentpos[0]] == "#": #rotate 90
                currentdirection = "right"
            else:
                currentpos[1] -= 1
            map[currentpos[1]][currentpos[0]] = True
        elif currentdirection == "down":
            if currentpos[1]+1 <= len(doc)-1 and doc[currentpos[1]+1][currentpos[0]] == "#": #rotate 90
                currentdirection = "left"
            else:
                currentpos[1] += 1
            map[currentpos[1]][currentpos[0]] = True
        elif currentdirection == "right":
            if currentpos[0]+1 <= len(doc[0]) and doc[currentpos[1]][currentpos[0]+1] == "#": #rotate 90
                currentdirection = "down"
            else:
                currentpos[0] += 1
            map[currentpos[1]][currentpos[0]] = True
        elif currentdirection == "left":
            if currentpos[0]-1 >= 0 and doc[currentpos[1]][currentpos[0]-1] == "#": #rotate 90
                currentdirection = "up"
            else:
                currentpos[0] -= 1
            map[currentpos[1]][currentpos[0]] = True
    
    for row in map:
        for bool in row:
            if bool:
                positions += 1
    
    return positions
    

if __name__ == "__main__":
    with open("input.txt") as file:
        document = [line.strip() for line in file]
    result = main(document)
    print(result)