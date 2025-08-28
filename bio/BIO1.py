def generate(startnum, endindex):
    currentstring = str(startnum)
    currentnum = startnum

    if endindex == 0:
        return 0

    while True:
        if endindex > 0:
            if len(currentstring) >= endindex+1: #in region
                if '987654321' in currentstring:
                    print(currentstring.index('987654321'))
                return int(currentstring[endindex-1])
            elif len(currentstring) < endindex+1:
                currentnum += 1
                currentstring += str(currentnum)

startnum = int(input('n: '))
endindex = int(input('i: '))

result = generate(startnum, endindex)
print(result)