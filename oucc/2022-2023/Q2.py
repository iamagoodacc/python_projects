numbers = []

currinput = input()
numbers.append(currinput)

while currinput != '':
    currinput = input()
    if currinput != '':
        numbers.append(currinput)

print(numbers)

for number in numbers:
    print(int(number)*'-')