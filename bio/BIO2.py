def generateOdd(endvalue):
    arrayofnum = []
    currentindex = 0

    while True:
        if endvalue:
            if len(arrayofnum) >= endvalue:
                return arrayofnum
            elif len(arrayofnum) < endvalue:
                arrayofnum.append((2*currentindex)+1)
                currentindex += 1

def generateEven(endvalue):
    arrayofnum = []
    currentindex = 1

    while True:
        if endvalue:
            if len(arrayofnum) >= endvalue:
                return arrayofnum
            elif len(arrayofnum) < endvalue:
                arrayofnum.append((2*currentindex))
                currentindex += 1

def generateInt(endvalue):
    arrayofnum = []
    currentindex = 1

    while True:
        if endvalue:
            if len(arrayofnum) >= endvalue:
                return arrayofnum
            elif len(arrayofnum) < endvalue:
                for i in range(currentindex):
                    arrayofnum.append(int(currentindex))
                currentindex += 1

def manipulate(left, right, index):
    arrayofnum = []

    if index > 1:
        index += 1

    arrayofleft = []
    arrayofright = []
    if left == 'O' or left == 'T':
        arrayofleft = [1]
    elif left == 'E':
        arrayofleft = [2]

    if right == 'O' or right == 'T':
        arrayofright = [1]
    elif right == 'E':
        arrayofright = [2]

    if len(arrayofright) < index:
        currentindex = len(arrayofright)
        while True: #gen more values
            if len(arrayofright) >= index:
                break
            elif len(arrayofright) < index:
                if right == 'T':
                    for i in range(currentindex):
                        arrayofright.append(int(currentindex))
                elif right == 'O':
                    arrayofright.append((2*currentindex)+1)
                elif right == 'E':
                    arrayofright.append((2*currentindex))
                currentindex += 1
    if len(arrayofleft) < arrayofright[index-1]:
        currentindex = len(arrayofleft)
        while True: #gen more values
            if len(arrayofleft) >= arrayofright[index-1]:
                break
            elif len(arrayofleft) < arrayofright[index-1]:
                if left == 'T':
                    for i in range(currentindex):
                        arrayofleft.append(int(currentindex))
                elif left == 'O':
                    arrayofleft.append((2*currentindex)+1)
                elif left == 'E':
                    arrayofleft.append((2*currentindex))
                currentindex += 1

    if len(arrayofright) < arrayofleft[arrayofright[index-1]-1]:
        currentindex = len(arrayofright)+1
        while True: #gen more values
            if len(arrayofright) >= arrayofleft[arrayofright[index-1]-1]:
                break
            elif len(arrayofright) < arrayofleft[arrayofright[index-1]-1]:
                if right == 'T':
                    for i in range(currentindex):
                        arrayofright.append(int(currentindex))
                elif right == 'O':
                    arrayofright.append((2*currentindex)+1)
                elif right == 'E':
                    arrayofright.append((2*currentindex))
                currentindex += 1
    print(arrayofright)
    print(arrayofleft)
    print(index)
    print(arrayofright[index-1]-1)
    print(arrayofleft[arrayofright[index-1]-1])
    return arrayofright[arrayofleft[arrayofright[index-1]-1]-1]

def generateVals(string, endvalue):
    priority = ''
    begin = True
    for char in string:
        if char == '(':
            begin = True
        if char == ')':
            begin = False
        if begin == True:
            priority.append(char)
    
    if priority > 1:
        temp = ''
        for i in priority:
            if len(temp) != 2:
                temp.append(i)
            else:
                break
        result = manipulate(temp[0], temp[1], 1)

    arrayofnum = []
    currentindex = 1

    while True:
        if endvalue:
            if len(arrayofnum) >= endvalue:
                return arrayofnum
            elif len(arrayofnum) < endvalue:
                for i in range(currentindex):
                    arrayofnum.append(int(currentindex))
                currentindex += 1

string = input(': ')
place = input(': ')

result = manipulate('O', 'E', 1)
print(result)

# description = input('descrip: ')
# index = input('index: ')