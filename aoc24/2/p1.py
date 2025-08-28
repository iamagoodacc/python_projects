#['3', '6', '3', '5', '4', '3', '4']
def main(doc):
    l = 0
    r = 0
    safeT = 0
    for line in doc:
        safe = True
        diffs = 0

        line = line.split(" ")
        for i in range(len(line)):
            if i+1 < len(line):
                l = line[i]
                r = line[i+1]

                temp = diffs #original diffs
                diffs = diffs + (int(l) - int(r)) #find the difference and add it on
                if abs(temp) >= abs(diffs):
                    safe = False
                if abs(int(temp) - int(diffs)) == 0 or abs(int(temp) - int(diffs)) > 3:
                    safe = False

        if safe:
            safeT += 1
    return safeT

if __name__ == "__main__":
    with open("input.txt") as file:
        document = [line.strip() for line in file]
    result = main(document)
    print(result)