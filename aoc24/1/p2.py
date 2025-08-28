def main(doc):
    left = []
    right = {}
    for line in doc:
        line = line.split("   ")
        left.append(line[0])
        right[line[1]] = right.get(line[1], 0) + 1

    total = 0
    for num in left:
        if num in right:
            total += int(num)*right[num]

    return total

if __name__ == "__main__":
    with open("input.txt") as file:
        document = [line.strip() for line in file]
    result = main(document)
    print(result)