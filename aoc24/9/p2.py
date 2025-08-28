import re

#6327174563252

def main(line):
    checksum = 0
    sequence = []
    gap = False
    index = 0
    occurrence = {}

    for number in map(int, line): #map new function i learnt!!
        if gap:
            sequence.extend(["."] * number)
            gap = False
        else:
            sequence.extend([index] * number)
            occurrence[index] = occurrence.get(index, 0) + number
            index += 1
            gap = True

    length = len(sequence)
    gap_left = 0
    gap_right = 0
    num_left = length - 1
    num_right = length - 1
    loops = 0

    while gap_left < length:
        #get windows of gaps
        while gap_left < length and sequence[gap_left] != ".": #increment pointer if its not a dot
            gap_left += 1
        gap_right = gap_left + 1
        while gap_right < length and sequence[gap_right] == ".": #keep adding until you find a non dot
            gap_right += 1
        if sequence[gap_right] != ".": #its a dot
            gap_right -= 1

        while num_right >= 0 and (sequence[num_right] == "."):
            num_right -= 1
        num_left = num_right - 1
        while num_left < length and sequence[num_left] != "." and sequence[num_left] == sequence[num_right]: #keep subtracting until you find a dot
            num_left -= 1
        if sequence[num_left] == "." or sequence[num_left] != sequence[num_right]: #its a single number
            num_left += 1

        if gap_left > num_left:
            break
        
        #print(gap_left, gap_right, num_left, num_right)
        #print("".join(str(x) for x in sequence))

        if (gap_left != 0 and gap_right != 0) and abs(num_right - num_left + 1) <= abs(gap_right - gap_left + 1):
            fsize = num_right - num_left + 1
            sequence[gap_left:(gap_left + fsize)] = [sequence[num_left]] * fsize
            sequence[num_left:num_left + fsize] = ["."] * fsize
            gap_left = 0
            gap_right = 0 #reset the gap finder
            #gap_left = gap_right + 1  # continue searching from the next position after the current gap
        elif abs(num_right - num_left + 1) > abs(gap_right - gap_left + 1):
            #num_right = num_left - 1
            gap_left = gap_right + 1

        #i need to do it the other way round, find gaps suitable for hte number rather than number suitable for gap
            
        
    #print("".join(str(x) for x in sequence))

    for pos, val in enumerate(sequence):
        if val != ".":
            checksum += pos * val

    return checksum

if __name__ == "__main__":
    with open("test.txt") as file:
        document = [line.strip() for line in file]
    result = main(document[0])
    print(result)

