import re

def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])
    
def checker(rules, order):
    for number in order:
        if number in rules:
            for mappednum in rules[number]: #if the number appears afterwards then the order is wrong
                if mappednum in order and order.index(mappednum) > order.index(number):
                    return False 
    return True
def main(doc):
    rules = {} #{45: [1,2,3]} but reverse
    orders = []
    total = 0

    for line in doc:
        if "|" in line:
            line = line.split("|")
            if line[1] in rules:
                rules[line[1]].append(line[0])
            else:
                rules[line[1]] = [line[0]]
        else:
            orders.append(line.split(","))

    validlists = []    
    for order in orders:
        valid = checker(rules, order)
        if valid:
            validlists.append(order)
    
    for order in validlists: #list with valid orders
        total += int(findMiddle(order))

    return total

if __name__ == "__main__":
    with open("input.txt") as file:
        document = [line.strip() for line in file]
    result = main(document)
    print(result)