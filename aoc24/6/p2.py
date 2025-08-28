def main(doc):
    current_direction = "up"
    map = []
    start_position = None

    for y, line in enumerate(doc):
        row = []
        for x, char in enumerate(line):
            if char == "^":
                start_position = (x, y)
                current_direction = "up"
                row.append(".")
            else:
                row.append(char)
        map.append(row)

    def checker(map):
        visited_states = set()
        position = list(start_position)
        direction = current_direction

        while True:
            x, y = position
            state = (tuple(position), direction)

            #check for a loop i.e. if we visited here already
            if state in visited_states:
                return True

            visited_states.add(state)

            if direction == "up":
                if y - 1 >= 0 and map[y - 1][x] == "#":
                    direction = "right"
                else:
                    position[1] -= 1
            elif direction == "down":
                if y + 1 < len(map) and map[y + 1][x] == "#":
                    direction = "left"
                else:
                    position[1] += 1
            elif direction == "right":
                if x + 1 < len(map[0]) and map[y][x + 1] == "#":
                    direction = "down"
                else:
                    position[0] += 1
            elif direction == "left":
                if x - 1 >= 0 and map[y][x - 1] == "#":
                    direction = "up"
                else:
                    position[0] -= 1

            #bound check
            if position[0] < 0 or position[0] >= len(map[0]) or position[1] < 0 or position[1] >= len(map):
                return False
    obstruction_count = 0
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == ".":
                # temporarily place a wall
                map[y][x] = "#"
                if checker(map):
                    obstruction_count += 1
                map[y][x] = "."

    return obstruction_count


if __name__ == "__main__":
    with open("input.txt") as file:
        document = [line.strip() for line in file]
    result = main(document)
    print(result)
