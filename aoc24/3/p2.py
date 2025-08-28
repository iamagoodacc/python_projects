import re

def main(doc):
    sum = 0
    enabled = True
    for line in doc:
        matches = re.findall("mul\(\d*,\d*\)|do\(\)|don't\(\)", line, flags=re.IGNORECASE)
        if matches:
            for match in matches:
                if match == "do()": #a modifier
                    enabled = True
                elif match == "don't()":
                    enabled = False
                if enabled == True and match[0:3] == "mul":
                    nums = match[4:-1].split(",")
                    sum += int(nums[0]) * int(nums[1])
    return sum

if __name__ == "__main__":
    with open("input.txt") as file:
        document = [line.strip() for line in file]
    result = main(document)
    print(result)