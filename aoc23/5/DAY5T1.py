def getlowestlocation(document):
    result = None
    seeds = document[0].split(': ')[1].split(' ')

    categorymap = {}
    for line in document:
        if line == document[0]:
            continue
        if 'map' in line:
            categorymap[line] = []
        else:
            categorymap[list(categorymap.keys())[-1]].append(line)

    for seednum in seeds:
        print('current seednumber:', seednum)
        currentdestination = seednum
        for map, values in (categorymap.items()):
            if map == 'soil-to-fertilizer map:':
                break

            print('current map:', map)
            print('current values:', values)

            for index, value in enumerate(values):
                split = value.split(' ')

                destinationstart = int(split[0])
                sourcestart = int(split[1])
                rangelength = (int(split[2]))

                if int(currentdestination) >= destinationstart and int(currentdestination) <= (destinationstart + rangelength - 1):
                    currentdestination = (sourcestart + rangelength - 1) - ((destinationstart + (rangelength - 1)) - int(currentdestination))
                    break
                
                print(currentdestination)
        
    return result


with open('D:\Visual Studio\Python\ADVENTOFCODE23\DAY5MINI.txt') as file:
    document = []
    for line in file:
        line = line.strip()
        if line.strip():
            document.append(line)

result = getlowestlocation(document)
print(result)