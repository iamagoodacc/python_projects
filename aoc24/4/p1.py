import re

def main(doc):
    count = 0

    max_col = len(doc[0])
    max_row = len(doc)
    matrix = []

    for line in doc: #create matrix
        matrix.append(list(line))
    
    cols = [[] for _ in range(max_col)]
    rows = [[] for _ in range(max_row)]
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(matrix[y][x])
            rows[y].append(matrix[y][x])
            fdiag[x+y].append(matrix[y][x])
            bdiag[x-y-min_bdiag].append(matrix[y][x])

    for col in cols:
        matches = re.findall(r"(?=(XMAS|SAMX))", "".join(col), flags=re.IGNORECASE)
        count += len(matches)
    for row in rows:
        matches = re.findall(r"(?=(XMAS|SAMX))", "".join(row), flags=re.IGNORECASE)
        count += len(matches)
    for f in fdiag:
        matches = re.findall(r"(?=(XMAS|SAMX))", "".join(f), flags=re.IGNORECASE)
        count += len(matches)
    for b in bdiag:
        matches = re.findall(r"(?=(XMAS|SAMX))", "".join(b), flags=re.IGNORECASE)
        count += len(matches)
    return count

if __name__ == "__main__":
    with open("input.txt") as file:
        document = [line.strip() for line in file]
    result = main(document)
    print(result)