import re

def main(line):
    checksum = 0
    sequence = ""
    gap = False
    gapstring = ""
    index = 0
    occurrence = {}
    for number in line:
        if gap == True:
            gap = False
            gapstring = gapstring + "."*int(number)
            sequence = sequence + ("."*int(number))
        elif gap == False:
            sequence = sequence + str(index)*int(number)
            gap = True
            occurrence[index] = int(number)
            index += 1

    while gapstring not in sequence:
        v = sequence.find(".")
        i = sequence.rfind(str(index))
        if i == -1:
            index -= 1
        elif occurrence[index] >= 1:
            occurrence[index] -= 1
            sequence = sequence[:v] + str(index) + sequence[v + 1:] #replace the dot with index
            sequence = sequence[:i] + "." + sequence[i + 1:] #replace index with a dot
        elif occurrence[index] < 1:
            index -= 1
    
    for x,y in enumerate(sequence):
        if y != ".":
            checksum += x*int(y)

    return checksum

if __name__ == "__main__":
    with open("test.txt") as file:
        document = [line.strip() for line in file]
    result = main(document[0])
    print(result)
