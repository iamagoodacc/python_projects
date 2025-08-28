wordtonum = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

reversedwordtonum = {
    'orez': 0,
    'eno': 1,
    'owt': 2,
    'eerht': 3,
    'ruof': 4,
    'evif': 5,
    'xis': 6,
    'neves': 7,
    'thgie': 8,
    'enin': 9,
}

def checknum(convertstring, dict):
    for value in dict:
        if value in convertstring:
            return dict[value]
    return False

def trebuchet(document):
    totalsum = 0

    for line in document:
        convertstring = ''
        numarray = []
        for char in line:
            if char.isalpha():
                convertstring += char
                if checknum(convertstring, wordtonum) != False:
                    numarray.append(checknum(convertstring, wordtonum))
                    break
            elif char.isdigit():
                numarray.append(char)
                break

        convertstring = ''
        for char in line[::-1]:
            if char.isalpha():
                convertstring += char
                if checknum(convertstring, reversedwordtonum) != False:
                    numarray.append(checknum(convertstring, reversedwordtonum))
                    break
            elif char.isdigit():
                numarray.append(char)
                break

        totalsum += int(f'{str(numarray[0]) + str(numarray[-1])}')

    return totalsum


with open('D:\Visual Studio\Python\ADVENTOFCODE23\DAY1.txt') as file:
    document = [line.strip() for line in file]

result = trebuchet(document)
print(result)