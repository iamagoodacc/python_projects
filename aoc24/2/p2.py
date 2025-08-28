
def scan(lines):
    safeT = 0
    unsafelines = []
    
    for line in lines:
        safe = True
        diffs = []
        
        for i in range(len(line) - 1):
            l = int(line[i])
            r = int(line[i + 1])
            diff = l - r
            diffs.append(diff)
            if abs(diff) < 1 or abs(diff) > 3:
                safe = False
        if safe:
            is_increasing = all(d > 0 for d in diffs)
            is_decreasing = all(d < 0 for d in diffs)
            if not (is_increasing or is_decreasing):
                safe = False
        
        if safe:
            safeT += 1
        else:
            unsafelines.append(line)
    
    return safeT, unsafelines


def main(doc):
    lines = []
    for line in doc: #initial
        line = line.split(" ")
        lines.append(line)
    oldt, lines = scan(lines) #replace old lines with new ones
        
    newsafe = 0
    for line in lines:
        newlines = []
        for i in range(len(line)):
            value = line.pop(i)
            newlines.append(line.copy())
            line.insert(i, value)
        val, _ = scan(newlines)
        if val >= 1:
            newsafe += 1

    return oldt + newsafe

if __name__ == "__main__":
    with open("input.txt") as file:
        document = [line.strip() for line in file]
    result = main(document)
    print(result)