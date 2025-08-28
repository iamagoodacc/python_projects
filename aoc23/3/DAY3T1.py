print('\033[2J\033[H')

def gearratios(document):
    enginesum = 0

    # for rownum in range(len([char for char in document[0]])):
    #     for columnnum in range(len([line for line in file])):
    #         matrix.append([document[rownum], columnnum, ])

    indexestocheck = {}
    for lineindex, line in enumerate(document):
        num = ''
        for charindex, char in enumerate(line):
            if char.isdigit():
                num += char
            elif (not char.isalnum()):
                if num != '':
                    indexestocheck[num] = [lineindex, charindex-1-len(num)]
                num = ''
    
    for number in indexestocheck:
        startindexX = indexestocheck[number][1]
        startindexY = indexestocheck[number][0]
        numlength = len(number)

        char = ''
        numbervalid = False

        for row in range(max(startindexY-1, 0), min(startindexY+2, len(document))):
            for column in range(max(startindexX-1, 0), min(startindexX+numlength+1, len(document[0]))):
                if (not document[row][column].isalnum()) and document[row][column] != '.':
                    char = document[row][column]
                    numbervalid = True
        if numbervalid:
            print(number, char)
            enginesum += int(number)

    return enginesum


with open('D:\Visual Studio\Python\ADVENTOFCODE23\DAY3.txt') as file:
    document = [line.strip() for line in file]

result = gearratios(document)
print(result)