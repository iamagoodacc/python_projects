import re

def main(matrix):
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])

    def is_xmas(x, y):
        if (x - 1 >= 0 and y - 1 >= 0 and x + 1 < rows and y + 1 < cols):
            if (matrix[x - 1][y - 1] == "M" and
                matrix[x + 1][y + 1] == "S" and
                matrix[x][y] == "A" and
                matrix[x + 1][y - 1] == "M" and
                matrix[x - 1][y + 1] == "S"):
                return True
            elif (matrix[x - 1][y - 1] == "M" and
                matrix[x + 1][y + 1] == "S" and
                matrix[x][y] == "A" and
                matrix[x + 1][y - 1] == "S" and
                matrix[x - 1][y + 1] == "M"):
                return True
            elif (matrix[x - 1][y - 1] == "S" and
                matrix[x + 1][y + 1] == "M" and
                matrix[x][y] == "A" and
                matrix[x + 1][y - 1] == "M" and
                matrix[x - 1][y + 1] == "S"):
                return True
            elif (matrix[x - 1][y - 1] == "S" and
                matrix[x + 1][y + 1] == "M" and
                matrix[x][y] == "A" and
                matrix[x + 1][y - 1] == "S" and
                matrix[x - 1][y + 1] == "M"):
                return True
        return False

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            if is_xmas(x, y):
                count += 1

    return count

if __name__ == "__main__":
    with open("input.txt") as file:
        document = [line.strip() for line in file]
    result = main(document)
    print(result)