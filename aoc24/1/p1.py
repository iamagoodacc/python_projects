def main(doc):
    left = []
    right = []
    for line in doc:
        line = line.split("   ")
        left.append(line[0])
        right.append(line[1])
    
    left = sorted(left)
    right = sorted(right)

    total = 0
    for i in range(len(left)):
        total += abs(int(left[i]) - int(right[i]))

    return total

if __name__ == "__main__":
    with open("input.txt") as file:
        document = [line.strip() for line in file]
    result = main(document)
    print(result)