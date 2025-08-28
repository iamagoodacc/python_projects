import re

def inBound(x, y, maxwidth, maxheight):
    if x < 0 or x > maxwidth:
        return False
    if y < 0 or y > maxheight:
        return False
    return True

def main(doc):
    antinodepositions = set()#(x,y)
    antennapositions = {}
    maxheight = len(doc)-1
    maxwidth = len(doc[0])-1
    for row, line in enumerate(doc):
        antennas = list(line)
        for column, antenna in enumerate(antennas):
            if antenna != ".":
                if antenna in antennapositions:
                    antennapositions[antenna].append((column, row))
                else:
                    antennapositions[antenna] = [(column, row)]

    for antennatype in antennapositions:
        for antenna1 in antennapositions[antennatype]:
            for antenna2 in antennapositions[antennatype]:
                xdiff = abs(antenna1[0] - antenna2[0])
                ydiff = abs(antenna1[1] - antenna2[1])
                if xdiff == 0 and ydiff == 0: #same point
                    continue
                x = antenna1[0]
                y = antenna1[1]

                antinodepositions.add((x,y)) #the points themselves are counted
                if antenna1[0] > antenna2[0] and antenna1[1] > antenna2[1]:
                    while inBound(x,y, maxwidth, maxheight):
                        x += xdiff
                        y += ydiff
                        if inBound(x, y, maxwidth, maxheight):
                            antinodepositions.add((x,y))
                    x = antenna2[0]
                    y = antenna2[1]
                    while inBound(x,y, maxwidth, maxheight):
                        x -= xdiff
                        y -= ydiff
                        if inBound(x,y, maxwidth, maxheight):
                            antinodepositions.add((x,y))
                elif antenna1[0] > antenna2[0] and antenna1[1] < antenna2[1]:
                    while inBound(x,y, maxwidth, maxheight):
                        x += xdiff
                        y -= ydiff
                        if inBound(x,y, maxwidth, maxheight):
                            antinodepositions.add((x,y))
                    x = antenna2[0]
                    y = antenna2[1]
                    while inBound(x,y, maxwidth, maxheight):
                        x -= xdiff
                        y += ydiff
                        if inBound(x,y, maxwidth, maxheight):
                            antinodepositions.add((x,y))
                elif antenna1[0] < antenna2[0] and antenna1[1] > antenna2[1]:
                    while inBound(x,y, maxwidth, maxheight):
                        x -= xdiff
                        y += ydiff
                        if inBound(x,y, maxwidth, maxheight):
                            antinodepositions.add((x,y))
                    x = antenna2[0]
                    y = antenna2[1]
                    while inBound(x,y, maxwidth, maxheight):
                        x += xdiff
                        y -= ydiff
                        if inBound(x,y, maxwidth, maxheight):
                            antinodepositions.add((x,y))
                elif antenna1[0] < antenna2[0] and antenna1[1] < antenna2[1]:
                    while inBound(x,y, maxwidth, maxheight):
                        x -= xdiff
                        y -= ydiff
                        if inBound(x,y, maxwidth, maxheight):
                            antinodepositions.add((x,y))
                    x = antenna2[0]
                    y = antenna2[1]
                    while inBound(x,y, maxwidth, maxheight):
                        x += xdiff
                        y += ydiff
                        if inBound(x,y, maxwidth, maxheight):
                            antinodepositions.add((x,y))

    return len(antinodepositions)



if __name__ == "__main__":
    with open("input.txt") as file:
        document = [line.strip() for line in file]
    result = main(document)
    print(result)
