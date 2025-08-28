def trebuchet(document):
    totalsum = 0

    for line in document:
        numarray = []
        for char in line:
            if char.isdigit():
                numarray.append(char)
        
        totalsum += int(f'{str(numarray[0]) + str(numarray[-1])}')

    return totalsum


with open('D:\Visual Studio\Python\ADVENTOFCODE23\DAY1.txt') as file:
    document = [line.strip() for line in file]

result = trebuchet(document)
print(result)