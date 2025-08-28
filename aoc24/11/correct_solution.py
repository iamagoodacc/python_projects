from collections import Counter


def get_stones(puzzle_input):
    return list(map(int, puzzle_input.strip().split()))


def process_stone_optimized(stone):
    if stone == 0:
        return [1]

    if len(str(stone)) % 2 == 0:
        half_stone_length = int(len(str(stone)) / 2)
        left = int(str(stone)[:half_stone_length])
        right = int(str(stone)[half_stone_length:])
        return [left, right]

    result = stone * 2024

    return [result]


def solve_part_1(input):
    stones = get_stones(input)

    def process_stone(stone):
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            half_stone_length = int(len(str(stone)) / 2)
            left = int(str(stone)[:half_stone_length])
            right = int(str(stone)[half_stone_length:])
            new_stones.extend([left, right])
        else:
            new_stones.append(stone * 2024)

    for i in range(25):
        new_stones = []
        for stone in stones:
            process_stone(stone)

        stones = new_stones

    return len(stones)


def solve_part_2(input):
    stones = get_stones(input)

    # Use Counter instead of list to store stone counts
    current_stones = Counter(stones)

    for step in range(6):
        new_stones = Counter()
        print(current_stones)

        for stone, count in current_stones.items():
            processed = process_stone_optimized(stone)
            for new_stone in processed:
                new_stones[new_stone] += count

        current_stones = new_stones

    print(current_stones)
    return sum(current_stones.values())




if __name__ == '__main__':
    day = 11
    data = "125 17"

    # result_part_1 = solve_part_1(data)
    # print(f"Part 1: {result_part_1}")

    result_part_2 = solve_part_2(data)
    print(f"Part 2: {result_part_2}")