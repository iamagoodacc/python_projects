def explore_path(topomap, start):
    rows, cols = len(topomap), len(topomap[0])
    stack = [start]
    visited = set()
    rating = 0

    while stack:
        r, c = stack.pop()
        # if (r, c) in visited:
        #     continue
        visited.add((r, c))

        if topomap[r][c] == 9:
            rating += 1

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols: #and (nr, nc) not in visited:
                if topomap[nr][nc] == topomap[r][c] + 1: 
                    stack.append((nr, nc))

    return rating

def main(input_map):
    topomap = []
    for line in document:
        topomap.append([int(char) for char in line])

    trailheads = []
    for r, row in enumerate(topomap):
        for c, height in enumerate(row):
            if height == 0:
                trailheads.append((r, c))
    total_score = 0

    for trailhead in trailheads:
        total_score += explore_path(topomap, trailhead)

    return total_score

if __name__ == "__main__":
    with open("input.txt") as file:
        document = [line.strip() for line in file]
    result = main(document)
    print(result)
