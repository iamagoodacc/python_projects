def main(line):
    stones = []
    for stone in line.split(" "):
        if stone == "0":
            stones.append("1")
        elif len(stone) % 2 == 0:
            stones.append(stone[:(len(stone)//2)])
            stones.append(stone[(len(stone)//2):])
        else:
            stones.append(str(int(stone)*2024))
    for _ in range(24):
        temp = stones.copy()
        stones = []
        if _ < 5:
            print(" ".join(x for x in temp))
        for stone in temp:
            if stone == "0":
                stones.append("1")
            elif len(stone) % 2 == 0:
                stones.append(str(int(stone[:(len(stone)//2)])))
                stones.append(str(int(stone[(len(stone)//2):])))
            else:
                stones.append(str(int(stone)*2024))
    return len(stones)

if __name__ == "__main__":
    with open("input.txt") as file:
        document = [line.strip() for line in file]
    result = main(document[0])
    print(result)
