import re

def main(line):
    checksum = 0
    sequence = []
    gap = False
    index = 0

    for number in map(int, line): #map new function i learnt!!
        if gap:
            sequence.extend(["."] * number)
            gap = False
        else:
            sequence.extend([index] * number)
            index += 1
            gap = True

    length = len(sequence)
    v = 0
    i = length - 1

    while v < length:
        while v < length and sequence[v] != ".":
            v += 1
        if v >= length:
            break

        while i >= 0 and (sequence[i] == "."):
            i -= 1
        if i < 0:
            break
        if v > i:
            break

        file_id = sequence[i]
        sequence[v] = file_id
        sequence[i] = "."

    for pos, val in enumerate(sequence):
        if val != ".":
            checksum += pos * val

    return checksum

if __name__ == "__main__":
    with open("input.txt") as file:
        document = [line.strip() for line in file]
    result = main(document[0])
    print(result)
