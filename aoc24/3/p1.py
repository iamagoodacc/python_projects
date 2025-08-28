import re

def main(doc):
    sum = 0
    for line in doc:
        matches = re.findall("mul\(\d*,\d*\)", line, flags=re.IGNORECASE)
        if matches:
            for match in matches:
                nums = match[4:-1].split(",")
                sum += int(nums[0]) * int(nums[1])
    return sum

if __name__ == "__main__":
    with open("input.txt") as file:
        document = [line.strip() for line in file]
    result = main(document)
    print(result)